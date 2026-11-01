#!/usr/bin/env python3
"""Extract articles and embedded images from BYTE on CD-ROM data files."""

from __future__ import annotations

import argparse
import bisect
import json
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path

RECORD_MARKER = b"\x1eBYTE Magazine"
STYLE_MARKERS = {0x0F, 0x12}


@dataclass(frozen=True)
class ImageRecord:
    start: int
    end: int
    filename: str


def find_gif_end(data: bytes, start: int) -> int | None:
    if data[start : start + 6] not in (b"GIF87a", b"GIF89a"):
        return None
    cursor = start + 13
    if cursor > len(data):
        return None

    packed = data[start + 10]
    if packed & 0x80:
        cursor += 3 * (1 << ((packed & 0x07) + 1))

    def skip_subblocks(position: int) -> int | None:
        while position < len(data):
            size = data[position]
            position += 1
            if size == 0:
                return position
            position += size
            if position > len(data):
                return None
        return None

    while cursor < len(data):
        marker = data[cursor]
        cursor += 1
        if marker == 0x3B:
            return cursor
        if marker == 0x21:
            if cursor >= len(data):
                return None
            cursor = skip_subblocks(cursor + 1)
            if cursor is None:
                return None
        elif marker == 0x2C:
            if cursor + 9 > len(data):
                return None
            image_packed = data[cursor + 8]
            cursor += 9
            if image_packed & 0x80:
                cursor += 3 * (1 << ((image_packed & 0x07) + 1))
            if cursor >= len(data):
                return None
            cursor = skip_subblocks(cursor + 1)
            if cursor is None:
                return None
        else:
            return None
    return None


def extract_images(data: bytes, output_dir: Path) -> list[ImageRecord]:
    candidates: list[tuple[int, str, int]] = []
    for match in re.finditer(rb"GIF8[79]a", data):
        end = find_gif_end(data, match.start())
        if end is not None:
            candidates.append((match.start(), ".gif", end))

    cursor = 0
    while (start := data.find(b"\xff\xd8\xff", cursor)) >= 0:
        end_marker = data.find(b"\xff\xd9", start + 3)
        if end_marker < 0:
            break
        candidates.append((start, ".jpg", end_marker + 2))
        cursor = end_marker + 2

    candidates.sort()
    output_dir.mkdir(parents=True, exist_ok=True)
    images: list[ImageRecord] = []
    last_end = -1
    for start, suffix, end in candidates:
        if start < last_end:
            continue
        filename = f"image-{len(images) + 1:04d}{suffix}"
        (output_dir / filename).write_bytes(data[start:end])
        images.append(ImageRecord(start, end, filename))
        last_end = end
    return images


def text_chunks(
    data: bytes, start: int, end: int, images: list[ImageRecord]
) -> list[str]:
    image_starts = {image.start: image.end for image in images}
    chunks: list[str] = []
    current = bytearray()

    def flush() -> None:
        if current:
            value = current.decode("ascii", errors="ignore").strip()
            if len(value) >= 3:
                if re.match(
                    r"^(?:[A-Z][A-Z][a-z]|[a-z][A-Z][a-z]|[#&0][A-Z][a-z])", value
                ):
                    value = value[1:]
                chunks.append(re.sub(r"\s+", " ", value))
            current.clear()

    cursor = start
    while cursor < end:
        image_end = image_starts.get(cursor)
        if image_end is not None:
            flush()
            cursor = image_end
            continue

        if (
            data[cursor] == 0x06
            and cursor + 2 < end
            and data[cursor + 1] in STYLE_MARKERS
            and 0x20 <= data[cursor + 2] <= 0x7E
        ):
            flush()
            cursor += 3
            continue

        byte = data[cursor]
        if 0x20 <= byte <= 0x7E:
            current.append(byte)
        else:
            flush()
        cursor += 1
    flush()
    return chunks


def quote_yaml(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", normalized).strip("-").lower()
    return slug or "untitled"


def load_toc_titles(path: Path) -> dict[str, str]:
    if not path.is_file():
        return {}
    titles: dict[str, str] = {}
    for match in re.finditer(rb"[\x20-\x7e]{3,}", path.read_bytes()):
        value = match.group().decode("ascii").strip()
        key = re.sub(r"\s+", " ", value).casefold()
        titles.setdefault(key, value)
    return titles


def canonicalize_title(title: str, titles: dict[str, str]) -> str:
    for prefix_length in range(min(4, len(title))):
        candidate = title[prefix_length:].strip()
        key = re.sub(r"\s+", " ", candidate).casefold()
        if key in titles:
            return titles[key]
    return title


def parse_record(
    chunks: list[str],
) -> tuple[str, str, str, str, list[str], str | None]:
    publication = chunks[0] if chunks else "BYTE Magazine"
    issue = publication.partition(",")[2].strip()
    labels = chunks[1:]

    if len(labels) >= 3 and labels[0] == labels[1]:
        section, title, body = labels[0], labels[2], labels[3:]
    elif len(labels) >= 2:
        section, title, body = labels[0], labels[1], labels[2:]
    elif labels:
        section, title, body = "", labels[0], []
    else:
        section, title, body = "", "Untitled", []

    copyright = None
    if len(body) >= 2 and body[-2].lower() == "copyright":
        copyright = body[-1]
        body = body[:-2]
    return publication.partition(",")[0], issue, section, title, body, copyright


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source", type=Path, default=Path("/Volumes/BYTEDEMO/BYTE.DAT")
    )
    parser.add_argument("--toc", type=Path)
    parser.add_argument("--output", type=Path, default=Path("extracted"))
    args = parser.parse_args()

    data = args.source.read_bytes()
    toc_path = args.toc or args.source.with_suffix(".TOC")
    toc_titles = load_toc_titles(toc_path)
    starts: list[int] = []
    cursor = 0
    while (position := data.find(RECORD_MARKER, cursor)) >= 0:
        starts.append(position + 1)
        cursor = position + len(RECORD_MARKER)
    if not starts:
        raise SystemExit(f"No BYTE article records found in {args.source}")

    images = extract_images(data, args.output / "images")
    image_offsets = [image.start for image in images]
    articles_dir = args.output / "articles"
    articles_dir.mkdir(parents=True, exist_ok=True)
    index_entries: list[tuple[str, str]] = []

    for number, start in enumerate(starts):
        end = starts[number + 1] - 1 if number + 1 < len(starts) else len(data)
        chunks = text_chunks(data, start, end, images)
        publication, issue, section, title, body, copyright = parse_record(chunks)
        title = canonicalize_title(title, toc_titles)
        filename = f"{number + 1:04d}-{slugify(title)}.md"
        associated_images: list[ImageRecord] = []
        first_image = bisect.bisect_left(image_offsets, start)
        for image in images[first_image:]:
            if image.start >= end:
                break
            associated_images.append(image)

        frontmatter = [
            "---",
            f"title: {quote_yaml(title)}",
            f"publication: {quote_yaml(publication)}",
        ]
        if issue:
            frontmatter.append(f"issue: {quote_yaml(issue)}")
        if section:
            frontmatter.append(f"section: {quote_yaml(section)}")
        if copyright:
            frontmatter.append(f"copyright: {quote_yaml(copyright)}")
        frontmatter.extend(
            [
                f"source_file: {quote_yaml(args.source.name)}",
                f"source_offset: {quote_yaml(f'0x{start:08x}')}",
                "---",
            ]
        )

        content = [*frontmatter, "", f"# {title}"]
        if section:
            content.extend(["", f"*{section}*"])
        for paragraph in body:
            normalized = re.sub(r"\s+", " ", paragraph).casefold()
            if normalized in toc_titles:
                content.extend(["", f"## {toc_titles[normalized]}"])
            else:
                content.extend(["", paragraph])
        if associated_images:
            content.extend(["", "## Images"])
            for image in associated_images:
                image_path = f"../images/{image.filename}"
                content.extend(["", f"![{image.filename}]({image_path})"])

        (articles_dir / filename).write_text(
            "\n".join(content).rstrip() + "\n", encoding="utf-8"
        )
        index_entries.append((title, f"articles/{filename}"))

    expected_articles = {Path(path).name for _, path in index_entries}
    for existing in articles_dir.glob("[0-9][0-9][0-9][0-9]-*.md"):
        if existing.name not in expected_articles:
            existing.unlink()

    index = [
        "# BYTE on CD-ROM",
        "",
        f"Extracted {len(starts)} records and {len(images)} images from `{args.source.name}`.",
        "",
    ]
    for title, path in index_entries:
        index.append(f"- [{title}]({path})")
    (args.output / "index.md").write_text("\n".join(index) + "\n", encoding="utf-8")
    print(f"Extracted {len(starts)} records and {len(images)} images to {args.output}")


if __name__ == "__main__":
    main()

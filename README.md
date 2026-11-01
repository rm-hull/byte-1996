# BYTE CD-ROM

## Disc contents

The mounted read-only disc identifies itself as BYTE on CD-ROM, covering 1990-1996, published by Bureau van Dijk Electronic Publishing. The application is a Windows 3.x executable. The main files are `BYTE.DAT` (article/document data), `BYTE.TOC` (readable table of contents), and `BYTE.IDX` (binary search index). The legacy viewer is not required for extraction.

## Format

`BYTE.DAT` is a binary document stream, not a plain-text file. Document records are marked by the control byte `0x1e` followed by `BYTE Magazine`. Text fields are stored as readable ASCII among binary field and formatting data. The TOC contains issue labels, sections, and article headings; it also resolves several leading control characters that otherwise appear attached to titles.

The stream contains embedded GIF87a/GIF89a payloads. The extractor carves these as standalone images and associates them with the document whose byte range contains them.

## Output

- `extracted/index.md` lists all 313 extracted document records.
- `extracted/articles/` contains one Markdown file per record, with YAML frontmatter for title, publication, issue, section, copyright, source filename, and source offset when available.
- `extracted/images/` contains 318 validated GIF images. All are recognized as GIF files; no standalone JPEG files were produced.
- Article and TOC headings are represented as Markdown headings. Paragraphs and bylines are retained as separate text blocks.
- `extract_byte.py` reproduces the extraction with `python3 extract_byte.py` while `/Volumes/BYTEDEMO/` is mounted.

## Fidelity limits

The viewer's complete formatting schema has not been recovered. The extractor removes known run-control bytes and a narrow class of one-character style identifiers, but does not restore font, bold/italic, columns, or precise table layout. TOC-matched headings are promoted to Markdown subheadings; other styled text is kept as plain paragraphs. Extracted images are grouped at the end of their associated record because exact inline placement is not decoded. Non-ASCII text bytes are ignored by the current ASCII text parser, so a small number of accented characters may be lost.

## Attribution

Github Copilot assisted with extracting data from the CDROM image
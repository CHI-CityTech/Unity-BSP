#!/usr/bin/env python3
import sys
import os
import re
import base64
from pathlib import Path

try:
    import mammoth
    import html2text
except Exception as e:
    print("Missing Python dependencies. Install with: pip install -r requirements.txt")
    raise


def ensure_dirs(slug):
    originals = Path("docs/originals")
    proposals = Path("docs/proposals")
    assets = Path("docs/assets") / slug
    originals.mkdir(parents=True, exist_ok=True)
    proposals.mkdir(parents=True, exist_ok=True)
    assets.mkdir(parents=True, exist_ok=True)
    return originals, proposals, assets


def extract_data_images(html, assets_dir):
    # Find img tags with data URIs and save them
    def repl(match):
        nonlocal count
        data = match.group(1)
        header, b64 = data.split(',', 1)
        m = re.match(r'data:(image/[^;]+);base64', header)
        if not m:
            return match.group(0)
        mime = m.group(1)
        ext = {
            'image/png': 'png',
            'image/jpeg': 'jpg',
            'image/gif': 'gif'
        }.get(mime, 'bin')
        filename = f"image_{count}.{ext}"
        path = assets_dir / filename
        with open(path, 'wb') as f:
            f.write(base64.b64decode(b64))
        src = os.path.relpath(path, start=Path('docs/proposals'))
        count += 1
        return f'<img src="{src}" />'

    count = 1
    new_html = re.sub(r'<img[^>]+src="(data:[^"]+)"[^>]*>', repl, html)
    return new_html


def convert(input_path, slug=None):
    input_path = Path(input_path)
    if slug is None:
        slug = input_path.stem.replace(' ', '-').lower()

    originals, proposals, assets = ensure_dirs(slug)
    # copy original
    dest_original = originals / input_path.name
    if not dest_original.exists():
        import shutil
        shutil.copy2(input_path, dest_original)

    with open(input_path, 'rb') as docx_file:
        result = mammoth.convert_to_html(docx_file)
        html = result.value

    # extract images embedded as data URIs
    html = extract_data_images(html, assets)

    # convert html to markdown
    md = html2text.html2text(html)

    out_md = proposals / f"{slug}.md"
    with open(out_md, 'w', encoding='utf-8') as f:
        f.write(md)

    print(f"Converted: {input_path} -> {out_md}")
    print(f"Media (if any) saved to: {assets}")


def main():
    if len(sys.argv) < 2:
        print("Usage: convert_docx_mammoth.py <input.docx> [slug]")
        sys.exit(1)
    convert(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)


if __name__ == '__main__':
    main()

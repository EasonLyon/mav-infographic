import os
from pathlib import Path

ROOT = Path(__file__).parent

html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Workspace Home</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {{ font-family: 'Roboto', Arial, sans-serif; margin: 0; background: #f4f6fb; }}
        .container {{ max-width: 700px; margin: 40px auto; background: #fff; border-radius: 12px; box-shadow: 0 4px 24px rgba(0,0,0,0.08); padding: 32px; }}
        h1 {{ color: #2d3748; margin-bottom: 32px; }}
        .folder {{ font-size: 1.2em; font-weight: 700; color: #4a5568; margin-top: 32px; margin-bottom: 12px; }}
        ul {{ list-style: none; padding: 0; }}
        li {{ margin: 10px 0; }}
        a {{ text-decoration: none; color: #3182ce; font-size: 1.08em; transition: color 0.2s; }}
        a:hover {{ color: #2b6cb0; text-decoration: underline; }}
        .empty {{ color: #a0aec0; font-style: italic; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Workspace Home</h1>
        {folders_html}
    </div>
</body>
</html>'''.strip()

def get_html_files(folder_path):
    if not folder_path.exists() or not folder_path.is_dir():
        return []
    html_files = []
    for entry in os.listdir(folder_path):
        full_path = folder_path / entry
        if full_path.is_file() and entry.endswith('.html'):
            html_files.append(entry)
    return html_files

def build_folders_html(root):
    folders_html = ''
    for folder in sorted(os.listdir(root)):
        folder_path = root / folder
        if folder_path.is_dir():
            html_files = get_html_files(folder_path)
            if not html_files:
                continue  # Skip folders with no HTML files
            folders_html += f'<div class="folder">{folder}</div><ul>'
            for file in sorted(html_files):
                folders_html += f'<li><a href="{folder}/{file}">{file}</a></li>'
            folders_html += '</ul>'
    # Also include HTML files in the root directory
    root_html_files = [f for f in os.listdir(root) if f.endswith('.html') and (root / f).is_file() and f != 'index.html']
    if root_html_files:
        folders_html = f'<div class="folder">(Root)</div><ul>' + ''.join(
            f'<li><a href="{file}">{file}</a></li>' for file in sorted(root_html_files)
        ) + '</ul>' + folders_html
    return folders_html

if __name__ == '__main__':
    folders_html = build_folders_html(ROOT)
    html = html_template.format(folders_html=folders_html)
    with open(ROOT / 'index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("index.html generated successfully.")
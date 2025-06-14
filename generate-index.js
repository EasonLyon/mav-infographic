// This script dynamically lists all HTML files in the workspace and displays them in a styled way
const fs = require('fs');
const path = require('path');

const ROOT = __dirname;
const FOLDERS = ['Black_Wave', 'Black_Wave_Industry_Report', 'World_Masterclass'];

function getHtmlFiles(folder) {
    const dir = path.join(ROOT, folder);
    if (!fs.existsSync(dir)) return [];
    return fs.readdirSync(dir)
        .filter(f => f.endsWith('.html'))
        .map(f => ({
            name: f,
            path: `${folder}/${f}`
        }));
}

function render() {
    let html = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Workspace Home</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Roboto', Arial, sans-serif; margin: 0; background: #f4f6fb; }
        .container { max-width: 700px; margin: 40px auto; background: #fff; border-radius: 12px; box-shadow: 0 4px 24px rgba(0,0,0,0.08); padding: 32px; }
        h1 { color: #2d3748; margin-bottom: 32px; }
        .folder { font-size: 1.2em; font-weight: 700; color: #4a5568; margin-top: 32px; margin-bottom: 12px; }
        ul { list-style: none; padding: 0; }
        li { margin: 10px 0; }
        a { text-decoration: none; color: #3182ce; font-size: 1.08em; transition: color 0.2s; }
        a:hover { color: #2b6cb0; text-decoration: underline; }
        .empty { color: #a0aec0; font-style: italic; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Workspace Home</h1>`;
    FOLDERS.forEach(folder => {
        html += `<div class="folder">${folder}</div><ul>`;
        const files = getHtmlFiles(folder);
        if (files.length === 0) {
            html += `<li class="empty">(Empty folder)</li>`;
        } else {
            files.forEach(file => {
                html += `<li><a href="${file.path}">${file.name}</a></li>`;
            });
        }
        html += `</ul>`;
    });
    html += `</div></body></html>`;
    return html;
}

fs.writeFileSync(path.join(ROOT, 'index.html'), render());

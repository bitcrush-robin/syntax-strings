# Add syntax highlighting in Python multiline strings for VS Code

Adds syntax highlight support for various syntaxes inside Python multiline strings in VS Code.

Built from https://github.com/ptweir/python-string-sql

## Usage


### SQL

Insert `--sql`, `--beginsql`, or `--begin-sql` at the beginning of the part of the string you would like highlighted and a semicolon `;`, `--endsql`, or `--end-sql` at the end of the highlighted section.

### Python

Insert `#python`, `#beginpython`, or `#begin-python` at the beginning of the part of the string you would like highlighted, `#endpython`, or `#end-python` at the end of the highlighted section.

### HTML

Insert `<html>`, `<!-- html -->`, `--html`, `--beginhtml`, or `--begin-html` at the beginning of the part of the string you would like highlighted and `</html>`, `<!-- /html -->`, `--endhtml`, or `--end-html` at the end of the highlighted section.

### GLSL (WebGL)

Install the WebGL GLSL Editor, or your preferred GLSL syntax highlighter.

Multiline strings will highlight starting from `#version` and ending at `// endglsl` or `// end-glsl`.



## Requirements

- Visual Studio Code v1.32.0 recommended
- Comments at beginning and end of highlighted section in the string (see Usage section).

# Any syntax highlighting in Python multiline strings, HTML or PHP, for VS Code

Built from https://github.com/ptweir/python-string-sql

Adds syntax highlight support for various syntaxes inside various strings in VS Code.

## Installation

## Usage

Insert `--sql`, `--beginsql`, or `--begin-sql` at the beginning of the part of the string you would like highlighted and a semicolon, `--endsql`, or `--end-sql` at the end of the highlighted section.

### Snippets
begin typing `sql` and the autocomplete snippet will appear:

![Snippet](docs/snippet.gif)

### Keybindings

cmd+s (or ctrl+s on mac) - Insert the following snippet:
```
"""
--sql
SELECT
;
"""
```

## Requirements

- Visual Studio Code v1.32.0 recommended
- Comments at beginning and end of highlighted section in the string (see Usage section).

# books

Convert `.mobi` files to `.epub` format.

## Requirements

- Python 3
- [Calibre](https://calibre-ebook.com/) — provides the `ebook-convert` command-line tool.

  Install on Ubuntu/Debian:
  ```bash
  sudo apt-get install calibre
  ```
  Install on macOS (Homebrew):
  ```bash
  brew install --cask calibre
  ```

## Usage

```bash
python3 convert_mobi_to_epub.py [OPTIONS] PATH [PATH ...]
```

`PATH` can be:
- One or more individual `.mobi` files
- One or more directories (searched recursively for `.mobi` files)
- Any combination of the above

### Options

| Option | Description |
|--------|-------------|
| `-o DIR`, `--output-dir DIR` | Write all `.epub` files into `DIR` (default: same folder as each source file) |

### Examples

Convert a single file:
```bash
python3 convert_mobi_to_epub.py mybook.mobi
```

Convert all `.mobi` files in a directory:
```bash
python3 convert_mobi_to_epub.py /path/to/books/
```

Convert multiple files and directories, writing output to a specific folder:
```bash
python3 convert_mobi_to_epub.py book1.mobi book2.mobi /path/to/more/books/ -o /path/to/epubs/
```

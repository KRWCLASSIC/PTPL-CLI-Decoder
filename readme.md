# `PTPL` CLI Decoder

## Overview

The PTPL CLI Decoder is a command-line tool designed to decode `.ptpl` files into XML format. This tool is made for people working with PTPL files generated by the MCreator program.

## How it works

- Reads `.ptpl` file compressed in gzip format.
- Decodes the base64 content of the PTPL file.
- Formats the decoded XML content for better readability.
- Option to save the output to an XML file or print it to the console.
- Verbose mode for detailed output during the decoding process.

## Usage

To use the PTPL CLI Decoder, run the following command in your terminal:

```python main.py <path_to_ptpl_file> [--output <output_path>] [--verbose]```

### Arguments

- `<path_to_ptpl_file>`: The path to the `.ptpl` file you want to decode.
- `--output`, `-o`: (Optional) Specify the path to save the extracted XML file. If not provided, the XML content will be printed to the console.
- `--verbose`, `-v`: (Optional / Useless) Enable verbose output for detailed processing information.

## Notice

> **This tool is intended for future use in the PTPL Editor project. PTPL files are generated by the MCreator program.**

## Requirements

- Python 3.x
- Required libraries: `argparse`, `gzip`, `base64`, `xml.dom.minidom`

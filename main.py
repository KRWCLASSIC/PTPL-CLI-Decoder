import argparse
import gzip
import base64
from xml.dom.minidom import parseString

def decode_ptpl(file_path, output_path=None, verbose=False):
    if not file_path.endswith(".ptpl"):
        raise ValueError("File must have a .ptpl extension.")

    if verbose:
        print(f"Reading {file_path} as a gzip archive...")
    try:
        with gzip.open(file_path, 'rb') as gz_file:
            inner_ptpl_data = gz_file.read()
    except Exception as e:
        raise RuntimeError(f"Failed to read the .ptpl file as a gzip archive: {e}")

    if verbose:
        print("Decoding base64 content...")
    try:
        padding = len(inner_ptpl_data) % 4
        if padding != 0:
            inner_ptpl_data += b'=' * (4 - padding)
        xml_data = base64.b64decode(inner_ptpl_data).decode('utf-8')
    except Exception as e:
        raise RuntimeError(f"Failed to decode base64 content: {e}")

    if verbose:
        print("Formatting XML content...")
    try:
        pretty_xml = parseString(xml_data).toprettyxml(indent="  ")
    except Exception as e:
        raise RuntimeError(f"Failed to format XML content: {e}")

    if output_path:
        output_path = output_path if output_path.endswith(".xml") else f"{output_path}.xml"
        if verbose:
            print(f"Saving XML content to {output_path}...")
        try:
            with open(output_path, 'w', encoding='utf-8') as output_file:
                output_file.write(pretty_xml)
            print(f"XML content saved to {output_path}")
        except Exception as e:
            raise RuntimeError(f"Failed to save XML content to file: {e}")
    else:
        if verbose:
            print("Printing XML content:")
        print(pretty_xml)

def main():
    parser = argparse.ArgumentParser(description="Decode .ptpl files into XML.")
    parser.add_argument("file", help="Path to the .ptpl file to decode.")
    parser.add_argument("--output", "-o", help="Path to save the extracted XML file.")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose output.")
    args = parser.parse_args()

    try:
        decode_ptpl(args.file, args.output, args.verbose)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

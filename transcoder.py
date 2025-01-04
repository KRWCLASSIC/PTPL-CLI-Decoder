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

def encode_ptpl(file_path, output_path=None, verbose=False):
    if not file_path.endswith(".xml"):
        raise ValueError("File must have a .xml extension.")

    if verbose:
        print(f"Reading {file_path} as an XML file...")
    try:
        with open(file_path, 'r', encoding='utf-8') as input_file:
            xml_data = input_file.read()
    except Exception as e:
        raise RuntimeError(f"Failed to read the XML file: {e}")

    if verbose:
        print("Encoding XML content to base64...")
    try:
        encoded_data = base64.b64encode(xml_data.encode('utf-8'))
    except Exception as e:
        raise RuntimeError(f"Failed to encode XML content: {e}")

    if verbose:
        print("Compressing data with gzip...")
    try:
        compressed_data = gzip.compress(encoded_data)
    except Exception as e:
        raise RuntimeError(f"Failed to compress data: {e}")

    output_path = output_path if output_path.endswith(".ptpl") else f"{output_path}.ptpl"
    if verbose:
        print(f"Saving encoded data to {output_path}...")
    try:
        with open(output_path, 'wb') as output_file:
            output_file.write(compressed_data)
        print(f"Encoded data saved to {output_path}")
    except Exception as e:
        raise RuntimeError(f"Failed to save encoded data to file: {e}")

def main():
    parser = argparse.ArgumentParser(description="Encode or decode .ptpl files.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-d", "--decode", action="store_true", help="Decode a .ptpl file.")
    group.add_argument("-e", "--encode", action="store_true", help="Encode an XML file into .ptpl format.")
    parser.add_argument("file", help="Path to the input file.")
    parser.add_argument("--output", "-o", help="Path to save the output file.")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose output.")
    args = parser.parse_args()

    try:
        if args.decode:
            decode_ptpl(args.file, args.output, args.verbose)
        elif args.encode:
            encode_ptpl(args.file, args.output, args.verbose)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

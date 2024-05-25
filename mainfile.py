import argparse
import json
import yaml
import xml.etree.ElementTree as ET
import os
import sys

def parse_arguments():
    parser = argparse.ArgumentParser(description="Load and save JSON, YAML, or XML files.")
    parser.add_argument("input_file", help="Path to the input JSON, YAML, or XML file.")
    parser.add_argument("output_file", help="Path to the output JSON, YAML, or XML file.")
    return parser.parse_args()

def loading_file(input_file):
    if not os.path.isfile(input_file):
        print(f"Error: The file {input_file} does not exist.", file=sys.stderr)
        sys.exit(1)

    file_extension = os.path.splitext(input_file)[1].lower()
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            if file_extension == ".json":
                return json.load(file)
            elif file_extension == ".yml" or file_extension == ".yaml":
                return yaml.safe_load(file)
            elif file_extension == ".xml":
                tree = ET.parse(file)
                return tree.getroot()
            else:
                print(f"Error: Unsupported file format {file_extension}.", file=sys.stderr)
                sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: The file {input_file} contains invalid JSON. {e}", file=sys.stderr)
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"Error: The file {input_file} contains invalid YAML. {e}", file=sys.stderr)
        sys.exit(1)
    except ET.ParseError as e:
        print(f"Error: The file {input_file} contains invalid XML. {e}", file=sys.stderr)
        sys.exit(1)

def save_file(output_file, data):
    file_extension = os.path.splitext(output_file)[1].lower()
    try:
        with open(output_file, "w", encoding="utf-8") as file:
            if file_extension == ".json":
                json.dump(data, file, indent=4)
            elif file_extension == ".yml" or file_extension == ".yaml":
                yaml.dump(data, file, default_flow_style=False)
            elif file_extension == ".xml":
                tree = ET.ElementTree(data)
                tree.write(file, encoding="unicode", xml_declaration=True)
            else:
                print(f"Error: Unsupported file format {file_extension}.", file=sys.stderr)
                sys.exit(1)
    except IOError as e:
        print(f"Error: Unable to write to file {output_file}. {e}", file=sys.stderr)
        sys.exit(1)

def main():
    args = parse_arguments()
    input_file = args.input_file
    output_file = args.output_file

    # Load data from input file
    obj = loading_file(input_file)

    # Save data to output file
    save_file(output_file, obj)

if __name__ == "__main__":
    main()





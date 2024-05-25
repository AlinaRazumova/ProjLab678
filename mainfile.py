import argparse
import json
import os
import sys

def parse_arguments():
    parser = argparse.ArgumentParser(description="Load and save JSON files.")
    parser.add_argument("input_file", help="Path to the input JSON file.")
    parser.add_argument("output_file", help="Path to the output JSON file.")
    return parser.parse_args()

def loading_json(input_file):
    if not os.path.isfile(input_file):
        print(f"Error: The file {input_file} does not exist.", file=sys.stderr)
        sys.exit(1)
    
    try:
        with open(input_file, "r", encoding="utf-8") as file_js:
            json_obj = json.load(file_js)
            return json_obj
    except json.JSONDecodeError as e:
        print(f"Error: The file {input_file} contains invalid JSON. {e}", file=sys.stderr)
        sys.exit(1)

def save_json(output_file, data):
    try:
        with open(output_file, "w", encoding="utf-8") as file_js:
            json.dump(data, file_js, indent=4)
    except IOError as e:
        print(f"Error: Unable to write to file {output_file}. {e}", file=sys.stderr)
        sys.exit(1)

def main():
    args = parse_arguments()
    input_file = args.input_file
    output_file = args.output_file
    
    if os.path.splitext(input_file)[1].lower() == ".json":
        obj = loading_json(input_file)
        save_json(output_file, obj)
    else:
        print(f"Error: The input file {input_file} is not a JSON file.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()


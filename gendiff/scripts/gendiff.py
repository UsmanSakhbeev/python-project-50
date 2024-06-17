import argparse
import json
import os


def main():
    parser = argparse.ArgumentParser(description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file", type=str, help="First configuration file")
    parser.add_argument("second_file", type=str, help="Second configuration file")
    parser.add_argument(
        "-f", "--format", type=str, help="set format of output"
    )

    args = parser.parse_args()

    print(f"First file: {args.first_file}")
    print(f"Second file: {args.second_file}")
    print(f"Output format: {args.format}")
    
    with open(args.first_file, 'r') as file:
        file1 = json.load(file)
    with open(args.second_file, 'r') as file:
        file2 = json.load(file)

    
    diff = compare_json(file1, file2)
    print_diff(diff)


def compare_json(file1, file2, path=""):
    diffs = {}
    for key in file1.keys() | file2.keys():
        if key not in file1:
            diffs[f"{path}/{key}"] = f"Key '{key}' added in second file"
        elif key not in file2:
            diffs[f"{path}/{key}"] = f"Key '{key}' removed in second file"
        else:
            if isinstance(file1[key], dict) and isinstance(file2[key], dict):
                nested_diff = compare_json(file1[key], file2[key], path + "/" + key)
                diffs.update(nested_diff)
            elif file1[key] != file2[key]:
                diffs[f"{path}/{key}"] = f"Value changed from {file1[key]} to {file2[key]}"
    return diffs


def print_diff(diff):
    if not diff:
        print("No differences found.")
    else:
        for key, message in diff.items():
            print(f"{key}: {message}")


if __name__ == "__main__":
    main()
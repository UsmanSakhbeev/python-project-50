import argparse
from gendiff.scripts.parse_files import get_text
from gendiff.scripts.formatter import stylish_formatter
from gendiff.scripts.formatter import plain_formatter
from gendiff.scripts.formatter import json_formatter


def main():
    parser = argparse.ArgumentParser(
        description="Compares and shows a difference.")
    parser.add_argument("first_file", type=str, help="First conf file")
    parser.add_argument("second_file", type=str, help="Second conf file")
    parser.add_argument(
        "-f", "--format", type=str, default="stylish", choices=["stylish", "json"],
        help="set format of output (default: stylish)")

    args = parser.parse_args()
    file1, file2 = get_text(args.first_file, args.second_file)
    diff = generate_diff(file1, file2, args.format)
    return diff
    


def generate_diff(first_file, second_file, format):
    def build(node1, node2):
        sorted_keys = sorted(node1.keys() | node2.keys())
        diff = {}
        for key in sorted_keys:
            if key not in node1:
                diff[key] = {"type": "added", "value": node2[key]}
            elif key not in node2:
                diff[key] = {"type": "deleted", "value": node1[key]}
            elif isinstance(node1[key], dict) and isinstance(node2[key], dict):
                diff[key] = {"type": "chained", "value": build(node1[key], node2[key])}
            elif key in node1 and key in node2:
                if node1[key] != node2[key]:
                    diff[key] = {"type": "changed", "old_value": node1[key], "new_value": node2[key]}
                else:
                    diff[key] = {"type": "unchanged", "value": node1[key]}

        return diff
    diff = build(first_file, second_file)
    
    if format == "stylish":
        return stylish_formatter(diff)
    elif format == "plain":
        return plain_formatter(diff)
    elif format == "json":
        return json_formatter(diff)


if __name__ == "__main__":
    main()

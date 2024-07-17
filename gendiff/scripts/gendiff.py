#!/usr/bin/env python3


import argparse
import json
import yaml
from gendiff.scripts.formatter import stylish_formatter
from gendiff.scripts.formatter import plain_formatter
from gendiff.scripts.formatter import json_formatter


def main():
    parser = argparse.ArgumentParser(
        description="Compares and shows a difference.")
    parser.add_argument("first_file", type=str, help="First conf file")
    parser.add_argument("second_file", type=str, help="Second conf file")
    parser.add_argument(
        "-f", "--format",
        type=str, default="stylish",
        choices=["stylish", "json", "plain"],
        help="set format of output (default: stylish)")

    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


def generate_diff(first_file, second_file, format="stylish"):
    node1 = read_file(first_file)
    node2 = read_file(second_file)
    diff = build_diff(node1, node2)

    if format == "stylish":
        return stylish_formatter(diff)
    elif format == "plain":
        return plain_formatter(diff)
    elif format == "json":
        return json_formatter(diff)


def build_diff(node1, node2):
    sorted_keys = sorted(node1.keys() | node2.keys())
    diff = {}

    for key in sorted_keys:
        if key not in node1:
            diff[key] = {"type": "added", "value": node2[key]}
        elif key not in node2:
            diff[key] = {"type": "deleted", "value": node1[key]}
        elif isinstance(node1[key], dict) and isinstance(node2[key], dict):
            diff[key] = {
                "type": "chained", "value": build_diff(node1[key], node2[key])}
        elif key in node1 and key in node2:
            evaluate_changes(node1, node2, key)
    return diff


def evaluate_changes(node1, node2, key):
    if node1[key] != node2[key]:
        return {
            "type": "changed",
            "old_value": node1[key],
            "new_value": node2[key]}
    else:
        return {"type": "unchanged", "value": node1[key]}


def read_file(path_to_file: str):
    if '.yml' in path_to_file or '.yaml' in path_to_file:
        with open(path_to_file) as file_to_parse:
            result = yaml.load(file_to_parse, Loader=yaml.FullLoader)
    elif '.json' in path_to_file:
        with open(path_to_file) as file_to_parse:
            result = json.load(file_to_parse)
    else:
        result = {'Exception': 'file has wrong format'}
    return result


if __name__ == "__main__":
    main()

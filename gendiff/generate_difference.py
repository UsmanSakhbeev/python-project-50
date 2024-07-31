from gendiff.formatter import (
    format_to_json,
    format_to_plain,
    format_to_stylish,
)
from gendiff.parse_files import read_file


def generate_diff(first_file, second_file, format="stylish"):
    node1 = read_file(first_file)
    node2 = read_file(second_file)
    diff = build_diff(node1, node2)

    if format == "stylish":
        return format_to_stylish(diff)
    elif format == "plain":
        return format_to_plain(diff)
    elif format == "json":
        return format_to_json(diff)
    else:
        raise ValueError(f"Unsupported format {format}")


def build_diff(node1, node2):
    sorted_keys = sorted(node1.keys() | node2.keys())
    diff = {}

    for key in sorted_keys:
        if key not in node1:
            diff[key] = {"type": "added", "value": node2[key]}
        elif key not in node2:
            diff[key] = {"type": "deleted", "value": node1[key]}
        elif isinstance(node1[key], dict) and isinstance(node2[key], dict):
            diff[key] = {"type": "chained", "value": build_diff(node1[key], node2[key])}
        elif key in node1 and key in node2:
            diff[key] = evaluate_changes(node1, node2, key)
    return diff


def evaluate_changes(node1, node2, key):
    if node1[key] != node2[key]:
        return {"type": "changed", "old_value": node1[key], "new_value": node2[key]}
    else:
        return {"type": "unchanged", "value": node1[key]}

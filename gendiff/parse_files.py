import json

import yaml


def get_text(
    path_to_file,
):
    if path_to_file.endswith(".json"):
        with open(path_to_file) as f:
            path = json.load(f)
            format = "json"
    elif path_to_file.endswith(".yml") or path_to_file.endswith(".yaml"):
        with open(path_to_file) as f:
            path = yaml.safe_load(f)
            format = "yml"
    return path, format


def read_file(path_to_file: str):
    if ".yml" in path_to_file or ".yaml" in path_to_file:
        with open(path_to_file) as file_to_parse:
            result = yaml.load(file_to_parse, Loader=yaml.FullLoader)
    elif ".json" in path_to_file:
        with open(path_to_file) as file_to_parse:
            result = json.load(file_to_parse)
    else:
        result = {"Exception": "file has wrong format"}
    return result


def create_path(parents, child):
    if parents == "":
        return child
    else:
        return f"{parents}.{child}"


def to_string(value, format="without_quotes"):
    if value is False:
        return "false"
    elif value is True:
        return "true"
    elif value is None:
        return "null"
    elif format == "single_quotes":
        if isinstance(value, int):
            return f"{str(value)}"
        else:
            return f"'{str(value)}'"
    elif format == "double_quotes":
        if isinstance(value, int):
            return f"{str(value)}"
        else:
            return f'"{str(value)}"'
    elif format == "without_quotes":
        return f"{str(value)}"

import json

import yaml


def parse_file_content(content: str, file_extension: str):
    if file_extension in [".yml", ".yaml"]:
        return yaml.load(content, Loader=yaml.FullLoader)
    elif file_extension == ".json":
        return json.loads(content)
    else:
        return {"Exception": "file has wrong format"}


def read_file(path_to_file: str):
    file_extension = path_to_file[path_to_file.rfind("."):]
    try:
        with open(path_to_file, "r") as file_to_parse:
            content = file_to_parse.read()
        return parse_file_content(content, file_extension)
    except Exception as e:
        return {"Exception": str(e)}


def create_path(parents, child):
    if parents == "":
        return child
    else:
        return f"{parents}.{child}"

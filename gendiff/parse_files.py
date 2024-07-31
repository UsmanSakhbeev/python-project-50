import json
import yaml


def get_text(path_to_file, ):
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


def main():
    return


if __name__ == '__main__':
    main()

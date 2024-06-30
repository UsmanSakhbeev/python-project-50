import json
import yaml


def get_text(file_path1, file_path2):
    if file_path1.endswith(".json"):
        with open(file_path1) as f:
            file1 = json.load(f)
        with open(file_path2) as f:
            file2 = json.load(f)
    elif file_path1.endswith(".yml") or file_path1.endswith(".yaml"):
        with open(file_path1) as f:
            file1 = yaml.safe_load(f)
        with open(file_path2) as f:
            file2 = yaml.safe_load(f)
    return file1, file2


def main():
    return


if __name__ == '__main__':
    main()

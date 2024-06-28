import argparse
import json


def main():
    parser = argparse.ArgumentParser(
        description="Compares and shows a difference.")
    parser.add_argument("first_file", type=str, help="First conf file")
    parser.add_argument("second_file", type=str, help="Second conf file")
    parser.add_argument(
        "-f", "--format", type=str, help="set format of output")

    args = parser.parse_args()

    diff = generate_diff(args.first_file, args.second_file)
    print_diff(diff)


def get_text(file_path: str):
    with open(file_path) as file:
        return json.load(file)


def generate_diff(file_path1, file_path2, path=""):
    file1 = get_text(file_path1)
    file2 = get_text(file_path2)
    output = {}
    sorted_keys = sorted(file1.keys() | file2.keys())
    for key in sorted_keys:
        if key not in file1:
            output[f" + {key}"] = file2[key]
        elif key not in file2:
            output[f" - {key}"] = file1[key]
        elif key in file1 and key in file2:
            if file1[key] == file2[key]:
                output[f"   {key}"] = file1[key]
            else:
                output[f" - {key}"] = file1[key]
                output[f" + {key}"] = file2[key]
    return output


def print_diff(diff):
    print("{")
    for key, message in diff.items():
        print(f"{key}: {message}")
    print("}")


if __name__ == "__main__":
    main()

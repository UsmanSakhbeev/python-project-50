import argparse
from gendiff.scripts.parse_files import get_text


def main():
    parser = argparse.ArgumentParser(
        description="Compares and shows a difference.")
    parser.add_argument("first_file", type=str, help="First conf file")
    parser.add_argument("second_file", type=str, help="Second conf file")
    parser.add_argument(
        "-f", "--format", type=str, help="set format of output")

    args = parser.parse_args()
    file1, file2 = get_text(args.first_file, args.second_file)
    return generate_diff(file1, file2)


def generate_diff(file1, file2, path=""):
    output = ["{"]
    sorted_keys = sorted(file1.keys() | file2.keys())
    for key in sorted_keys:
        if key not in file1:
            output.append(f"  + {key}: {file2[key]}")
        elif key not in file2:
            output.append(f"  - {key}: {file1[key]}")
        elif key in file1 and key in file2:
            if file1[key] == file2[key]:
                output.append(f"    {key}: {file1[key]}")
            else:
                output.append(f"  - {key}: {file1[key]}")
                output.append(f"  + {key}: {file2[key]}")
    output.append('}')
    return "\n".join(output).lower().strip()


if __name__ == "__main__":
    main()

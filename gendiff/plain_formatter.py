from gendiff.parse_files import create_path


def format_to_plain(value):
    def build(current_value, path):
        result = []
        for key, val in current_value.items():
            string = ""
            match val.get("type"):
                case "chained":
                    string = build(val["value"], create_path(path, key))
                case "added":
                    string = create_added(path, key, val)
                case "changed":
                    string = create_changed(path, key, val)
                case "deleted":
                    string = f"Property '{create_path(path, key)}' was removed"
                case _:
                    continue
            result.append(string)
        return "\n".join(result)

    return build(value, "")


def create_added(path, key, val):
    if isinstance(val["value"], dict):
        value = "[complex value]"
    else:
        value = plain_to_string(val["value"])
    return f"Property '{create_path(path, key)}' was added with value: {value}"


def create_changed(path, key, val):
    value1 = "[complex value]"
    value2 = "[complex value]"

    if isinstance(val["old_value"], dict):
        value2 = plain_to_string(val["new_value"])
    elif isinstance(val["new_value"], dict):
        value1 = plain_to_string(val["old_value"])
    else:
        value1 = plain_to_string(val["old_value"])
        value2 = plain_to_string(val["new_value"])
    return (
        f"Property '{create_path(path, key)}' was updated."
        + f" From {value1} to {value2}"
    )


def plain_to_string(value):
    if value is False:
        return "false"
    elif value is True:
        return "true"
    elif value is None:
        return "null"
    elif isinstance(value, int):
        return f"{str(value)}"
    else:
        return f"'{str(value)}'"

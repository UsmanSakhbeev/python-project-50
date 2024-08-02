from gendiff.parse_files import create_path, to_string


def format_to_plain(value):
    def build(current_value, current_path):
        result = []
        for key, val in current_value.items():
            current_string = ""
            match val.get("type"):
                case "chained":
                    current_string = build(val["value"], create_path(current_path, key))
                case "added":
                    if isinstance(val["value"], dict):
                        current_string = f"Property '{create_path(current_path, key)}' was added with value: [complex value]"
                    else:
                        current_string = f"Property '{create_path(current_path, key)}' was added with value: {to_string(val['value'], 'single_quotes')}"
                case "changed":
                    if isinstance(val["old_value"], dict):
                        current_string = f"Property '{create_path(current_path, key)}' was updated. From [complex value] to {to_string(val['new_value'], 'single_quotes')}"
                    elif isinstance(val["new_value"], dict):
                        current_string = f"Property '{create_path(current_path, key)}' was updated. From {to_string(val['old_value'], 'single_quotes')} to [complex value]"
                    else:
                        current_string = f"Property '{create_path(current_path, key)}' was updated. From {to_string(val['old_value'], 'single_quotes')} to {to_string(val['new_value'], 'single_quotes')}"
                case "deleted":
                    current_string = (
                        f"Property '{create_path(current_path, key)}' was removed"
                    )
                case _:
                    continue
            result.append(current_string)
        return "\n".join(result)

    return build(value, "")

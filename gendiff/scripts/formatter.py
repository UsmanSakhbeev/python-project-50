def stylish_formatter(value):

    def build(current_value, depth, replacer=" "):
        if not isinstance(current_value, dict):
            return format_exception_check(current_value)

        indent = replacer * depth
        child_depth = depth + 4
        result = ["{"]

        for key, val in current_value.items():
            string = ""
            if isinstance(val, dict):
                match val.get("type"):
                    case "chained":
                        string = (
                            f"{indent}    {key}: {build(val['value'], child_depth)}"
                        )
                    case "added":
                        string = (
                            f"{indent}  + {key}: {build(val['value'], child_depth)}"
                        )
                    case "deleted":
                        string = (
                            f"{indent}  - {key}: {build(val['value'], child_depth)}"
                        )
                    case "unchanged":
                        string = (
                            f"{indent}    {key}: {build(val['value'], child_depth)}"
                        )
                    case "changed":
                        string = (
                            f"{indent}  - {key}: {build(val['old_value'], child_depth)}"
                        )
                        result.append(string)
                        string = (
                            f"{indent}  + {key}: {build(val['new_value'], child_depth)}"
                        )
                    case _:
                        string = f"{indent}    {key}: {build(val, child_depth)}"
                result.append(string)
            else:
                string = f"{indent}    {key}: {build(val, child_depth)}"
                result.append(string)

        result.append(indent + "}")
        return "\n".join(result)

    return build(value, 0)


def plain_formatter(value):
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
                        current_string = f"Property '{create_path(current_path, key)}' was added with value: {format_exception_check(val['value'], 'single_quotes')}"
                case "changed":
                    if isinstance(val["old_value"], dict):
                        current_string = f"Property '{create_path(current_path, key)}' was updated. From [complex value] to {format_exception_check(val['new_value'], 'single_quotes')}"
                    elif isinstance(val["new_value"], dict):
                        current_string = f"Property '{create_path(current_path, key)}' was updated. From {format_exception_check(val['old_value'], 'single_quotes')} to [complex value]"
                    else:
                        current_string = f"Property '{create_path(current_path, key)}' was updated. From {format_exception_check(val['old_value'], 'single_quotes')} to {format_exception_check(val['new_value'], 'single_quotes')}"
                case "deleted":
                    current_string = (
                        f"Property '{create_path(current_path, key)}' was removed"
                    )
                case _:
                    continue
            result.append(current_string)
        return "\n".join(result)

    return build(value, "")


def json_formatter(value):
    replacer = " "
    spaces_count = 4

    def build(current_value, depth):

        if not isinstance(current_value, dict):
            return format_exception_check(current_value, "double_quotes")

        current_intend = replacer * depth
        child_depth = depth + spaces_count
        child_intend = replacer * child_depth

        children = ["{"]
        last_key = list(current_value.keys())[-1]
        for key, value in current_value.items():
            comma = "," if key != last_key else ""
            if isinstance(value, dict):
                current_string = (
                    f'{child_intend}"{key}": {build(value, child_depth)}{comma}'
                )
            else:
                current_string = (
                    f'{child_intend}"{key}": {build(value, child_depth)}{comma}'
                )

            children.append(current_string)

        children.append(current_intend + "}")
        return "\n".join(children)

    return build(value, 0)


def create_path(parents, child):
    if parents == "":
        return child
    else:
        return f"{parents}.{child}"


def format_exception_check(value, format="without_quotes"):
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


def main():
    pass


if __name__ == "__main__":
    main()

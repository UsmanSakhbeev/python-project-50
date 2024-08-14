REPLACER = " "
SPACES_COUNT = 4


def format_to_json(value):
    def build(current_value, depth):
        if not isinstance(current_value, dict):
            return json_to_string(current_value)

        current_intend = REPLACER * depth
        child_depth = depth + SPACES_COUNT
        child_intend = REPLACER * child_depth

        children = [
            f'{child_intend}"{key}": {build(val, child_depth)}'
            for key, val in current_value.items()
        ]

        return "{\n" + ",\n".join(children) + f"\n{current_intend}}}"

    return build(value, 0)


def json_to_string(value, format="without_quotes"):
    if value is False:
        return "false"
    elif value is True:
        return "true"
    elif value is None:
        return "null"
    elif isinstance(value, int):
        return f"{str(value)}"
    else:
        return f'"{str(value)}"'

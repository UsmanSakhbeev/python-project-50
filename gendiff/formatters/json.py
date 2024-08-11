REPLACER = " "
SPACES_COUNT = 4


def format_to_json(value):
    def build(current_value, depth):

        if not isinstance(current_value, dict):
            return json_to_string(current_value)

        current_intend = REPLACER * depth
        child_depth = depth + SPACES_COUNT
        child_intend = REPLACER * child_depth

        children = ["{"]
        last_key = list(current_value.keys())[-1]
        for key, value in current_value.items():
            comma = "," if key != last_key else ""
            current_string = (
                f'{child_intend}"{key}": {build(value, child_depth)}{comma}'
            )
            children.append(current_string)

        children.append(current_intend + "}")
        return "\n".join(children)

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

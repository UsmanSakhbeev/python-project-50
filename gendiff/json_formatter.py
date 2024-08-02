from gendiff.parse_files import to_string


def format_to_json(value):
    replacer = " "
    spaces_count = 4

    def build(current_value, depth):

        if not isinstance(current_value, dict):
            return to_string(current_value, "double_quotes")

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

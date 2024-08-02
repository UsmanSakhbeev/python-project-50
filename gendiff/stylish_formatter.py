from gendiff.parse_files import to_string


def format_to_stylish(value):

    def build(current_value, depth, replacer=" "):
        if not isinstance(current_value, dict):
            return to_string(current_value)

        indent = replacer * depth
        child_depth = depth + 4
        result = ["{"]

        for key, val in current_value.items():
            string = ""
            if isinstance(val, dict):
                string = build_node(val.get("type"), indent, key, val, child_depth)
                result.extend(string)
            else:
                string = build_string(indent, key, val, child_depth)
                result.append(string)

        result.append(indent + "}")
        return "\n".join(result)

    def build_node(type, indent, key, val, depth):
        result = []
        match type:
            case "chained":
                string = f"{indent}    {key}: {build(val['value'], depth)}"
            case "added":
                string = f"{indent}  + {key}: {build(val['value'], depth)}"
            case "deleted":
                string = f"{indent}  - {key}: {build(val['value'], depth)}"
            case "unchanged":
                string = f"{indent}    {key}: {build(val['value'], depth)}"
            case "changed":
                string = f"{indent}  - {key}: {build(val['old_value'], depth)}"
                result.append(string)
                string = f"{indent}  + {key}: {build(val['new_value'], depth)}"
            case _:
                string = f"{indent}    {key}: {build(val, depth)}"
        result.append(string)
        return result

    def build_string(indent, key, value, child_depth):
        string = f"{indent}    {key}: {build(value, child_depth)}"
        return string

    return build(value, 0)

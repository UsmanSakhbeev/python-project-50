def stylish_formatter(value):
    replacer = " "

    def build(current_value, depth):
        if not isinstance(current_value, dict):
            return format_exception_check(current_value)

        current_intend = replacer * depth
        child_intend_size = depth + 4
        result = ["{"]

        for key, val in current_value.items():
            current_string = ""
            if isinstance(val, dict):
                if val.get("type") == "chained":
                    current_string = f"{current_intend}    {key}: {build(val['value'], child_intend_size)}"
                elif val.get("type") == "added":
                    current_string = f"{current_intend}  + {key}: {build(val['value'], child_intend_size)}"
                elif val.get("type") == "deleted":
                    current_string = f"{current_intend}  - {key}: {build(val['value'], child_intend_size)}"
                elif val.get("type") == "unchanged":
                    current_string = f"{current_intend}    {key}: {build(val['value'], child_intend_size)}"
                elif val.get("type") == "changed":
                    current_string = f"{current_intend}  - {key}: {build(val['old_value'], child_intend_size)}"
                    result.append(current_string)
                    current_string = f"{current_intend}  + {key}: {build(val['new_value'], child_intend_size)}"
                else:
                    current_string = f"{current_intend}    {key}: {build(val, child_intend_size)}"
                result.append(current_string)
            else:
                current_string = (f"{current_intend}    {key}: {build(val, child_intend_size)}")
                result.append(current_string)

        result.append(current_intend + "}")
        return "\n".join(result)
    return build(value, 0)


def plain_formatter(value):

    def build(current_value, current_path):
        result = []
        for key, val in current_value.items():
            current_string = ""
            if val.get("type") == "chained":
                current_string = build(val["value"], create_path(current_path, key))
            elif val.get("type") == "added":
                if isinstance(val['value'], dict):
                    current_string = f"Property '{create_path(current_path, key)}' was added with value: [complex value]"
                else:
                    current_string = f"Property '{create_path(current_path, key)}' was added with value: {format_exception_check(val['value'], 'single_quotes')}"
            elif val.get("type") == "changed":
                if isinstance(val['old_value'], dict):
                    current_string = f"Property '{create_path(current_path, key)}' was updated. From [complex value] to {format_exception_check(val['new_value'], 'single_quotes')}"
                else:
                    current_string = f"Property '{create_path(current_path, key)}' was updated. From {format_exception_check(val['old_value'], 'single_quotes')} to {format_exception_check(val['new_value'], 'single_quotes')}"
            elif val.get("type") == "deleted":
                current_string = f"Property '{create_path(current_path, key)}' was removed"
            else:
                continue
            result.append(current_string)
        return "\n".join(result)
    return build(value, "")


def json_formatter(value, replacer = " ", spaces_count = 4):
    def build(current_value, depth):

        if not isinstance(current_value, dict):
            return format_exception_check(current_value, "double_quotes") 
        
        current_intend = replacer * depth
        child_intend_size = depth + spaces_count
        child_intend = replacer * child_intend_size

        children = ["{"]
        last_key = list(current_value.keys())[-1]
        for key, value in current_value.items():
            if key != last_key:
                if isinstance(value, dict):
                    current_string = f'{child_intend}"{key}": {build(value, child_intend_size)},'
                else:                
                    current_string = f'{child_intend}"{key}": {build(value, child_intend_size)},'
            else:
                if isinstance(value, dict):
                    current_string = f'{child_intend}"{key}": {build(value, child_intend_size)}'
                else:                
                    current_string = f'{child_intend}"{key}": {build(value, child_intend_size)}'                
            children.append(current_string)
            
        children.append(current_intend + "}")
        return "\n".join(children)
    
    return build(value, 0)


def create_path(parents, child):
    if parents == "":
        return child
    else:
        return f"{parents}.{child}"


def format_exception_check(value, format = "without_quotes"):
    if value is False:
        return "false"
    elif value is True:
        return "true"
    elif value is None:
        return "null"
    elif format == "single_quotes":
        return f"'{str(value)}'"
    elif format == "double_quotes":
        return f'"{str(value)}"'
    elif format == "without_quotes":
        return f"{str(value)}"


def main():
    pass


if __name__ == '__main__':
    main()

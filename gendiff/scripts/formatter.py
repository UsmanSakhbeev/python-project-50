def json_formatter(value):
    replacer = " "

    def build(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)
        
        current_intend = replacer * depth
        child_intend_size = depth + 4
        child_intend = replacer * child_intend_size

        children = ["{"]

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
                    children.append(current_string)
                    current_string = f"{current_intend}  + {key}: {build(val['new_value'], child_intend_size)}"
                else:
                    current_string = f"{child_intend}    {key}: {build(val, child_intend_size)}"
                children.append(current_string)                              
            else:
                current_string = (f"{child_intend}    {key}: {build(val, child_intend_size)}")
                children.append(current_string)

        children.append(current_intend  + "}")
        return "\n".join(children)
    return build(value, 0)


def main():
    pass


if __name__ == '__main__':
    main()

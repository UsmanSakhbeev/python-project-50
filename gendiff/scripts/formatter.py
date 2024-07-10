def json_formatter(value):
    replacer = " "

    def build(current_value, depth):
        if not isinstance(current_value, dict):
            if current_value == False:
                return "false"
            elif current_value == True:
                return "true"
            elif current_value == None:
                return "null"
            else:
                return str(current_value)
        
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

        result.append(current_intend  + "}")
        return "\n".join(result)
    return build(value, 0)

def plain_formatter(value):
    
    def build(current_value, current_path):   
        if not isinstance(current_value, dict):
            return str(current_value)
        children = []
        for key, val in current_value.items():            
            if isinstance(val, dict):
                if val.get("type") == "chained":
                    build(val, current_path+f".{key}")
                elif val.get("type") == "added":
                    current_string = f"Property {current_path} was added with value: {build(val, current_path+f'.{key}')}"
                    children.append(current_string)                              
            else:
                current_string = (f"asdfd")
                children.append(current_string)
        return "\n".join(children)
    return build(value, "")

    

def main():
    pass


if __name__ == '__main__':
    main()

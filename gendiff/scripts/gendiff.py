import argparse
from gendiff.scripts.parse_files import get_text


def main():
    parser = argparse.ArgumentParser(
        description="Compares and shows a difference.")
    parser.add_argument("first_file", type=str, help="First conf file")
    parser.add_argument("second_file", type=str, help="Second conf file")
    parser.add_argument(
        "-f", "--format", type=str, help="set format of output")

    args = parser.parse_args()
    file1, file2 = get_text(args.first_file, args.second_file)
    diff =  new_diff(file1, file2)
    return formatter(diff)



def new_diff(first_file, second_file):
    def build(node1, node2):        
        sorted_keys = sorted(node1.keys() | node2.keys())
        diff = {}
        for key in sorted_keys:
            if key not in node1:
                diff[key] = {"type": "added", "value": node2[key]}
            elif key not in node2:
                diff[key] = {"type": "deleted", "value": node1[key]}
            elif isinstance(node1[key], dict) and isinstance(node2[key], dict):
                diff[key] = {"type": "chained", "value": build(node1[key], node2[key])}
            elif key in node1 and key in node2:
                if node1[key] != node2[key]:
                    diff[key] = {"type": "changed", "old_value": node1[key], "new_value": node2[key]}
                else:
                    diff[key] = {"type": "unchanged", "value": node1[key]}

        return diff
        
          
    
    return build(first_file, second_file)


def generate_diff(file1, file2, path=""):
    output = ["{"]
    sorted_keys = sorted(file1.keys() | file2.keys())
    for key in sorted_keys:
        if key not in file1:
            output.append(f"  + {key}: {file2[key]}")
        elif key not in file2:
            output.append(f"  - {key}: {file1[key]}")
        elif key in file1 and key in file2:
            if file1[key] == file2[key]:
                output.append(f"    {key}: {file1[key]}")
            else:
                output.append(f"  - {key}: {file1[key]}")
                output.append(f"  + {key}: {file2[key]}")
    output.append('}')
    return "\n".join(output).lower().strip()


def formatter(value, replacer = " ", spaces_count = 1):
    def build(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)
        
        current_intend = replacer * depth
        child_intend_size = depth + spaces_count
        child_intend = replacer * child_intend_size

        children = ["{"]
        for key, val in current_value.items():
            if val["type"] == "added":
                current_string = f"  + {child_intend}{key}: {build(val['value'], child_intend_size)}"
                children.append(current_string)
            elif val["type"] == "removed":
                current_string = f"  - {child_intend}{key}: {build(val['value'], child_intend_size)}"
                children.append(current_string)
            elif val["type"] == "changed":
                current_string = f"  - {child_intend}{key}: {build(val['old_value'], child_intend_size)}"
                children.append(current_string)
                current_string = f"  = {child_intend}{key}: {build(val['new_value'], child_intend_size)}"
                children.append(current_string)
            elif val["type"] == "nested":
                current_string = f"    {child_intend}{key}: {build(val['value'], child_intend_size)}"
                children.append(current_string)                
            children.append(current_intend + "}")
        return "\n".join(children)
    
    return build(value, 0)

if __name__ == "__main__":
    main()

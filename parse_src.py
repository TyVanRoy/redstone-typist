import os
from constants import *


def find_tags(file_path, tags):
    with open(file_path, "r") as file:
        content = file.read()
        for tag in tags:
            if tag in content:
                return tag
    return None


def parse_src(src_path, tags=[NEW_TAG, EDIT_TAG]):
    target_file = None
    target_tag = None

    for root, _, files in os.walk(src_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            found_tag = find_tags(file_path, tags)
            if found_tag:
                if target_file:
                    raise ValueError(
                        "Only one tag is allowed in the entire project source.")
                target_file = file_path
                target_tag = found_tag

    if not target_file:
        raise ValueError("No tag found in the project source.")

    return target_file, target_tag


if __name__ == "__main__":
    # Test the parse_src function
    test_src_path = "./test_project_source"
    print(parse_src(test_src_path))

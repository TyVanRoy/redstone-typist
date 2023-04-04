import os
import shutil
import re
from datetime import datetime
from constants import NEW_TAG, EDIT_TAG, END_TAG


def create_backup(file_path):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file_name = f"{os.path.basename(file_path)}_{timestamp}.bak"
    backup_path = os.path.join("./backups", backup_file_name)
    shutil.copy2(file_path, backup_path)
    return backup_path


def insert_response(file_path, tag, response):
    create_backup(file_path)

    with open(file_path, "r") as file:
        content = file.read()

    if tag == NEW_TAG:
        content = content.replace(tag, response, 1)
    elif tag == EDIT_TAG:
        edit_end_pattern = re.compile(
            rf'{re.escape(EDIT_TAG)}.*?{re.escape(END_TAG)}', re.DOTALL)
        content = edit_end_pattern.sub(response, content, count=1)

    with open(file_path, "w") as file:
        file.write(content)


if __name__ == "__main__":
    # Test the insert_response function
    test_file_path = "./test_project_source/test_file.py"
    test_tag = EDIT_TAG
    test_response = "def hello():\n    print('Hello, world!')"
    insert_response(test_file_path, test_tag, test_response)

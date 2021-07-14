import json
import os

def write_to_file(**kwargs):
    """Append to a file"""

    file_name = os.environ['DATA_FILE_NAME']


    with open(file_name, "a") as file:
        file.write(json.dumps(kwargs, indent=4))
        file.write("\n")

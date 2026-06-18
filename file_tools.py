import os

def create_file(filepath, content=""):

    try:

        with open(filepath, "w") as f:
            f.write(content)

        return f"Created {filepath}"

    except Exception as e:

        return f"Error: {e}"
def create_folder(path):

    try:

        os.makedirs(
            path,
            exist_ok=True
        )

        return f"Created folder {path}"

    except Exception as e:

        return f"Error: {e}"
def append_file(filepath, text):

    try:

        with open(filepath, "a") as f:
            f.write(text)

        return f"Updated {filepath}"

    except Exception as e:

        return f"Error: {e}"
def replace_in_file(filepath, old_text, new_text):

    try:

        with open(filepath, "r") as f:
            content = f.read()

        content = content.replace(
            old_text,
            new_text
        )

        with open(filepath, "w") as f:
            f.write(content)

        return f"Modified {filepath}"

    except Exception as e:

        return f"Error: {e}"

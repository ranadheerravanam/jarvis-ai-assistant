from langchain.tools import tool
import subprocess
import os


@tool
def open_chrome():
    """
    Open Google Chrome browser.
    """

    subprocess.Popen(["google-chrome"])

    return "Chrome opened successfully"


@tool
def open_vscode():
    """
    Open Visual Studio Code editor.
    """

    subprocess.Popen(["code"])

    return "VS Code opened successfully"


@tool
def open_terminal():
    """
    Open the Linux terminal application.

    Use when the user wants:
    - terminal
    - shell
    - console
    - command prompt
    """

    subprocess.Popen(["gnome-terminal"])

    return "Terminal opened"


@tool
def open_files():
    """
    Open the graphical file manager.

    Use when the user wants:
    - file manager
    - file explorer
    - browse folders
    - open downloads
    """

    subprocess.Popen(["nautilus"])

    return "File manager opened"


@tool
def open_calculator():
    """
    Open calculator application.
    """

    subprocess.Popen(["gnome-calculator"])

    return "Calculator opened"


@tool
def find_python_files():
    """
    Find Python files in the current project directory.
    """

    import os

    project_dir = os.getcwd()

    matches = []

    for root, dirs, files in os.walk(project_dir):

        # Ignore virtual environments
        dirs[:] = [
            d for d in dirs
            if d not in ["venv", "myenv", "__pycache__", ".git"]
        ]

        for file in files:

            if file.endswith(".py"):

                matches.append(
                    os.path.join(root, file)
                )

    return "\n".join(matches)

@tool
def find_file(filename: str):
    """
    Search for a specific file by filename.

    Examples:
    - Find tool_agent.py
    - Locate README.md
    - Search for settings.py

    Returns the full path.
    """

    matches = []

    for root, dirs, files in os.walk(os.path.expanduser("~")):

        if filename in files:

            matches.append(
                os.path.join(root, filename)
            )

    if not matches:
        return "File not found"

    return "\n".join(matches[:20])


@tool
def read_file(filepath: str):
    """
    Read the contents of a text file.

    Use when the user wants:
    - read a file
    - inspect a file
    - analyze a file
    - explain a file
    """

    try:

        with open(filepath, "r", encoding="utf-8") as f:

            return f.read()[:5000]

    except Exception as e:

        return f"Error reading file: {e}"
@tool
def explain_file(filepath: str):
    """
    Read a file and return its contents for explanation.
    """

    try:

        with open(filepath, "r", encoding="utf-8") as f:

            return f.read()[:5000]

    except Exception as e:

        return f"Error: {e}"
@tool
def explain_file(filepath: str):
    """
    Read a Python file and explain it.
    """

    try:

        with open(filepath, "r", encoding="utf-8") as f:

            return f.read()[:5000]

    except Exception as e:

        return f"Error: {e}"

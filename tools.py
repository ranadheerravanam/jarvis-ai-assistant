from langchain.tools import tool
import os
import subprocess

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
    Open terminal application.
    """

    subprocess.Popen(["gnome-terminal"])

    return "Terminal opened"


@tool
def open_files():
    """
    Open file manager.
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
    Find all Python files in the user's home directory.
    """

    matches = []

    for root, dirs, files in os.walk(os.path.expanduser("~")):

        for file in files:

            if file.endswith(".py"):

                matches.append(
                    os.path.join(root, file)
                )

        if len(matches) >= 20:
            break

    return "\n".join(matches[:20])

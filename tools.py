from langchain.tools import tool
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

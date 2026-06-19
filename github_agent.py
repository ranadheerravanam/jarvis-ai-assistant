import subprocess


def git_status():

    result = subprocess.run(
        ["git", "status"],
        capture_output=True,
        text=True
    )

    return result.stdout


def git_add():

    subprocess.run(
        ["git", "add", "."]
    )

    return "Files staged."


def git_commit(message):

    result = subprocess.run(
        ["git", "commit", "-m", message],
        capture_output=True,
        text=True
    )

    return result.stdout

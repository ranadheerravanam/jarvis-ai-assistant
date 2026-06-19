import subprocess


def run_project(path):

    result = subprocess.run(
        ["python", path],
        capture_output=True,
        text=True
    )

    return {
        "stdout": result.stdout,
        "stderr": result.stderr,
        "returncode": result.returncode
    }

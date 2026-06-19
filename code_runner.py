import subprocess

def run_python(filepath):

    try:

        result = subprocess.run(
            ["python", filepath],
            capture_output=True,
            text=True,
            timeout=30
        )

        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        }

    except Exception as e:

        return {
            "stdout": "",
            "stderr": str(e),
            "returncode": 1
        }

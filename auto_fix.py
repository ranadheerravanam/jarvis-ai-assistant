from code_runner import run_python
from self_healer import fix_code


def auto_fix(filepath):

    with open(filepath, "r") as f:
        code = f.read()

    result = run_python(filepath)

    if result["returncode"] == 0:

        print("Code runs successfully.")
        return

    print("\nERROR FOUND:\n")
    print(result["stderr"])

    fixed = fix_code(
        code,
        result["stderr"]
    )

    with open(filepath, "w") as f:
        f.write(fixed)

    print("\nCode fixed.")

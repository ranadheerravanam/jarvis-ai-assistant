from code_runner import run_python
from self_healer import fix_code


def auto_fix(filepath, max_attempts=5):

    for attempt in range(max_attempts):

        print(f"\nAttempt {attempt + 1}")

        result = run_python(filepath)

        if result["returncode"] == 0:

            print("\nSUCCESS")
            print(result["stdout"])

            return True

        print("\nERROR:")
        print(result["stderr"])

        with open(filepath, "r") as f:
            code = f.read()

        fixed = fix_code(
            code,
            result["stderr"]
        )

        with open(filepath, "w") as f:
            f.write(fixed)

    print("\nFAILED")

    return False

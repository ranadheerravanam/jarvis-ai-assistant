from project_runner import run_project
from auto_fix_v2 import auto_fix

project_path = input("Project Entry File: ")

max_attempts = 3

for attempt in range(max_attempts):

    print(f"\nAttempt {attempt + 1}")

    result = run_project(project_path)

   if result["returncode"] == 0 and \
       "No module named" not in result["stdout"] and \
       "not properly configured" not in result["stdout"]:
        print(result["stdout"])

        break

    print("\nERROR FOUND")

    print(result["stderr"])

    auto_fix(project_path)

else:

    print("\nFailed after 3 attempts.")

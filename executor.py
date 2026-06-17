from tools import (
    find_python_files,
    read_file
)


def execute_step(step):

    step = step.lower()

    if "find python files" in step or "find_python_files" in step:

        print("\n[TOOL] find_python_files")

        return find_python_files.invoke({})

    if "read" in step:

        return "Read operation planned"

    return f"Executed: {step}"

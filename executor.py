from tools import (
    find_python_files,
    find_file,
    read_file,
    web_search
)


def execute_step(step):

    step_lower = step.lower()

    # FIND PYTHON FILES

    if "find_python_files" in step_lower or \
       "find python files" in step_lower:

        print("\n[TOOL] find_python_files")

        return find_python_files.invoke({})

    # FIND FILE

    if "find_file" in step_lower:

        print("\n[TOOL] find_file")

        return "Filename required"

    # READ FILE

    if "read_file" in step_lower:

        print("\n[TOOL] read_file")

        files = find_python_files.invoke({})

        first_file = files.split("\n")[0]

        return read_file.invoke(
            {"filepath": first_file}
        )
    # WEB SEARCH

    if "web_search" in step_lower or \
       "search documentation" in step_lower or \
       "look up" in step_lower:

        print("\n[TOOL] web_search")

        return web_search.invoke(
            {"query": "python project analysis"}
        )

    return f"Executed: {step}"

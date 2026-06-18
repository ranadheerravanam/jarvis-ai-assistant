from file_tools import (
    create_folder,
    create_file
)

project = input("Project Name: ")

create_folder(project)

create_file(
    f"{project}/README.md",
    f"# {project}"
)

create_file(
    f"{project}/main.py",
    'print("Hello World")'
)

print("Project created.")

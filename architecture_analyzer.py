from tools import find_python_files, read_file

files = find_python_files.invoke({}).split("\n")

imports = {}

for f in files:

    try:
        content = read_file.invoke(
            {"filepath": f}
        )

        lines = content.split("\n")

        imports[f] = []

        for line in lines:

            line = line.strip()

            if line.startswith("import ") \
               or line.startswith("from "):

                imports[f].append(line)

    except:
        pass

print("\nPROJECT DEPENDENCIES\n")

for file, deps in imports.items():

    print("\nFILE:", file)

    for d in deps:

        print("  ", d)

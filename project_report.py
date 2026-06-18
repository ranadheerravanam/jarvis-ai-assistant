from tools import find_python_files, read_file

files = find_python_files.invoke({}).split("\n")

print("\nPROJECT REPORT\n")

print(f"Total Python Files: {len(files)}\n")

for f in files[:5]:

    print("=" * 60)
    print("FILE:", f)
    print("=" * 60)

    try:
        content = read_file.invoke(
            {"filepath": f}
        )

        print(content[:500])

    except Exception as e:
        print("Error:", e)

import subprocess

result = subprocess.run(
    ["git", "push"],
    capture_output=True,
    text=True
)

print(result.stdout)
print(result.stderr)

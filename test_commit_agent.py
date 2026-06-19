from commit_agent import generate_commit

changes = """
Added project runner
Added autonomous builder
Fixed manage.py
"""

print(
    generate_commit(changes)
)

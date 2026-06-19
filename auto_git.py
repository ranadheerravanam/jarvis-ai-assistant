from github_agent import (
    git_status,
    git_add,
    git_commit
)

from commit_agent import (
    generate_commit
)

status = git_status()

print("\nGIT STATUS\n")
print(status)

git_add()

message = generate_commit(status)

print("\nCOMMIT MESSAGE:")
print(message)

print(
    git_commit(message)
)

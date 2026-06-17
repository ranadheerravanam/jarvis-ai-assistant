from planner import make_plan
from executor import execute_step


task = input("Task: ")

plan = make_plan(task)

print("\nPLAN:\n")
print(plan)

print("\nEXECUTION:\n")

for line in plan.split("\n"):

    line = line.strip()

    if not line:
        continue

    result = execute_step(line)

    print(result)

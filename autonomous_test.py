from planner import make_plan
from executor import execute_step

task = input("Task: ")

plan = make_plan(task)

print("\nPLAN:\n")
print(plan)

print("\nEXECUTION:\n")

steps = [
    s.strip()
    for s in plan.splitlines()
    if s.strip()
]

for step in steps:
    step = step.strip()

    if not step:
        continue

    print(f"\nExecuting: {step}")

    result = execute_step(step)

    print(result)

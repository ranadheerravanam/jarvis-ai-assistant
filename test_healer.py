from self_healer import fix_code

broken = """
print("Hello"
"""

error = """
SyntaxError: '(' was never closed
"""

fixed = fix_code(
    broken,
    error
)

print(fixed)

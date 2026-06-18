from code_rag.code_engine import ask_code

def execute_step(step):

    print(f"\nExecuting: {step}")

    result = ask_code(step)

    return result

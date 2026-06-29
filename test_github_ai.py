from github_ai_agent import github_ai

while True:

    query = input("Repository: ")

    if query == "exit":
        break

    print(github_ai(query))

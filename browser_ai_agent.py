from selenium_agent import (
    github_open_first_result,
    google_search,
    youtube_search,
    get_title,
    get_page_text
)
from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2")


def browser_ai(command):

    command = command.lower().strip()

    print("Step 1 : Processing command")

    if command.startswith("github"):

        query = command.replace("github", "").strip()

        print("Searching GitHub...")

        github_open_first_result(query)

    elif command.startswith("google"):

        query = command.replace("google", "").strip()

        print("Searching Google...")

        google_search(query)

    elif command.startswith("youtube"):

        query = command.replace("youtube", "").strip()

        print("Searching YouTube...")

        youtube_search(query)

    else:

        return "Unknown command"

    input("\nAfter the page loads press ENTER...")

    print("Reading page title...")

    title = get_title()

    print("Title:", title)

    print("Reading page...")

    page = get_page_text()

    print("Page read successfully")

    prompt = f"""
You are an AI assistant.

Summarize this webpage.

Title:
{title}

Content:
{page[:3000]}
"""

    print("Thinking...")

    answer = llm.invoke(prompt)

    return answer.content

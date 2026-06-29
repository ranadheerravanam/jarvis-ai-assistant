from langchain_ollama import ChatOllama

from tools import *

from rag.rag_engine import ask_rag
from code_rag.code_engine import ask_code

from browser.browser_tools import (
    youtube_search,
    google_search,
    github_search,
    ott_search
)

from core.router import normalize


llm = ChatOllama(model="llama3.2")


def process(command):

    command = normalize(command)

    # ===============================
    # DESKTOP APPS
    # ===============================

    if command == "open vscode":
        return open_vscode.invoke({})

    if command == "open chrome":
        return open_chrome.invoke({})

    if command == "open terminal":
        return open_terminal.invoke({})

    if command == "open calculator":
        return open_calculator.invoke({})

    if command == "open files":
        return open_files.invoke({})

    if command == "open youtube":
        return open_youtube.invoke({})

    # ===============================
    # GOOGLE
    # ===============================

    if command.startswith("google "):

        query = command.replace(
            "google",
            "",
            1
        ).strip()

        return google_search(query)

    # ===============================
    # GITHUB
    # ===============================

    if command.startswith("github "):

        query = command.replace(
            "github",
            "",
            1
        ).strip()

        return github_search(query)

    # ===============================
    # YOUTUBE SEARCH
    # ===============================

    if command.startswith("youtube "):

        query = command.replace(
            "youtube",
            "",
            1
        ).strip()

        return youtube_search(query)

    # ===============================
    # OTT
    # ===============================

    if command == "open netflix":
        return ott_search("netflix", "")

    if command == "open prime":
        return ott_search("prime", "")

    if command == "open hotstar":
        return ott_search("hotstar", "")

    if command.startswith("netflix "):

        query = command.replace(
            "netflix",
            "",
            1
        ).strip()

        return ott_search(
            "netflix",
            query
        )

    if command.startswith("prime "):

        query = command.replace(
            "prime",
            "",
            1
        ).strip()

        return ott_search(
            "prime",
            query
        )

    if command.startswith("hotstar "):

        query = command.replace(
            "hotstar",
            "",
            1
        ).strip()

        return ott_search(
            "hotstar",
            query
        )

    # ===============================
    # PDF RAG
    # ===============================

    if command.startswith("ask pdf"):

        question = command.replace(
            "ask pdf",
            "",
            1
        ).strip()

        return ask_rag(question)

    # ===============================
    # CODE RAG
    # ===============================

    if command.startswith("ask code"):

        question = command.replace(
            "ask code",
            "",
            1
        ).strip()

        return ask_code(question)

    # ===============================
    # WEB SEARCH TOOL
    # ===============================

    if command.startswith("search "):

        query = command.replace(
            "search",
            "",
            1
        ).strip()

        return web_search.invoke(
            {"query": query}
        )

    # ===============================
    # NORMAL CHAT
    # ===============================

    return llm.invoke(command).content

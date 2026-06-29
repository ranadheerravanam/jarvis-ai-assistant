from selenium_browser_agent import browser_agent

while True:

    cmd = input("Command: ")

    if cmd == "exit":
        break

    print(browser_agent(cmd))

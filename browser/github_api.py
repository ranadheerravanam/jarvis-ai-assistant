import requests


def github_search(query):

    url = "https://api.github.com/search/repositories"

    params = {
        "q":f"{query} in:name",
        "sort": "stars",
        "order": "desc",
        "per_page": 1
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return None

    data = response.json()

    if data["total_count"] == 0:
        return None

    repo = data["items"][0]

    return {
        "name": repo["full_name"],
        "url": repo["html_url"],
        "description": repo["description"],
        "stars": repo["stargazers_count"]
    }

import subprocess
import urllib.parse
def ott_search(platform, query):

    q = urllib.parse.quote(query)

    urls = {
        "netflix": f"https://www.netflix.com/search?q={q}",
        "prime": f"https://www.primevideo.com/search/ref=atv_nb_sr?phrase={q}",
        "hotstar": f"https://www.hotstar.com/in/search?q={q}",
        "zee5": f"https://www.zee5.com/search?q={q}",
        "sony": f"https://www.sonyliv.com/search/{q}"
    }

    if platform not in urls:
        return f"Unsupported OTT platform: {platform}"

    subprocess.Popen([
        "google-chrome",
        "--profile-directory=Default",
        urls[platform]
    ])

    return f"Searching {platform} for {query}"
def youtube_search(query):

    q = urllib.parse.quote(query)

    subprocess.Popen([
        "google-chrome",
        "--profile-directory=Default",
        f"https://www.youtube.com/results?search_query={q}"
    ])

    return f"Searching YouTube for {query}"


def google_search(query):

    q = urllib.parse.quote(query)

    subprocess.Popen([
        "google-chrome",
        "--profile-directory=Default",
        f"https://www.google.com/search?q={q}"
    ])

    return f"Searching Google for {query}"


def github_search(query):

    q = urllib.parse.quote(query)

    subprocess.Popen([
        "google-chrome",
        "--profile-directory=Default",
        f"https://github.com/search?q={q}"
    ])

    return f"Searching GitHub for {query}"

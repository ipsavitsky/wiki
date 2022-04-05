import requests

class NoArticleFound(Exception):
    pass

def fetch_wiki_data(keyword: str) -> str:
    url = "https://ru.wikipedia.org/w/api.php"
    params = {
        "action": "parse",
        "page": keyword,
        "format": "json",
        "prop": "text",
        "redirects": "",
    }
    data = requests.get(url, params=params).json()
    # print(data)
    if "error" in data:
        raise NoArticleFound(data["error"]["info"])
    return data["parse"]


if __name__ == "__main__":
    fetch_wiki_data("python")

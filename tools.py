import requests
from bs4 import BeautifulSoup


def search_web(query: str) -> str:
    """
    Fetches basic web search information.
    """

    url = "https://www.google.com/search"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(
        url,
        params={"q": query},
        headers=headers,
        timeout=10
    )

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    results = []

    for result in soup.select("div"):
        text = result.get_text(
            " ",
            strip=True
        )

        if len(text) > 100:
            results.append(text[:500])

        if len(results) >= 5:
            break

    return "\n\n".join(results)

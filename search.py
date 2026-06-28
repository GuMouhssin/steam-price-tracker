from fetch import fetch

def search_game(name):
    url = (
        f"https://store.steampowered.com/api/storesearch/"
        f"?term={name}&l=english&cc=US"
    )
    resp = fetch(url)
    if not resp:
        return []
    data = resp.json()
    return data.get("items", [])


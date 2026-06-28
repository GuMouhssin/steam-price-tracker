from fetch import fetch
from db import get_all_games, update_game, add_action
from alerts import send_alert
def fetch_by_id(id):
    url = (f"https://store.steampowered.com/api/appdetails?appids={id}")
    resp = fetch(url)
    if not resp:
        return None
    data = resp.json()
    data = data[f"{id}"]
    if not data["success"] :
        return None
    data = data["data"]
    return {
        "id": id,
        "name": data["name"],
        "init_price": int(data["price_overview"]["initial"]) if not data["is_free"] else 0,
        "fin_price": int(data["price_overview"]["final"]) if not data["is_free"] else 0,
        "final_formatted": data["price_overview"]["final_formatted"] if not data["is_free"] else "N/A",
        "discount": (int(data["price_overview"]["discount_percent"]))/100 if not data["is_free"] else -1,
        "currency":data["price_overview"]["currency"] if not data["is_free"] else "usd"
    }

def compare_games(old, new):
    if old[3] == new["fin_price"]:
        return 0
    elif old[3] > new["fin_price"]:
        return 1
    else:
        return -1

def track_prices():
    games = get_all_games()
    for game in games:
        game_now = fetch_by_id(game[0])
        status = compare_games(game, game_now)
        send_alert(game[1], game[3], game_now["fin_price"], status)
        if status == 0:
            continue
        elif status == 1:
            print(f"the price of {game[1]} has droped from {game[6]} to {game_now['final_formatted']}")
            add_action(game, game_now)
            update_game(game_now)
        else:
            print(f"the price of {game[1]} has raised from {game[6]} to {game_now['final_formatted']}")
            add_action(game, game_now)
            update_game(game_now)


def parse_game(game):
    init_price = game.get("price", {}).get("initial", -1)
    fin_price = game.get("price", {}).get("final", -1)
    if init_price > 0:
        discount = (init_price - fin_price) / init_price
    else:
        discount = -1
    return {
        "id": game.get("id", "N/A"),
        "name": game.get("name", "N/A"),
        "init_price": init_price,
        "fin_price": fin_price,
        "discount": discount,
        "currency": game.get("price", {}).get("currency", "N/A")
    }
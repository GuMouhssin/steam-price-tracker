import os, sqlite3
from search import search_game
from tracker import track_prices, fetch_by_id
from parser import parse_game
from db import init_db, add_game, get_all_games, remove_game, add_action, update_game, get_game_history

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def choose_game():
    clear_screen()
    name = input("Enter game name: ").strip()
    results = search_game(name)
    if not results:
        input("No results found. Press Enter to continue...")
        return None
    while True:
        clear_screen()
        print("=" * 50)
        print(f"{len(results)} results found")
        print("=" * 50)
        for i, game in enumerate(results, start=1):
            print(f"{i} - {game['name']}")
        try:
            choice = int(input("\nChoose a game: "))
            if 1 <= choice <= len(results):
                return results[choice - 1]
            input("Invalid choice. Press Enter...")
        except ValueError:
            input("Please enter a valid number. Press Enter...")
    
def check_prices():
    clear_screen()
    print("------DETECTED CHANGES------")
    track_prices()
    input("press enter to continue")

def m_add_game():
    game = choose_game()
    if not game:
        return
    parsed = parse_game(game)
    game = fetch_by_id(game["id"])
    while True:
        clear_screen()
        confirm = input("track this game ? (Y/N): ")
        if confirm.lower() == "y":
            try:
                add_game(game)
                break
            except sqlite3.IntegrityError:
                input("the game already exist, press enter to continue...")
                break
        elif confirm.lower() == "n":
            break
        else:
            input("please enter a valid choice (Y/N)")

def show_games():
    clear_screen()
    games = get_all_games()
    if not games or len(games) == 0:
        print("there is no tracked games")
    else:
        print("------TRACKED GAMES------")
        for i, game in enumerate(games, start = 1):
            print(f"{i}. {game[1]} - {game[6]}")
    input("press enter to return...")

def del_game():
    clear_screen()
    games = get_all_games()
    if not games or len(games) == 0:
        print("there is no tracked games")
        input("press enter to return...")
    else:
        print("------TRACKED GAMES------")
        for i, game in enumerate(games, start = 1):
            print(f"{i}. {game[1]} - {game[6]}")
        while True:
            try:
                i = int(input("choose a game to remove (by it's index): "))
                if 0 < i <= len(games):
                    game_id = games[i-1][0]
                    remove_game(game_id)
                    break
                else: 
                    input("invalid choice, press enter...")
            except ValueError:
                input("please enter a valid number, press enter...")

def show_game_history():
    clear_screen()
    games = get_all_games()
    if not games or len(games) == 0:
        print("there is no tracked games")
        input("press enter to return...")
    else:
        print("------TRACKED GAMES------")
        for i, game in enumerate(games, start = 1):
            print(f"{i}. {game[1]} - {game[6]}")
        while True:
            try:
                i = int(input("choose a game (by it's index): "))
                if 0 < i <= len(games):
                    game_id = games[i-1][0]
                    history = get_game_history(game_id)
                    clear_screen()
                    if not history or len(history) == 0:
                        print("there is no history for this game")
                        input("press enter to continue")
                    else:
                        print(f"------{games[i-1][1].upper()} HISTORY------")
                        print("============================================")
                        print("Old price   |New price   | changed at   ")
                        for action in history:
                            print("----------------------------------")
                            print(f"{action[1]} {action[4]}   |{action[2]} {action[4]}   |{action[5]}")
                            print("----------------------------------")
                        input("press enter to continue")
                    break
                else: 
                    input("invalid choice, press enter...")
            except ValueError:
                input("please enter a valid number, press enter...")

def menu():
    while True:
        clear_screen()
        print("=" * 50)
        print("        STEAM STORE TRACKER")
        print("=" * 50)
        print("1. Search and track a new game")
        print("2. Show tracked games")
        print("3. Remove a tracked game")
        print("4. Check prices now")
        print("5. View price change history")
        print("0. Exit")
        print("=" * 50)

        choice = input("Choose: ").strip()

        if choice == "1":
            m_add_game()

        elif choice == "2":
            show_games()

        elif choice == "3":
            del_game()

        elif choice == "4":
            check_prices()


        elif choice == "5":
            show_game_history()

        elif choice == "0":
            print("Goodbye.")
            break

        else:
            input("Invalid choice. Press Enter...")
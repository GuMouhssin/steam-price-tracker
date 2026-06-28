import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("games.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY,
            name TEXT,
            init_price INTEGER,
            fin_price INTEGER,
            discount REAL,
            currency TEXT,
            final_formatted TEXT
        )
    ''')
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS price_history (
            game_id INTEGER,
            old_price INTEGER,
            new_price INTEGER,
            discount INTEGER,
            currency TEXT,
            changed_at TEXT,
            PRIMARY KEY (game_id, changed_at),
            FOREIGN KEY (game_id) REFERENCES games(id)
        )
    """)
    conn.commit()
    conn.close()

def add_game(game):
    conn = sqlite3.connect("games.db")
    cursor = conn.cursor()
    cursor.execute(f'''
        INSERT INTO games (id, name, init_price, fin_price, discount, currency, final_formatted)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''',(
            game["id"],
            game["name"],
            game["init_price"],
            game["fin_price"],
            game["discount"],
            game["currency"],
            game["final_formatted"]
        )
    )
    conn.commit()
    conn.close()

def get_all_games():
    conn = sqlite3.connect("games.db")
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM games
    ''')
    games = cursor.fetchall()
    conn.close()
    return games

def remove_game(game_id):
    conn = sqlite3.connect("games.db")
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM games WHERE id = ?
    ''', (game_id,)
    )
    conn.commit()
    conn.close()

def update_game(game):
    conn = sqlite3.connect("games.db")
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE games
        SET 
            init_price = ?,
            fin_price = ?,
            discount = ?,
            final_formatted = ?
        WHERE id = ?
    ''', (game["init_price"], game["fin_price"], game["discount"], game["final_formatted"], game['id']))
    conn.commit()
    conn.close()

def add_action(old, new):
    conn = sqlite3.connect("games.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO price_history (game_id, old_price, new_price, discount, currency, changed_at)
        VALUES (?, ?, ?, ?, ?, ?)
    ''',(
        old[0],
        old[3],
        new["fin_price"],
        new["discount"],
        new["currency"],
        datetime.now().isoformat()
    )
    )
    conn.commit()
    conn.close()

def get_game_history(game_id):
    conn = sqlite3.connect("games.db")
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM price_history
        WHERE game_id = ?
        ORDER BY changed_at ASC
    ''', (game_id,))
    history = cursor.fetchall()
    conn.close()
    return history

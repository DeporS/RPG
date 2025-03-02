import sqlite3
import time


def connect():
    return sqlite3.connect("my-rpg.db")


def create_tables():
    conn = connect()
    cursor = conn.cursor()

    # Player table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS players (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nickname TEXT,
                   lvl INTEGER,
                   xp INTEGER,
                   gold INTEGER
                   )               
    """)

    conn.commit()
    conn.close()


def save_player(nickname, lvl, xp, gold):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT into players (nickname, lvl, xp, gold) VALUES (?, ?, ?, ?)", (nickname, lvl, xp, gold))
    conn.commit()
    conn.close()


def update_player(player_id, nickname=None, lvl=None, xp=None, gold=None):
    conn = None
    while conn is None:
        try:
            conn = connect()  # try to connect
        except sqlite3.OperationalError:
            print("Database is locked, retrying...")
            time.sleep(2)  # wait 2 sec and try again

    cursor = conn.cursor()
    try:
        if nickname:
            cursor.execute(
                "UPDATE players SET nickname = ? WHERE id = ?", (nickname, player_id))
        if lvl is not None:
            cursor.execute(
                "UPDATE players SET lvl = ? WHERE id = ?", (lvl, player_id))
        if xp is not None:
            cursor.execute("UPDATE players SET xp = ? WHERE id = ?",
                           (xp, player_id))
        if gold is not None:
            cursor.execute(
                "UPDATE players SET gold = ? WHERE id = ?", (gold, player_id))

        conn.commit()
    except sqlite3.Error as e:
        print("Error while updating player:", e)
    finally:
        conn.close()


def load_player():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM players LIMIT 1")
    player = cursor.fetchone()
    conn.close()
    return player

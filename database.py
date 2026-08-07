import sqlite3

DB_NAME = "users.db"


def connect():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER UNIQUE,
        username TEXT,
        first_name TEXT,
        join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        plan TEXT DEFAULT 'ندارد',
        expire_date TEXT DEFAULT NULL,
        volume TEXT DEFAULT '0GB',
        config TEXT DEFAULT NULL
    )
    """)

    conn.commit()
    conn.close()


def add_user(telegram_id, username, first_name):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT OR IGNORE INTO users
    (telegram_id, username, first_name)
    VALUES (?, ?, ?)
    """,
    (telegram_id, username, first_name))

    conn.commit()
    conn.close()


def get_user(telegram_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE telegram_id=?",
        (telegram_id,)
    )

    user = cursor.fetchone()

    conn.close()

    return user

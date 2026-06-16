import sqlite3

conn = sqlite3.connect("memory.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS memories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fact TEXT
)
""")

conn.commit()


def save_memory(text):

    cursor.execute(
        "INSERT INTO memories (fact) VALUES (?)",
        (text,)
    )

    conn.commit()

    return "Memory saved."


def get_memories():

    cursor.execute(
        "SELECT fact FROM memories"
    )

    return [
        row[0]
        for row in cursor.fetchall()
    ]

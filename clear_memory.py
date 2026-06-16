import sqlite3

conn = sqlite3.connect("memory.db")

cursor = conn.cursor()

cursor.execute("DELETE FROM memories")

conn.commit()

print("Memory cleared.")

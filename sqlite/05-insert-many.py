import sqlite3

with sqlite3.connect("sqlite/app.db") as connectionDB:
    cursor = connectionDB.cursor()
    usuarios = [
        (2, "Chanchito"),
        (3, "Feliz"),
        (4, "Chanchito Triste"),
    ]
    cursor.executemany(
        "insert into usuarios values(?, ?)",
        usuarios,
    )

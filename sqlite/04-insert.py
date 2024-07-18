import sqlite3

with sqlite3.connect("sqlite/app.db") as connectionDB:
    cursor = connectionDB.cursor()
    cursor.execute(
        "insert into usuarios values(?, ?)",
        (1, "Abraham"),
    )

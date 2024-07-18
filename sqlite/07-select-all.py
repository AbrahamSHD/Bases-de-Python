import sqlite3

with sqlite3.connect("sqlite/app.db") as connectionDB:
    cursor = connectionDB.cursor()
    cursor.execute("SELECT * from usuarios")
    # print(cursor.fetchmany(size=2))
    print(cursor.fetchall())

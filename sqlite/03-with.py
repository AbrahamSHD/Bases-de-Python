import sqlite3

with sqlite3.connect("sqlite/app.db") as connectionDB:
    cursor = connectionDB.cursor()
    cursor.execute(
        """
        CREATE TABLE if not exists usuarios
        (id INTEGER primary key, nombre VARCHAR(50))
        """
    )

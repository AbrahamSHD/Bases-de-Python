import sqlite3

connectionDB = sqlite3.connect("sqlite/app.db")
cursor = connectionDB.cursor()
cursor.execute(
    """
    CREATE TABLE if not exists usuarios
    (id INTEGER primary key, nombre VARCHAR(50))
    """
)
connectionDB.commit()
connectionDB.close()

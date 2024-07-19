# import time

# print(time.time())

from datetime import datetime

fecha = datetime(2024, 6, 18)
fecha2 = datetime(2024, 7, 18)
# ahora = datetime.now()

# ? La separación entre año mes y día debe ser igual en cada argumento
fechaStr = datetime.strptime("2023-01-01", "%Y-%m-%d")

print(fecha.strftime("%Y-%m-%d"))
print(fecha > fecha2)
print(
    fecha.year,
    fecha.month,
    fecha.day,
    fecha.hour,
    fecha.minute
)

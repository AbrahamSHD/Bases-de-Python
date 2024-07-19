from datetime import datetime, timedelta

fecha1 = datetime(2024, 1, 1) - timedelta(weeks=1)
fecha2 = datetime(2024, 2, 1)

delta = fecha2 - fecha1
print(delta)
print("Dias: ", delta.days)
print("Segundos", delta.seconds)
print("Microsegundos: ", delta.microseconds)
print("Total_seconds(): ", delta.total_seconds())

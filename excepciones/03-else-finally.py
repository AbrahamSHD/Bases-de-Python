try:
    n1 = int(input("Ingresa un número: "))
except ValueError as ex:
    print(f"Ocurrió un error: {ex}")
    print("Ingrese un valor que corresponda")
except NameError as ex:
    print(f"Ocurrió un error: {ex}")
else:
    print("Todo salió correctamente")
finally:
    print("Se ejecuta siempre")

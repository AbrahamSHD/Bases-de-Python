def division(n=0):
    if n == 0:
        raise ZeroDivisionError(f"No se puede dividir por {n}")
    return 5 / n


try:
    division()
except ZeroDivisionError as ex:
    print(ex)

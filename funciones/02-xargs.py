def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma()
suma(10, 20)
suma(10, 20, 30)
suma(10, 20, 30, 40)
suma(10, 20, 30, 40, 50)

print('Bienvenido, ingresa un número, la operación que quieres realizar y posteriormente otro número')
print('Para terminar salir escribe "salir", operaciones: suma, resta, multiplicación, división')

while True:
    numero_1 = int(input('Ingresa un número: '))
    operacion = input('Ingresa la operación: ')
    numero_2 = int(input('Ingresa un número: '))

    if numero_1 == '':
        numero_1 = int(input('Ingresa un número: '))

    if operacion == '':
        operacion = int(input('Ingresa la operación: '))
        command = input('$ ')
        print(command)
        if command.lower() == 'salir':
            break

    if numero_2 == '':
        numero_2 = int(input('Ingresa un número: '))
        if command.lower() == 'salir':
            break

    if operacion.lower == 'suma':
        print(f"Resaultado: {numero_1} + {numero_2} = {numero_1 + numero_2}")
        if command.lower() == 'salir':
            break

    if operacion.lower == 'resta':
        print(f"Resaultado: {numero_1} - {numero_2} = {numero_1 - numero_2}")
        if command.lower() == 'salir':
            break

    if operacion.lower == 'multiplicacion':
        print(f"Resaultado: {numero_1} * {numero_2} = {numero_1 * numero_2}")
        if command.lower() == 'salir':
            break

    if operacion.lower == 'division':
        print(f"Resaultado: {numero_1} / {numero_2} = {numero_1 / numero_2}")
        if command.lower() == 'salir':
            break

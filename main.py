import random  # Importamos el módulo random

jugar = "si"  # Creamos la variable jugar con el valor "si"

while jugar == "si":  # Repite el juego mientras jugar sea igual a "si"

    numero_secreto = random.randint(1, 100)  # Generamos un número aleatorio del 1 al 100
    print(numero_secreto)
    print("""
====================
    ADIVINA EL NUMERO
====================

El numero esta en el rango del 1 al 100.

Tienes 10 intentos para encontrarlo.

====================
        REGLAS
====================

-Si estas a 5 numeros o menos, estas cerca.
-El programa te dira si el numero secreto es mayor.
-El programa te dira si el numero secreto es menor.

====================
""")

    intentos = 0  # Comenzamos el contador de intentos en 0

    numero_usuario = int(input("Ingresa un numero: "))  # Pedimos el primer número
    intentos += 1  # Contamos el primer intento

    while numero_usuario != numero_secreto and intentos < 10:
        # Repetimos mientras no acierte y tenga menos de 10 intentos

        distancia = abs(numero_usuario - numero_secreto)
        # Calculamos la distancia entre el número ingresado y el secreto

        if distancia <= 5:
            print("Estas cerca")

        elif numero_secreto > numero_usuario:
            print("El numero es mayor")

        else:
            print("El numero es menor")

        numero_usuario = int(input("Ingresa un numero: "))
        intentos += 1

    if numero_usuario == numero_secreto:
        print(
            f"Ganaste, has encontrado el numero correcto, "
            f"lo conseguiste en: {intentos} intentos"
        )

    else:
        print(
            f"Perdiste, has agotado tus intentos, "
            f"el numero era: {numero_secreto}"
        )

    jugar = input("¿Quieres volver a jugar? (si/no): ").lower()

    while jugar != "si" and jugar != "no":
        jugar = input("¿Quieres volver a jugar? (si/no): ").lower()
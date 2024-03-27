import random

print("¡Bienvenido al juego de adivinanza de números!")
print("Intentaré adivinar el número que estás pensando entre 1 y 10.")

numero_secreto = random.randint(1, 10)
intentos = 0

while True:
    intento = int(input("Introduce tu número (o 0 para rendirte): "))
    intentos += 1

    if intento == 0:
        print(f"¡Te rendiste! El número secreto era {numero_secreto}.")
        break
    elif intento < numero_secreto:
        print("Demasiado bajo. Intenta de nuevo.")
    elif intento > numero_secreto:
        print("Demasiado alto. Intenta de nuevo.")
    else:
        print(f"¡Adivinaste! El número secreto era {numero_secreto} y lo lograste en {intentos} intentos.")
        break
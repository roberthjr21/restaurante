import random

def juego():
    numero_secreto = random.randint(1, 10)
    intentos = 0

    while True:
        numero_usuario = int(input("Adivina el número secreto entre 1 y 10: "))
        intentos += 1

        if numero_usuario == numero_secreto:
            print(f"¡Felicidades! Has adivinado el número secreto en {intentos} intentos.")
            break
        elif numero_usuario < numero_secreto:
            print("El número secreto es mayor. Intenta de nuevo.")
        else:
            print("El número secreto es menor. Intenta de nuevo.")



def juego():
    while True:
        numero_secreto = random.randint(1, 10)
        intentos = 0

        while True:
            numero_usuario = int(input("Adivina el número secreto entre 1 y 10: "))
            intentos += 1

            if numero_usuario == numero_secreto:
                print(f"¡Felicidades! Has adivinado el número secreto en {intentos} intentos.")
                break
            elif numero_usuario < numero_secreto:
                print("El número secreto es mayor. Intenta de nuevo.")
            else:
                print("El número secreto es menor. Intenta de nuevo.")

        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ")
        if jugar_de_nuevo.lower() != "s":
            break

if __name__ == "__main__":
    juego()
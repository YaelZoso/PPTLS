import random
import time
from diccionarios import dibujos, opciones

cantidad_partidas = 3

RESET = "\033[0m"
AZUL = "\033[94m"
VERDE = "\033[92m"
ROJO = "\033[91m"
AMARILLO = "\033[93m"


def mostrar_dibujo(opcion, color=RESET):
    nombre = opciones.get(opcion)
    if nombre:
        print(f"{color}{nombre.capitalize()}:{RESET}")
        print(f"{color}{dibujos[nombre]}{RESET}")
    else:
        print("Opcion invalida")


def determinar_ganador(jugador1, jugador2):
    reglas = {
        1: [3, 4],  # piedra vence a tijera y lagarto
        2: [1, 5],  # papel vence a piedra y spock
        3: [2, 4],  # tijera vence a papel y lagarto
        4: [2, 5],  # lagarto vence a papel y spock
        5: [1, 3]   # spock vence a piedra y tijera
    }

    if jugador1 == jugador2:
        return "empate"
    elif jugador2 in reglas[jugador1]:
        return "jugador 1"
    else:
        return "jugador 2"


def jugar_maquina():
    puntuacion1 = 0
    puntuacion2 = 0

    while puntuacion1 + puntuacion2 < cantidad_partidas:
        print("\n1. Piedra\n2. Papel\n3. Tijera\n4. Lagarto\n5. Spock")
        usuario = int(input("Elige una opción: "))
        maquina = random.choice([1, 2, 3, 4, 5])

        print("\nTu elección:")
        mostrar_dibujo(usuario, AZUL)
        print("Elección de la máquina:")
        print(".", end="", flush=True)
        time.sleep(0.5)
        mostrar_dibujo(maquina, ROJO)

        resultado = determinar_ganador(usuario, maquina)

        if resultado == "jugador 1":
            puntuacion1 += 1
            print("¡Ganaste esta ronda!, no te confies")
        elif resultado == "jugador 2":
            puntuacion2 += 1
            print("¡La máquina gana esta ronda!")
        else:
            print("Empate.")

        print(f"Puntuación: Tú {puntuacion1} - Máquina {puntuacion2}")

    if puntuacion1 > puntuacion2:
        print(f"\n¡Felicidades! Has ganado el mejor de {cantidad_partidas}.")
    else:
        print(f"\n¡La máquina gana el mejor de {cantidad_partidas}!")


def jugar_usuario():
    puntuacion1 = 0
    puntuacion2 = 0

    while puntuacion1 + puntuacion2 < cantidad_partidas:
        print("\n1. Piedra\n2. Papel\n3. Tijera\n4. Lagarto\n5. Spock")
        jugador1 = int(input("Jugador 1, elige: "))
        jugador2 = int(input("Jugador 2, elige: "))

        print("\nJugador 1 eligió:")
        mostrar_dibujo(jugador1, AZUL)
        print("Jugador 2 eligió:")
        mostrar_dibujo(jugador2, VERDE)

        resultado = determinar_ganador(jugador1, jugador2)

        if resultado == "Jugador 1":
            puntuacion1 += 1
            print("Jugador 1 gana esta ronda.")
        elif resultado == "Jugador 2":
            puntuacion2 += 1
            print("Jugador 2 gana esta ronda.")
        else:
            print("Empate.")

        print(f"Jugador 1 - {puntuacion1} | Jugador 2 - {puntuacion2}")

    if puntuacion1 > puntuacion2:
        print(f"\n¡Jugador 1 gana el mejor de {cantidad_partidas}!")
    else:
        print(f"\n¡Jugador 2 gana el mejor de {cantidad_partidas}!")


def main():
    print("Bienvenido al juego PPTLS")
    print("¿Contra quién quieres jugar? "
          "1: Jugador VS Máquina | ""2: Jugador VS Jugador")
    opcion = int(input("Introduce una opción 1 o 2: "))
    if opcion == 1:
        jugar_maquina()
    elif opcion == 2:
        jugar_usuario()
    else:
        print("Opción no válida. Inténtalo de nuevo.")

    jugar_de_nuevo = input("¿Quieres volver a jugar? (s/n): ").lower()
    if jugar_de_nuevo == "s":
        main()


main()

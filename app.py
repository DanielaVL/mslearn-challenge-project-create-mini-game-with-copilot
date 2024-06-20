# escribe 'hola mundo' en la consola 
# print('Hola mundo')

# construye el juego de piedra, papel y tijera
# hay tres reglas simples: la rock gana a las scissors, las scissors ganan al paper y el paper gana a la rock
# el juego es multijugador, donde el ordenador es el oponente y podra elegir aleatoriamiente una de las tres opciones por cada movimiento
# la interacción con el juego será a través de la consola (terminal)
# el jugador podrá elegir una de las tres opciones, rock, paper o scissors, y se le debería advertir en caso de introducir una opción no válida
# en cada ronda, el jugador debe entrar en una de las opciones de la lista y ser informado de si ganó, perdió o empató con el oponente
# al final de cada ronda, el jugador elegirá si vuelve a jugar
# muestra la puntuación del jugador al final del juego
# el minijuego debe controlar las entradas del usuario, colocarlas en minúsculas e informar al usuario si la opción no es válida

# ---------------------------------------- SOLUCIÓN MÍA----------------------------------------

# construye el juego de piedra, papel y tijera en python
# hay tres reglas simples: la rock gana a las scissors, las scissors ganan al paper y el paper gana a la rock
# empieza a importar la librería random
import random

# crea una lista de opciones para el juego
opciones = ['rock', 'paper', 'scissors']

# crea una variable para la puntuación del jugador
puntuacion = 0

# crea una variable para el juego
jugar = True

# crea una variable para el numero de rondas
rondas = 0

# crea una variable para el numero de victorias
victorias = 0

# crea un bucle para el juego añadiendo el conteo de rondas y victorias
while jugar:
    # incrementa el numero de rondas
    rondas += 1
    # imprime el numero de rondas
    print(f'Ronda {rondas}')
    # pide al jugador que elija una opción
    jugador = input('Elige rock, paper o scissors: ').lower()
    # elige aleatoriamente una opción para el oponente
    oponente = random.choice(opciones)
    # imprime la elección del oponente
    print(f'Oponente: {oponente}')
    # comprueba si el jugador ha elegido una opción válida
    if jugador in opciones:
        # comprueba si el jugador ha ganado
        if (jugador == 'rock' and oponente == 'scissors') or (jugador == 'scissors' and oponente == 'paper') or (jugador == 'paper' and oponente == 'rock'):
            # incrementa la puntuación del jugador
            puntuacion += 1
            # incrementa el numero de victorias
            victorias += 1
            # imprime un mensaje de victoria
            print('¡Ganaste!')
        # comprueba si el jugador ha perdido
        elif (jugador == 'rock' and oponente == 'paper') or (jugador == 'scissors' and oponente == 'rock') or (jugador == 'paper' and oponente == 'scissors'):
            # imprime un mensaje de derrota
            print('Perdiste!')
        # comprueba si el jugador ha empatado
        else:
            # imprime un mensaje de empate
            print('Empate!')
    # si el jugador no ha elegido una opción válida
    else:
        # imprime un mensaje de error
        print('Opción no válida!')
    # pide al jugador que elija si quiere volver a jugar
    jugar = input('¿Quieres jugar de nuevo? (si/no): ').lower() == 'si'

# imprime un mensaje de despedida
print('Gracias por jugar!')
#imprime el numero de rondas jugadas
print(f'Rondas jugadas: {rondas}')
#imprime el numero de victorias
print(f'Victorias: {victorias}')
# imprime la puntuación final del jugador
print(f'Puntuación final: {puntuacion}')

# ---------------------------------------- SOLUCIÓN ESPERADA ----------------------------------------
# create a rock paper scissors game using python with GitHub Copilot

# import the random module
import random

# create a list of options
options = ["rock", "paper", "scissors"]

# create the score and round played variables
score = 0
rounds_played = 0

# create the loop to play the game

while True:

    # choose a random option of the list
    computer_choice = random.choice(options)

    # asking for the user input
    player_choice = input("Rock, paper or scissors?  ")

    # if player chose rock 
    if player_choice.lower() == "rock":
        if computer_choice == "rock":
            print("Computer chose rock. It's a tie!")
        elif computer_choice == "paper":
            print("Computer chose paper. You lose!")
        elif computer_choice == "scissors":
            print("Computer chose scissors. You win!")
            score += 1
        rounds_played += 1

    # if player chose paper
    elif player_choice.lower() == "paper":
        if computer_choice == "rock":
            print("Computer chose rock. You win!")
            score += 1
        elif computer_choice == "paper":
            print("Computer chose paper. It's a tie!")
        elif computer_choice == "scissors":
            print("Computer chose scissors. You lose!")
        rounds_played += 1

    # if player chose scissors
    elif player_choice.lower() == "scissors":
        if computer_choice == "rock":
            print("Computer chose rock. You lose!")
        elif computer_choice == "paper":
            print("Computer chose paper. You win!")
            score += 1
        elif computer_choice == "scissors":
            print("Computer chose scissors. It's a tie!")
        rounds_played += 1

    # if player chose something else
    else:
        print("That's not a valid play. Check your spelling!")

    # ask the user if they want to play again and break the loop if they don't
    # if they break the loop, print the score
    play_again = input("Do you want to play again? (y/n) ")
    if play_again.lower() != "y":
        print(f"You played {rounds_played} rounds and got {score} points!")
        break

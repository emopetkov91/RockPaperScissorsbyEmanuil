import random
from colorama import Fore, Style , init

init()

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player_score = 0
computer_score = 0

while player_score < 2 and computer_score < 2:
    player_move = input("\nChoose [r]ock, [p]aper or [s]cissors: ")

    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        print(Fore.RED + "Invalid Input. Try again ...")
        continue

    computer_random_number = random.randint(1, 3)
    computer_move = " "

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    else:
        computer_move = scissors

    print(Fore.CYAN + f"Computer chose {computer_move}")

    if (player_move == rock and computer_move == scissors) or (player_move == paper and computer_move == rock) or (player_move == scissors and computer_move == paper):
        print(Fore.GREEN + "You Win This Round!")
        player_score += 1
    elif player_move == computer_move:
        print(Fore.YELLOW + "Draw!")
    else:
        print(Fore.RED + "You Lose This Round!")
        computer_score += 1

if player_score == 2:
    print(Fore.GREEN + "\nYOU WON THE MATCH!")
else:
    print(Fore.RED + "\nCOMPUTER WON THE MATCH!")

print(Style.RESET_ALL)
print(f"Score -> You: {player_score} | Computer: {computer_score}")
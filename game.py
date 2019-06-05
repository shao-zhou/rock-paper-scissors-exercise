# game.py

import random

print("Rock, Paper, Scissors, Shoot!")

# CAPTURE INPUTS

user_choice = input("Please choose one of the following options: 'rock', 'paper', or 'scissors' (without the quotes):")

print("------------------")
print("USER CHOICE:", user_choice)

# VALIDATE INPUTS

options = ["rock", "paper", "scissors"]

if user_choice not in options:
    print("INVALID SELECTION, PLEASE TRY AGAIN...")
    exit()

# GENERATE COMPUTER SELECTION

computer_choice = random.choice(options)
print("------------------")
print("GENERATING...")
print("COMPUTER CHOICE:", computer_choice)

# DETERMINE WINNER

# rock beats scissors
# paper beats rock
# scissors beats paper
# same selection is a tie

if user_choice == computer_choice:
    print("TIE")
elif user_choice == "rock" and computer_choice == "paper":
    print("PAPER")
elif user_choice == "rock" and computer_choice == "scissors":
    print("ROCK")
elif user_choice == "paper" and computer_choice == "rock":
    print("ROCK")
elif user_choice == "paper" and computer_choice == "scissors":
    print("SCISSORS")
elif user_choice == "scissors" and computer_choice == "rock":
    print("ROCK")
elif user_choice == "scissors" and computer_choice == "paper":
    print("SCISSORS")

# DISPLAY FINAL OUTPUTS / OUTCOMES
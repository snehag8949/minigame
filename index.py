import random

def get_player_choice():
    while True:
        choice = input("Choose rock, paper, or scissors: ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player_choice, computer_choice):
    print(f"\nYou chose {player_choice}, computer chose {computer_choice}.\n")
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")

while True:
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    determine_winner(player_choice, computer_choice)

    play_again = input("Play again? (y/n): ").lower()
    if play_again != "y":
        break

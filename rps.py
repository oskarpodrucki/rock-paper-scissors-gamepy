import random

def winner(player, computer):
    if player == computer:
        return "TIE!"
    elif (player == "rock" and computer == "scissors") or \
        (player == "paper" and computer == "rock") or \
        (player == "scissors" and computer == "paper"):
        return "PLAYER WINS!"
    else:
        return "COMPUTER WINS!"

def main():

    choices = ['rock', 'paper', 'scissors']

    while True:
        print("\nRock, Paper, Scissors")
        player = input("Your choice: ").lower()

        if player not in choices:
            print("Invalid choice. Choose again")
            continue

        computer = random.choice(choices)
        print("Computer's choice: ", computer)

        print(winner(player, computer))

        playAgain = input("Do you want to play again? (y/n) ").lower()
        if playAgain != "y":
            print("THANKS FOR PLAYING!")
            break

if __name__ == "__main__":
    main()

import random

VALID_CHOICES = {"rock", "paper", "scissors"}


def get_computer_choice():
    return random.choice(list(VALID_CHOICES))


def get_user_choice():
    while True:
        choice = input("Choose rock, paper, or scissors: ").strip().lower()
        if choice in VALID_CHOICES:
            return choice
        print(f"Invalid choice: '{choice}'. Please choose rock, paper, or scissors.\n")


def determine_winner(user, computer):
    if user == computer:
        return "tie"

    if (
        (user == "rock" and computer == "scissors")
        or (user == "paper" and computer == "rock")
        or (user == "scissors" and computer == "paper")
    ):
        return "user"
    else:
        return "computer"


def play_round():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    winner = determine_winner(user_choice, computer_choice)

    if winner == "tie":
        print("Result: It's a tie!\n")
    elif winner == "user":
        print("Result: You win!\n")
    else:
        print("Result: Computer wins!\n")

    return winner


def main():
    print("=== Rock-Paper-Scissors ===\n")

    wins = 0
    losses = 0
    ties = 0

    while True:
        winner = play_round()

        if winner == "user":
            wins += 1
        elif winner == "computer":
            losses += 1
        else:
            ties += 1

        again = input("Play again? (y/n): ").strip().lower()
        print()
        if again != "y":
            print(f"Final score -> Wins: {wins}, Losses: {losses}, Ties: {ties}")
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
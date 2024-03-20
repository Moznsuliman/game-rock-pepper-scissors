import random

def get_user_choice():
    """Get user's choice (rock, paper, scissors)"""
    valid_choices = ("rock", "paper", "scissors")
    user_choice = input("Enter your choice (rock, paper, scissors): ")
    while user_choice not in valid_choices:
        user_choice = input("Invalid choice. Please enter again: ")
    return user_choice

def get_computer_choice():
    """Get computer's choice (rock, paper, scissors)"""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner (user or computer)"""
    if user_choice == computer_choice:
        return "tie"
    if (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "scissors" and computer_choice == "paper") or \
       (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    """Play a game of rock, paper, scissors"""
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"User choose: {user_choice}")
    print(f"Computer choose: {computer_choice}")
    winner = determine_winner(user_choice, computer_choice)
    if winner == "user":
        print("User wins!")
    elif winner == "computer":
        print("Computer wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_game()
import random

# Display game instructions
print("Welcome to Rock-Paper-Scissors-Lizard-Spock!")
print("Instructions:")
print("1. Choose a move.")
print("2. Enter your move (options are case-sensitive).")
print("3. The winner will be determined based on the rules:")

# Define the game rules
rules = {
    "rock": ["scissors", "lizard"],
    "scissors": ["paper", "lizard"],
    "paper": ["rock", "spock"],
    "lizard": ["spock", "paper"],
    "spock": ["rock", "scissors"]
}

# Display the available moves
moves = list(rules.keys())
print("Available moves:", ", ".join(moves))

# Get user's move
user_move = input("Enter your move: ")

# Generate a random move for the computer
comp_move = random.choice(moves)

# Display the choices
print("\nResults:")
print("Your choice:", user_move)
print("Computer's choice:", comp_move)

# Determine the winner
if user_move == comp_move:
    print("\nIt's a TIE GAME!")
elif user_move in rules and comp_move in rules:
    if comp_move in rules[user_move]:
        print(f"\n{user_move.upper()} beats {comp_move.upper()}. YOU WIN!")
    else:
        print(f"\n{comp_move.upper()} beats {user_move.upper()}. COMPUTER WINS!")
else:
    print("\nInvalid move! Please choose a valid move from the available options.")

# Offer to play again
play_again = input("\nPlay again? (yes/no): ")
if play_again.lower() == "yes":
    print("\nLet's play again!")
else:
    print("\nThanks for playing!")
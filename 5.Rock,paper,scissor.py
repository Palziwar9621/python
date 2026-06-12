import random

choice = ["stone", "scissors", "paper"]

player_choice = input("Enter your choice (stone, scissors, paper): ").strip().lower()

if player_choice not in choice:
    print("Invalid choice! Please choose stone, scissors, or paper.")
else:
    computer_choice = random.choice(choice)
    print(f"Computer chose: {computer_choice}")

    # Method 1 - if/elif
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "stone" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "stone"):
        print("You win!")
    else:
        print("Computer wins!")

    # Method 2 - matrix
    outcome_matrix = {
        ("stone", "scissors"): "You win!",
        ("scissors", "paper"): "You win!",
        ("paper", "stone"): "You win!",
        ("scissors", "stone"): "Computer wins!",
        ("paper", "scissors"): "Computer wins!",
        ("stone", "paper"): "Computer wins!",
        ("stone", "stone"): "It's a tie!",
        ("scissors", "scissors"): "It's a tie!",
        ("paper", "paper"): "It's a tie!"
    }

    print(outcome_matrix[(player_choice, computer_choice)])
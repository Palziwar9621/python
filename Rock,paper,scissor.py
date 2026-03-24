choice=["stone","scissors","paper"]
import random
player_choice=str(input("Enter your choice (stone, scissors, paper): ")).lower()
computer_choice=random.choice(choice)
print(f"Computer chose: {computer_choice}")
if (player_choice == computer_choice):
    print("It's a tie!")
elif (player_choice =="stone" and computer_choice=="paper") or(player_choice=="paper"and computer_choice=="scissors") or(player_choice=="scissors" and computer_choice=="stone"):
    print("Computer wins!")
else:
    print("You win!")

# now using matrix to determine the winner
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
print(outcome_matrix.get((player_choice, computer_choice), "Invalid choice! Please choose stone, scissors, or paper."))

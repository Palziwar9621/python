import random

number_to_guess = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))
guess_times = 1

while guess != number_to_guess:
    if number_to_guess < guess:
        print("Too high, try lower")
    else:
        print("Too low, try higher")
    guess_times += 1
    guess = int(input("Guess a number between 1 and 100: "))

print(f"Congratulations! You guessed the number in {guess_times} attempts.")

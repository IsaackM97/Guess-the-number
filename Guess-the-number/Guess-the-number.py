import random

hidden_number = random.randrange(1,10) # random number value
guess = int(input("Guess a number between 1-10: "))
guess_count = 1
guess_limit = 5

while guess != hidden_number:
    if guess < hidden_number:
        print(f"Number of turns: {guess_count} ")
        guess_count += 1
        print("Guess higher, try again!")
        guess = int(input("\nGuess a number between 1-10: "))


    else:
        print(f"Number of turns: {guess_count} ")
        guess_count += 1
        print("Guess lower, try again!")
        guess = int(input("\nGuess a number between 1-10: "))




print(f"{guess} is the right number!")




import random

def number_guessing_game():
    number = random.randint(1, 100)
    print("Guess a number between 1 and 100")
    while True:
        guess = int(input("Enter your guess: "))
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number.")
            break

number_guessing_game()

import random as rng


def new_game():
    user_max = input("What max number would you like? ")
    target_number = rng.randrange(1, int(user_max) + 1)  # User gets to choose their own max
    first_guess = False
    guessed_number = int(input("Guess my number: "))
    guess_loop(target_number, int(guessed_number), first_guess)


def guess_loop(number, guess, first_guess):
    if first_guess is True:
        guess = int(input("Guess again: "))
    else:
        first_guess = True
    if guess == number:
        print("You guessed it! My number was " + str(number))
        new_game()
    elif guess > number:
        print("Too high! My number is lower")
        guess_loop(number, guess, first_guess)
    elif guess < number:
        print("Too low! My number is higher")
        guess_loop(number, guess, first_guess)
    else:
        print("Oops! an error occurred :(")


new_game()

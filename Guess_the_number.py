import random

print('''
   _____                           _______ _                _   _                 _                  _ 
  / ____|                         |__   __| |              | \ | |               | |                | |
 | |  __ _   _  ___  ___ ___         | |  | |__   ___      |  \| |_   _ _ __ ___ | |__   ___ _ __   | |
 | | |_ | | | |/ _ \/ __/ __|        | |  | '_ \ / _ \     | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|  | |
 | |__| | |_| |  __/\__ \__ \        | |  | | | |  __/     | |\  | |_| | | | | | | |_) |  __/ |     |_|
  \_____|\__,_|\___||___/___/        |_|  |_| |_|\___|     |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     (_)
''')

print("Welcome to the Number Guessing game!")
print("I'm thinking of a number between 1 and 100")

diff = input("Choose a difficulty.. Type 'easy' or 'hard': ")
guess = 0

if diff == "easy":
    guess = 10
    print("You have 10 attempts remaining to guess the number.")
if diff == "hard":
    guess = 5
    print("You have 5 attempts remaining to guess the number.")

random_number = random.randint(1, 100)

while guess != 0:
    your = int(input("Make a guess: "))
    if random_number > your:
        print("Too low")
        guess -= 1
        print("Guess again.")
        print(f"You have {guess} attempts remaining to guess the number.")

    if random_number < your:
        print("Too High")
        guess -= 1
        print("Guess again.")
        print(f"You have {guess} attempts remaining to guess the number.")

    if random_number == your:
        print(f"You got it! The answer was {random_number}")
        break

    if guess == 0:
        print("You ran out of chances.")
        print(f"The answer was {random_number}.")

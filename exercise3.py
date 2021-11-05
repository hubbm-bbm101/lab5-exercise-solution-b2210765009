import random
correct_number = random.randint(1,100)

guess = int(input("Please guess a number between 1 and 100: "))


while guess != correct_number:
    if guess < correct_number:
        print("Increase your guess.")
        guess = int(input("Please guess another number: "))

    if guess > correct_number:
        print("Decrease your guess.")
        guess = int(input("Please guess another number: "))

if guess == correct_number:
    print("Correct!")



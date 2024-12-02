import random
from logo import text
print(text)
print("Welcome to the number guessing game!\nYou have to guess a number between 1 and 100.")
difficulty = input(
    "Chosse a difficulty level?\n'e' foe easy and 'h' for hard:\n")
attempts = 0
if difficulty == 'e':
    attempts = 10
elif difficulty == "h":
    attempts = 5
else:
    print("Give an valid input.")
    attempts = 0
answer = random.randint(1, 100)
turns = 0
while attempts > 0:
    print(f"You have {attempts} remaining to guess the answer.")
    guess = int(input("Guess the number?\n"))
    attempts -= 1
    turns += 1
    if guess == answer:
        print("You won")
        break
    else:
        if guess > answer:
            print("Guess a smaller number.")
        else:
            print("Guess a bigger number")
if attempts == 0:
    print("Your loss!!!!!")

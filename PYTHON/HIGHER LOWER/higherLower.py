import random
from game_data import data
from art import logo, vs

A = {}
b = {}

A = random.choice(data)


def game():
    global A
    A
    print(logo)
    print("Comapre A:")
    print(A['name'], A['description'], A['country'])
    print(vs)
    global B
    B = random.choice(data)
    print("Against B:")
    print(B['name'], B['description'], B['country'])


user = True
score = 0
while user == True:
    game()
    choice = input("Which one has more instahgram followers?A or B\n")
    if choice == "A":
        if A['follower_count'] > B['follower_count']:
            print("A folower count is", A['follower_count'], "millions")
            print("B folower count is", B['follower_count'], "millions")
            user == True
        else:
            print("A folower count is", A['follower_count'], "millions")
            print("B folower count is", B['follower_count'], "millions")
            user == False
            break
    elif choice == "B":
        if A['follower_count'] < B['follower_count']:
            print("A folower count is", A['follower_count'], "millions")
            print("B folower count is", B['follower_count'], "millions")
            A = B
            user == True
        else:
            print("A folower count is", A['follower_count'], "millions")
            print("B folower count is", B['follower_count'], "millions")
            user == False
            break
    else:
        break

    score += 1


print(f"Sorry that was wrong and your final score is {score}.")

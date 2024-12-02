import random
from art import logo
print(logo)
user = []
cpu = []


def fn():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random.shuffle(cards)
    user.append(random.choice(cards))
    return user


def fn_cpu():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random.shuffle(cards)
    cpu.append(random.choice(cards))
    return cpu


def f():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random.shuffle(cards)
    user.append(random.choice(cards))
    cpu.append(random.choice(cards))
    return user, cpu


def g(x):
    result = 0
    for i in x:
        result += int(i)
    return result


if input("Do you want to play this game 'y' or 'n' ") == "y":
    f()
    print(user)
    print(cpu)

Choice = ["y", "n", "y"]
while input("Do u want to take one more card 'y' or 'no'.") == "y":
    fn()
    score = g(user)
    if score > 21:
        if user[len(user)-1] == 11:
            user[len(user)-1] = 1
    score = g(user)
    print(f"your cards are {user} and your score is {score} ")

cpu_choice = random.choice(Choice)
while cpu_choice == "y":
    cpu_choice = random.choice(Choice)
    fn_cpu()
    score = g(cpu)
    if score > 21:
        if cpu_choice == 11:
            cpu[len(cpu)-1] = 1
        else:
            break
score_user = g(user)
print(f"your cards are {user} and your score is {score_user} ")
score_cpu = g(cpu)
print(f"cpu cards are {cpu} and cpu score is {score_cpu} ")
if (score_cpu > 21 & score_user > 21) or (score_user == score_cpu):
    print(""" ____  ____      ___        __
|  _ \|  _ \    / \ \      / /
| | | | |_) |  / _ \ \ /\ / / 
| |_| |  _ <  / ___ \ V  V /  
|____/|_| \_\/_/   \_\_/\_/   """)


elif (score_user > 21) or (score_cpu > score_user):
    print("""  ____ ____  _   _  __        _____  _   _ 
 / ___|  _ \| | | | \ \      / / _ \| \ | |
| |   | |_) | | | |  \ \ /\ / / | | |  \| |
| |___|  __/| |_| |   \ V  V /| |_| | |\  |
 \____|_|    \___/     \_/\_/  \___/|_| \_|""")


else:
    print("""__   _____  _   _  __        _____  _   _
\ \ / / _ \| | | | \ \      / / _ \| \ | |
 \ V / | | | | | |  \ \ /\ / / | | |  \| |
  | || |_| | |_| |   \ V  V /| |_| | |\  |
  |_| \___/ \___/     \_/\_/  \___/|_| \_|""")

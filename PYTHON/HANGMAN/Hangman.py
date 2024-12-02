print(""" _   _    _    _   _  ____ __  __    _    _   _ 
| | | |  / \  | \ | |/ ___|  \/  |  / \  | \ | |
| |_| | / _ \ |  \| | |  _| |\/| | / _ \ |  \| |
|  _  |/ ___ \| |\  | |_| | |  | |/ ___ \| |\  |
|_| |_/_/   \_\_| \_|\____|_|  |_/_/   \_\_| \_|""")

print("Guess the word! \n")
lives=6
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
word_list=["matreyee","akanksha","pranav"]
import random
chossen_word=word=random.choice(word_list)
a=""
count=0
for i in chossen_word:
    a+="_"
    count+=1
a=list(a)
print(a)
def check(x):
    value=[]
    length_x=len(x)
    for i in range(0,length_x):
        if x[i]=="_":
            value.append(True)
        else:
            value.append(False)
    length_value=len(value)
    answer=False
    for i in range (0,length_value):
        if value[i]==True:
            answer=True
        else:
            0
    return answer
def test(x):
    value=[]
    length_x=len(x)
    for i in range(0,length_x):
        if x[i]==True:
            value.append(True)
        else:
            value.append(False)
    length_value=len(value)
    answer=False
    for i in range (0,length_value):
        if value[i]==True:
            answer=True
        else:
            0
    return answer
while check(a)==True and lives>=0:
    m=0
    guess=input("guess a letter:\n")
    guess=guess.lower()
    list=[]
    for i in chossen_word:
        if guess==i:
            list.append(True)
            a[m]=i
            m+=1
            
        else:
            list.append(False)
            m+=1
    print(a)
    if test(list)==True:
        0
    else:
        print(HANGMANPICS[6-lives])
        lives-=1
        print("OOOPS")
        print(f"you are left with only {lives} lives")
    if lives<0:
        print("You Lost")

print(a)

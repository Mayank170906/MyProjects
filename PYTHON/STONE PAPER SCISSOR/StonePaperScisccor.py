import random
print("""$$\   $$\ $$$$$$$$\ $$\       $$\       $$$$$$\    
$$ |  $$ |$$  _____|$$ |      $$ |     $$  __$$\   
$$ |  $$ |$$ |      $$ |      $$ |     $$ /  $$ |  
$$$$$$$$ |$$$$$\    $$ |      $$ |     $$ |  $$ |  
$$  __$$ |$$  __|   $$ |      $$ |     $$ |  $$ |  
$$ |  $$ |$$ |      $$ |      $$ |     $$ |  $$ |  
$$ |  $$ |$$$$$$$$\ $$$$$$$$\ $$$$$$$$\ $$$$$$  |  
\__|  \__|\________|\________|\________|\______/  
""")
user=input("stone,paper,scissor\n")
user=user.lower()
result=["stone","paper","scissor"]
cpu=random.choice(result)
if((user!="stone")|(user!="paper")|(user!="scissor")):
    print("Invalid choice")
if(cpu=="stone"):
    print("""cpu=\n  _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)""")

if(cpu=="paper"):
    print("""cpu=\n  _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________) """)
if(cpu=="scissor"):
    print("""cpu=\n _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___) """)
if(user=="stone"):
    print("""user=\n  _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)""")

if(user=="paper"):
    print("""user=\n  _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________) """)
if(user=="scissor"):
    print("""user=\n _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___) """)
    
if((cpu=="stone")&(user=="paper")):
    print("""          _       
__      _(_)_ __  
\ \ /\ / / | '_ \ 
 \ V  V /| | | | |
  \_/\_/ |_|_| |_|""")

if((cpu=="paper")&(user=="scissor")):
    print("""          _       
__      _(_)_ __  
\ \ /\ / / | '_ \ 
 \ V  V /| | | | |
  \_/\_/ |_|_| |_|""")
    
if((cpu=="scissor")&(user=="stone")):
    print("""          _       
__      _(_)_ __  
\ \ /\ / / | '_ \ 
 \ V  V /| | | | |
  \_/\_/ |_|_| |_|""")
elif((cpu==user)):
        print("""     _                    
  __| |_ __ __ ___      __
 / _` | '__/ _` \ \ /\ / /
| (_| | | | (_| |\ V  V / 
 \__,_|_|  \__,_| \_/\_/  """)
else:
    print(""" _           _   
| | ___  ___| |_ 
| |/ _ \/ __| __|
| | (_) \__ \ |_ 
|_|\___/|___/\__|""")
    







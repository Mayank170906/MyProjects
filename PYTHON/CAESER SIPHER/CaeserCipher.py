alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print("""  ____                            ____  _       _               
 / ___|__ _  ___  ___  ___ _ __  / ___|(_)_ __ | |__   ___ _ __ 
| |   / _` |/ _ \/ __|/ _ \ '__| \___ \| | '_ \| '_ \ / _ \ '__|
| |__| (_| |  __/\__ \  __/ |     ___) | | |_) | | | |  __/ |   
 \____\__,_|\___||___/\___|_|    |____/|_| .__/|_| |_|\___|_|   
                                         |_|                    """)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def encrypt(text,shift):
    shift=shift % 26
    answer=""
    for i in text:
        if i in alphabet:
            position=alphabet.index(i)
            answer+=alphabet[position+shift]
        else:
            answer+=str(i)
    print(answer)
    text=str(answer)
def decrypt(text,shift):
    shift=shift%26
    answer=""
    for i in text:
        if i in alphabet:
            position=alphabet.index(i)
            answer+=alphabet[position-shift]
        else:
            answer+=str(i)
    print(answer)
    text=str(answer)
if direction=="encode":
    encrypt(text,shift)
    user=input("Do u want to encode again?yes or no. ")
    while user=="yes":
        
        encrypt(text,shift)
        user=input("Do u want to encode again?yes or no. ")

elif direction=="decode":
    decrypt(text,shift)
else:
    print("Wrong inputs!") 
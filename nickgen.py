import random
import string
from colorama import Fore, init
import os
import time
import sys
from datetime import datetime


init()

def start():
    print(Fore.WHITE + " ")
    print(Fore.GREEN + "Starting...")
    time.sleep(3)
    global start_time
    start_time = datetime.now()
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print(Fore.MAGENTA + """
   _____ __         __          __ 
  / ___// /____  __/ /__  _____/ /_
  \__ \/ //_/ / / / / _ \/ ___/ __/
 ___/ / ,< / /_/ / /  __/ /  / /_  
/____/_/|_|\__, /_/\___/_/   \__/  
          /____/                   
""")

def generate_pseudo(length=8):
    blocks = [
        string.ascii_letters,  # BASIC LATIN
        string.printable[95:127],  # BASIC LATIN (Punctuation)
        string.printable[128:160],  # LATIN-1 SUPPLEMENT
        string.printable[160:383],  # LATIN EXTENDED-A
        string.printable[383:591],  # LATIN EXTENDED-B
        string.printable[688:767],  # SPACING MODIFIER LETTERS
        ''.join(chr(i) for i in range(880, 1024)),  # GREEK AND COPTIC
        ''.join(chr(i) for i in range(5760, 5792)),  # OGHAM
        ''.join(chr(i) for i in range(7680, 7936)),  # LATIN EXTENDED ADDITIONAL
        ''.join(chr(i) for i in range(8192, 8304)),  # GENERAL PUNCTUATION
        ''.join(chr(i) for i in range(64256, 64336)),  # ALPHABETIC PRESENTATION FORMS
        ''.join(chr(i) for i in range(64336, 65024)),  # ARABIC PRESENTATION FORMS-A
        ''.join(chr(i) for i in range(65024, 65136))  # ARABIC PRESENTATION FORMS-B
    ]

    characters = ''.join(blocks)

    pseudo = ''.join(random.choice(characters) for _ in range(length))
    return pseudo

if __name__ == "__main__":
    start()
    print("Bienvenue dans le générateur de pseudo !")
    
    while True:
        if len(sys.argv) > 1 and sys.argv[1].isdigit():
            length = int(sys.argv[1])
        else:
            length = int(input("Veuillez entrer la longueur du pseudo souhaitée : "))
        
        print("Votre pseudo généré est:", generate_pseudo(length))
        
        choice = input("Voulez-vous générer un autre pseudo ? (y/n): ").lower()
        if choice != "y":
            break

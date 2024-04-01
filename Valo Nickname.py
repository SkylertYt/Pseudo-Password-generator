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
    eligible_characters = string.ascii_letters + string.digits  # Lettres majuscules, minuscules et chiffres
    pseudo = ''.join(random.choice(eligible_characters) for _ in range(length))
    return pseudo

if __name__ == "__main__":
    start()
    print("Bienvenue dans le générateur de pseudo pour Valorant !")
    
    while True:
        length = int(input("Veuillez entrer la longueur du pseudo souhaitée : "))
        print("Votre pseudo généré est:", generate_pseudo(length))
        
        choice = input("Voulez-vous générer un autre pseudo ? (oui/non): ").lower()
        if choice != "oui":
            break

import time
import os

code = int(input("digite sua senha: "))
os.system('cls' if os.name == 'nt' else 'clear')

def trancado():
    senha = int(input("digite a senha: "))

while trancado() not in code:
    print("errado")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    trancado()
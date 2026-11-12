import time
import os 
import random
import keyboard

hp = 100

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"HP restante: {hp}")
    if hp > 0:
        print("Pressione F para atacar!")
    else:
        print("Inimigo derrotado!")

def attack():
    global hp
    if hp <= 0:
        return
        
    dmg = random.randint(5, 12)
    hp -= dmg
    print(f"\nAtacou por {dmg} de dano!")
    time.sleep(1)
    
    menu()
    
    if hp <= 0:
        keyboard.remove_hotkey('f')

menu()
keyboard.add_hotkey('f', attack)
keyboard.wait('esc')
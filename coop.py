import time
import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait():
    time.sleep(3)

# estatisticas do jogador 1
    p1hp = 100
    p1sp = 30
    p1atk = 0
    p1atkBonus = 0
    p1defBonus = 0
    p1slashBonus = 0
    p1 = str(input("Nome do 1º jogador: "))
    skipP1 = False
    def p1stats():
        print("------------------------------------")
        print(f"HP do {p1}: {p1hp}/100")
        print(f"SP do {p1}: {p1sp}/30")
        print(f"HP do inimigo: {enemyhp}/375")
    p1fireTurns = 0
    p1block = False
    p1MotivateATK = False
    p1MotivateDEF = False
    p1Defend = False
    lifeSteal = False
    ult = False

# estatisticas do jogador 2
    p2hp = 80
    p2sp = 60
    p2atk = 0
    heal = 20
    p2atkBonus = 0
    p2defBonus = 0
    p2 = str(input("Nome do 2º jogador: "))
    skipP2 = False
    def p2stats():
        print("------------------------------------")
        print(f"HP do {p2}: {p2hp}/80")
        print(f"SP do {p2}: {p2sp}/60")
        print(f"HP do inimigo: {enemyhp}/375")
    p2fireTurns = 0
    p2MotivateATK = False
    p2MotivateDEF = False
    p2Defend = False

# estatisticas do inimigo
    enemyhp = 375   
    turns = 0
    skipEnemy = False
    p1target = 0
    p2target = 0
    enemyfireTurns = 0
    distressTurns = 0
    playerChoice = 0

# ailments
    p1onFire = False
    p2onFire = False
    enemyOnFire = False
    enemyDistress = False

def p1Burn():
    global p1fireTurns, p1hp, p1onFire
    p1fireTurns += 1
    if p1fireTurns % 3 != 0:
        p1onFire = True
        print(f"{p1} está queimando! -10HP")
        print("-------------------------------------------------------------")
        p1hp -= 10
    else:
        p1onFire = False
        print("O fogo se passou...")

def p2Burn():
    global p2fireTurns, p2hp, p2onFire
    p2fireTurns += 1
    if p2fireTurns % 3 != 0:
        p2onFire = True
        print(f"{p2} está queimando! -10HP")
        print("-------------------------------------------------------------")
        p2hp -= 10
    else:
        p2onFire = False
        print("O fogo se passou...")

def burn():
    global enemyfireTurns, enemyhp, enemyOnFire
    enemyfireTurns += 1
    if enemyfireTurns % 3 != 0:
        enemyOnFire = True
        print("O inimigo está queimando! -15HP")
        print("-------------------------------------------------------------")
        wait()
        clear()
        enemyhp -= 15
    else:
        enemyOnFire = False
        print("O fogo do inimigo se passou...")
        wait()
        clear()

def distress():
    global p1target, p2target, enemyDistress, distressTurns
    distressTurns += 1
    if distressTurns % 3 != 0:
        enemyDistress = True
        print("O inimigo está distressado! -ATK")
        wait()
        clear()
        print("-------------------------------------------------------------")
        p1target //= 2
        p2target //= 2
    else:
        enemyDistress = False
        print("O distresse passou...")

def pray():
    global p1, p1hp, p2, p2hp, p2sp, heal
    if p2sp < 10:
        print("SP insuficiente.")
        wait()
        clear()
        p2menu()
    print(f"[1] {p1} ({p1hp})")
    print(f"[2] {p2} ({p2hp})")
    print("[3] Voltar")
    try:
        healChoice = int(input("Quem curar? [1/2/3]: "))
    except ValueError:
        healChoice = 0
    while healChoice not in [1, 2, 3]:
        try:
            healChoice = int(input("Escolha válida [1/2/3]: "))
        except ValueError:
            healChoice = 0
    if healChoice == 1:
        print(f"Curou {p1} com {heal}HP!")
        wait()
        clear()
        p2sp -= 10
        p1hp += heal
    elif healChoice == 2:
        print(f"Curou {p2} com {heal}HP!")
        wait()
        clear()
        p2sp -= 10
        p2hp += heal
    elif healChoice == 3:
        clear()
        p2magic()

def block():
    global p1hp, p1sp, p2, p2hp, p2target, p1block, playerChoice
    if p1block:
        p1absorb = p2target // 2
        p1hp -= p1absorb
        print(f"Absorveu {p1absorb} do dano!")
        p1block = False
        wait()
        clear()

def motivate():
    global p2sp, p1MotivateATK, p2MotivateATK, p1MotivateDEF, p2MotivateDEF, p1, p2
    if p2sp < 15:
        print("SP Insuficiente.")
        wait()
        clear()
        p2menu()
        return
    print("-------------------------------------------------------------")
    print(f"[1] {p1}")
    print(f"[2] {p2}")
    print(f"[3] Voltar")
    try:
        mot = int(input("Motivar quem: "))
    except ValueError:
        mot = 0
    while mot not in [1, 2, 3]:
        mot = int(input("Escolha 1 ou 2: "))
    if mot == 1:
        p1MotivateATK = True
        p2MotivateDEF = True
        print(f"{p1} foi motivado! ATK+ e DEF+")
        p2sp -= 15
    elif mot == 2:
        p2MotivateATK = True
        p2MotivateDEF = True
        print(f"{p2} foi motivado! ATK+ e DEF+")
        p2sp -= 15
    elif mot == 3:
        clear()
        p2magic()
        
# ações                               
def p1menu():
    global p1hp, p1sp, p1atk, p2hp, p2sp, enemyhp, skipP1, skipP2, skipEnemy
    if p1hp <= 0:
        return
    p1stats()
    if skipP1:
        print(f"{p1} não pode se mexer!")
        skipP1 = False
        wait()
        clear()
        return
    print(f"------------------------{p1} - Ações--------------------------")
    print("[1] Atacar - Dano básico com baixa chance de crítico")
    print("[2] Habilidades - Menu de habilidades")
    print("[3] Defender - Restora SP e reduz dano tomado")
    try:
        p1action = int(input("O que fazer: "))
    except ValueError:
        p1action = 0
    while p1action not in [1, 2, 3]:
        try:
            p1action = int(input("Escolha ação válida: "))
        except ValueError:
            p1action = 0
    if p1action == 1:
        p1dmg = random.randint(6, 24)
        crit = random.randint(1, 6)
        if crit == 6:
            p1dmg = int(p1dmg * 1.5)
            print(f"Crítico! {p1} atacou e deu {p1dmg} de dano! Derrubou o inimigo!")
            print("-------------------------------------------------------------")  
            skipEnemy = True
            enemyhp -= p1dmg
            wait()
            clear()
            print("-------------------------TURNO EXTRA!------------------------")
            p1menu()
        else:
            print(f"{p1} atacou e deu {p1dmg} de dano!")
            print("-------------------------------------------------------------")
            enemyhp -= p1dmg
            wait()
            clear()
    elif p1action == 2:
        clear()
        p1abilities()
    elif p1action == 3:
        p1sp += 10
        print(f"{p1} defendeu e recuperou 10 SP!")
        print("-------------------------------------------------------------")
        wait()
        clear()

def p1abilities():
    global p1hp, p1sp, p1atk, p2hp, p2sp, enemyhp, skipP1, skipP2, skipEnemy, p1block
    p1stats()
    print(f"------------------------{p1} - Habilidades--------------------------")
    print("[5] Slash - Dano físico com média chance de crítico (25 HP)")
    print("[6] Block - Absorve 50% do dano do aliado, se for atacado. (6 SP)")
    print("[7] Fire - Dano de fogo com baixa chance de Burn (8 SP)")
    print("[8] Voltar")
    try:
        p1ability = int(input("O que fazer: "))
    except ValueError:
        p1ability = 0
    while p1ability not in [5, 6, 7, 8]:
        try:
            p1ability = int(input("Escolha ação válida: "))
        except ValueError:
            p1ability = 0
    if p1ability == 5:
        slash = random.randint(10, 40) + p1atk
        enemyhp -= slash
        p1hp -= 25
        slashCrit = random.randint(1, 3)
        if slashCrit == 3:
            slash = int(slash * 1.5)
            print(f"Crítico! {p1} usou Slash e deu {slash} de dano! Derrubou o inimigo!")
            print("-------------------------------------------------------------")  
            skipEnemy = True
            wait()
            clear()
            print("-------------------------TURNO EXTRA!------------------------")
            p1menu()
        else:
            print(f"{p1} usou Slash e deu {slash} de dano!")
            print("-------------------------------------------------------------")
            wait()
            clear()
    elif p1ability == 6:
        p1sp -= 6
        p1block = True
        print(f"Protegeu {p2}! Dano será dividido entre os dois.")
        print("-------------------------------------------------------------")
        wait()
        clear()
    elif p1ability == 7:
        fire = random.randint(8, 32) + p1atk
        enemyhp -= fire
        p1sp -= 8
        print(f"{p1} usou Fire e deu {fire} de dano!")
        p1Apply = random.randint(1, 3)
        if p1Apply == 3:
            burn()
        else:
            print("-------------------------------------------------------------")
            wait()
            clear()
    elif p1ability == 8:
        clear()
        p1menu()

def p1cards():
    global p1atkBonus, p1defBonus, p1slashBonus, lifeSteal, ult, p1, p1sp, p1hp
    print("------------------{p1} - UPGRADE-----------------")
    print("[1] ATK++  |  Aumenta seu ataque.")
    print("[2] DEF++  |  Aumenta sua defesa.")
    print("[3] FIS++  |  Aprimora seus ataques físicos, a custo de HP.")
    if turns >= 9:
        options = [1, 2, 3, 4, 5]
        print("[5] ULT    |  Desbloqueia seu potencial e adiciona 20% de carga.")
    elif turns >= 6:
        options = [1, 2, 3, 4]
        print("[4] STEAL  |  Desbloqueia a habilidade Life Steal.")
    else:
        options = [1, 2, 3]
    try:
        p1upgrade = int(input("Escolha seu upgrade: "))
    except ValueError:
        p1upgrade = 0
    while p1upgrade not in options:
        p1upgrade = int(input("Escolha um upgrade válido: "))
    if p1upgrade == 1:
        print("Aumentou ataque por 3. Restaurou 5 SP.")
        print("------------------------------------")
        wait()
        clear()
        p1atkBonus += 3
        p1sp += 5
    elif p2upgrade == 2:
        print("Aumentou defesa por 2. Restaurou 5 SP.")
        print("------------------------------------")
        wait()
        clear()
        p1defBonus += 2
        p1sp += 5


def p2menu():
    global p1hp, p1sp, p1atk, p2hp, p2sp, enemyhp, skipP1, skipP2, skipEnemy
    if p2hp <= 0:
        return
    p2stats()
    if skipP2:
        print(f"{p2} não pode se mexer!")
        skipP2 = False
        wait()
        clear()
        return
    print(f"------------------------{p2} - Ações--------------------------")
    print("[1] Atacar - Ataque básico com baixa chance de Distresse")
    print("[2] Magia - Menu de feitiços")
    print("[3] Defender - Restora SP e reduz dano tomado")
    try:
        p2action = int(input("O que fazer: "))
    except ValueError:
        p2action = 0
    while p2action not in [1, 2, 3]:
        try:
            p2action = int(input("Escolha uma ação válida: "))
        except ValueError:
            p2action = 0
    if p2action == 1:
        p2dmg = random.randint(4, 16) + p2atk
        enemyhp -= p2dmg
        print(f"{p2} atacou e deu {p2dmg} de dano!")
        p2Distress = random.randint(1, 6)
        if p2Distress == 6:
            distress()
        else:
            print("-------------------------------------------------------------")
            wait()
            clear()
    elif p2action == 2:
        clear()
        p2magic()
    elif p2action == 3:
        p2sp += 15
        p2Defend = True
        print(f"{p2} defendeu e recuperou 15 SP!")
        print("-------------------------------------------------------------")
        wait()
        clear()

def p2magic():
    global p1hp, p1sp, p1atk, p2hp, p2sp, enemyhp, heal, skipP1, skipP2, p1, p2
    p2stats()
    print(f"------------------------{p2} - Magia--------------------------")
    print("[5] Ice - Ataque de gelo com média chance de Freeze (9 SP)")
    print(f"[6] Pray - Restaura {heal} HP para o jogador de escolha (10 SP)")
    print("[7] Motivate - Aumenta a defesa e dobra o dano do próximo ataque do jogador de escolha (15 SP)")
    print("[8] Voltar")
    try:
        p2action = int(input("O que fazer: "))
    except ValueError:
        p2action = 0
    while p2action not in [5, 6, 7, 8]:
        try:
            p2action = int(input("Escolha ação válida: "))
        except ValueError:
            p2action = 0
    if p2action == 5:
        ice = random.randint(8, 36) + p2atk
        enemyhp -= ice
        p2sp -= 9
        print(f"{p2} usou Ice e deu {ice} de dano!")
        print("-------------------------------------------------------------")
        wait()
        clear()
    elif p2action == 6:
        pray()
    elif p2action == 7:
        motivate()
    elif p2action == 8:
        clear()
        p2menu()



def enemyActions():
    global p1hp, p1sp, p2hp, p2sp, enemyhp, p1target, p2target, skipEnemy, skipP1, skipP2, playerChoice, p1block
    global p1MotivateDEF, p2MotivateDEF
    if p1hp <= 0 and p2hp <= 0:
        return
    if skipEnemy:
        print("O inimigo não pode se mexer!")
        skipEnemy = False
        wait()
        clear()
        return
    
    if p1hp > 0 and p2hp > 0:
        playerTarget = random.randint(1, 2)
    elif p1hp > 0:
        playerTarget = 1
    else:
        playerTarget = 2

    enemyChoice = random.randint(1, 2)
    if enemyChoice == 1:
        if playerTarget == 1:
            enemyatk = random.randint(7, 28) + p1target
            if p1MotivateDEF == True:
                enemyatk //= 2
                print(f"O inimigo atacou {p1} e deu {enemyatk} de dano!")
                p1MotivateDEF == False
                wait()
                clear()
            else:
                p1hp -= enemyatk
                print(f"O inimigo atacou {p1} e deu {enemyatk} de dano!")
                wait()
                clear()
        elif playerTarget == 2:
            enemyatk = random.randint(7, 28) + p2target
            if p1block:
                p1absorb = enemyatk // 2
                enemyatk -= p1absorb
                p1hp -= p1absorb
                print(f"{p1} bloqueou e absorveu {p1absorb} do dano!")
                p1block = False
            if p2MotivateDEF == True:
                enemyatk //= 2
                print(f"O inimigo atacou {p2} e deu {enemyatk} de dano!")
                p2MotivateDEF = False
                wait()
                clear()
            else:
                p2hp -= enemyatk
                print(f"O inimigo atacou {p2} e deu {enemyatk} de dano!")
                wait()
                clear()
    elif enemyChoice == 2:
        enemySpell = random.randint(1, 3)
        if enemySpell == 1:
            if playerTarget == 1:
                enemyFire = random.randint(10, 36) + p1target
                if p1MotivateDEF == True:
                    enemyFire //= 2
                    p1hp -= enemyIce
                    print(f"O inimigo usou fogo contra {p1}! Tomou {enemyFire} de dano.")
                    p1MotivateDEF = False
                else:
                    p1hp -= enemyFire
                    print(f"O inimigo usou fogo contra {p1}! Tomou {enemyFire} de dano.")
            elif playerTarget == 2:
                enemyFire = random.randint(10, 36) + p2target
                if p2MotivateDEF == True:
                    enemyFire //= 2
                    p2hp -= enemyIce
                    print(f"O inimigo usou fogo contra {p2}! Tomou {enemyFire} de dano.")
                    p2MotivateDEF = False
                else:
                    p2hp -= enemyFire
                    print(f"O inimigo usou fogo contra {p2}! Tomou {enemyFire} de dano.")
                enemyBurn = random.randint(1, 4)
                if enemyBurn == 4:
                    p2Burn()
                    wait()
                    clear()
                else:
                    wait()
                    clear()
        elif enemySpell == 2:
            if playerTarget == 1:
                enemyIce = random.randint(8, 30) + p1target
                if p1MotivateDEF == True:
                    enemyIce //= 2
                    p1hp -= enemyIce
                    print(f"O inimigo usou gelo contra {p1}! Tomou {enemyIce} de dano.")
                    p1MotivateDEF = False
                else:
                    p2hp -= enemyIce
                    print(f"O inimigo usou gelo contra {p2}! Tomou {enemyIce} de dano.")
                p1hp -= enemyIce
                print(f"O inimigo usou gelo contra {p1}! Tomou {enemyIce} de dano.")
                enemyFreeze = random.randint(1, 3)
                if enemyFreeze == 3:
                    skipP1 = True
                    time.sleep(2)
                    print(f"Congelou! {p1} não pode se mexer!")
                    wait()
                    clear()
                else:
                    wait()
                    clear()
            elif playerTarget == 2:
                enemyIce = random.randint(8, 30) + p2target
                if p2MotivateDEF == True:
                    enemyIce //= 2
                    p2hp -= enemyIce
                    print(f"O inimigo usou gelo contra {p2}! Tomou {enemyIce} de dano.")
                    p2MotivateDEF = False
                else:
                    p2hp -= enemyIce
                    print(f"O inimigo usou gelo contra {p2}! Tomou {enemyIce} de dano.")
                enemyFreeze = random.randint(1, 3)
                if enemyFreeze == 3:
                    skipP2 = True
                    time.sleep(2)
                    print(f"Congelou! {p2} não pode se mexer!")
                    wait()
                    clear()
                else:
                    wait()
                    clear()
        elif enemySpell == 3:
            enemyhp += 30
            print("O inimigo se curou com 30 HP.")
            wait()
            clear()


print("-----------------------------------")
print("        Batalha iniciada!")
print("-----------------------------------")
wait()
clear()

while (p1hp > 0 or p2hp > 0) and enemyhp > 0:
    if p1hp > 0:
        p1menu()
    if enemyhp <= 0:
        break
    if p2hp > 0:
        p2menu()
    if enemyhp <= 0:
        break
    enemyActions()
    turns += 1

if p1hp <= 0 and p2hp <= 0:
    print("Os jogadores perderam... womp womp")
    print(f"Total de turnos: {turns}")
elif enemyhp <= 0:
    print("Os jogadores venceram! yippie!")
    print(f"Total de turnos: {turns}")
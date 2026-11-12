# bibliotecas
import time
import os
import random

# estatisticas
hp = 100
sp = 40
enemyhp = 250

# variaveis de modificadores e upgrades
enemyAttack = 0
playerAttack = 0
fire = 0
ice = 0
heal = 20
enemyFire = 0
enemyIce = 0
turns = 0
spGain = 2
action = 0

skipPlayer = False
skipEnemy = False

print("-----------------------------------")
print("        Batalha iniciada!")
print("-----------------------------------")
time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')


def stats():
    print("-----------------------------------")
    print(f"HP Atual: {hp}/100")
    print(f"SP Atual: {sp}/40")
    print(f"HP do Inimigo: {enemyhp}/250")
    print("-----------------------------------")

def enemyActions():
    global hp, enemyhp, enemyAttack, enemyFire, enemyIce, skipEnemy, skipPlayer, action
    if skipEnemy:
        print("O inimigo não pode se mexer!")
        skipEnemy = False
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        return
    enemyAction = random.randint(1, 2)
    if enemyAction == 1:
        dano = max(0, random.randint(6, 24) + enemyAttack)
        if action == 2:
            dano = dano // 2
            hp -= dano
            print("------------------------------------------")
            print(f"O inimigo atacou e deu {dano} de dano!")
            time.sleep(2)
        else:
            hp -= dano
            print("------------------------------------------")
            print(f"O inimigo atacou e deu {dano} de dano!")
            time.sleep(2)
    elif enemyAction == 2:
        enemySpell = random.randint(1, 3)
        if enemySpell == 1:
            danoFogo = max(0, random.randint(16, 32) + enemyFire)
            if action == 2:
                danoFogo = danoFogo // 2
                hp -= danoFogo
                print("------------------------------------------")
                print(f"O inimigo usou um ataque de fogo e deu {danoFogo} de dano!")
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                hp -= danoFogo
                print("------------------------------------------")
                print(f"O inimigo usou um ataque de fogo e deu {danoFogo} de dano!")
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
        elif enemySpell == 2:
            danoGelo = max(0, random.randint(12, 24) + enemyIce)
            enemyFreeze = random.randint(1, 5)
            if action == 2:
                danoGelo = danoGelo // 2
                hp -= danoGelo
                print("------------------------------------------")
                print(f"O inimigo usou um ataque de gelo e deu {danoGelo} de dano!")
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                hp -= danoGelo
                print("------------------------------------------")
                print(f"O inimigo usou um ataque de gelo e deu {danoGelo} de dano!")
            if enemyFreeze == 5:
                print("Você foi congelado!")
                skipPlayer = True
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
        elif enemySpell == 3:
            enemyhp += 15
            if enemyhp > 250:
                enemyhp = 250
            print("------------------------------------------")
            print("O inimigo se curou com 15HP!")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')

def playerMagic():
    global hp, sp, enemyhp, fire, ice, heal, skipEnemy, skipPlayer, playerAttack
    print("[1] Fire - Dano de fogo (7 SP)")
    print("[2] Ice  - Dano de gelo com chance baixa de congelar (9 SP)")
    print("[3] Pray - Recupera HP. (10 SP)")
    print("[4] Slash - Ataque físico com alta chance de crítico (15 HP)")
    print("[5] Voltar")
    spell = 0
    try:
        spell = int(input("Qual magia usar: "))
    except ValueError:
        pass
    while spell not in [1, 2, 3, 4, 5]:
        try:
            spell = int(input("Escolha uma magia válida: "))
        except ValueError:
            pass
    if spell == 1:
        if sp < 7:
            print("SP Insuficiente.")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            playerActions()
        else:
            danoFogo = random.randint(15, 35) + fire
            print(f"Você deu {danoFogo} de dano de fogo.")
            sp -= 7
            enemyhp -= danoFogo
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
    elif spell == 2:
        if sp < 9:
            print("SP Insuficiente.")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            playerActions()
        else:
            danoGelo = random.randint(10, 30) + ice
            freeze = random.randint(1, 5)
            sp -= 9
            print(f"Você deu {danoGelo} de dano de gelo.")
            enemyhp -= danoGelo
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            if freeze == 5:
                print("Congelou o inimigo!")
                skipEnemy = True
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
    elif spell == 3:
        if sp < 10:
            print("SP Insuficiente.")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            playerActions()
        else:
            sp -= 10
            hp += heal
            if hp > 100:
                hp = 100
                print(f"Curou-se com {heal} hp. Vida máxima atingida!")
            else:
                print(f"Curou-se com {heal} hp.")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
    elif spell == 4:
        if hp <= 15:
            print("HP Insuficiente.")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            playerActions()
        else:
            danoCorte = random.randint(10, 38) + playerAttack
            crit = random.randint(1, 4)
            if crit == 4:
                danoCorte = int(danoCorte * 1.5)
                print(f"Crítico! Seu ataque deu {danoCorte} de dano e derrubou o inimigo!")
                enemyhp -= danoCorte
                hp -= 15
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                skipEnemy = True
            else:
                print(f"Seu ataque deu {danoCorte} de dano!")
                enemyhp -= danoCorte
                hp -= 15
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
    elif spell == 5:
        playerActions()

def playerActions():
    global hp, sp, enemyhp, enemyAttack, playerAttack, skipEnemy, skipPlayer, action
    if skipPlayer:
        print("Você não pode se mexer!")
        skipPlayer = False
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        return
    print("[1] Atacar")
    print("[2] Defender (Restora SP)")
    print("[3] Habilidades")
    try:
        action = int(input("Sua ação: "))
    except ValueError:
        pass
    while action not in [1, 2, 3]:
        try:
            action = int(input("Selecione ação válida: "))
        except ValueError:
            pass
    if action == 1:
        danoFisico = random.randint(5, 27) + playerAttack
        crit = random.randint(1, 7)
        if crit == 7:
            danoFisico = int(danoFisico * 1.5)
            print(f"Crítico! Seu ataque deu {danoFisico} de dano e derrubou o inimigo!")
            skipEnemy = True
        else:
            print(f"Seu ataque deu {danoFisico} de dano!")
        enemyhp -= danoFisico
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
    elif action == 2:
        print(f"Defendeu! Dano tomado sera reduzido por 50%.")
        print(f"Restaurou {spGain} SP.")
        sp += spGain
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
    elif action == 3:
        playerMagic()

def playerCards():
    global hp, enemyhp, playerAttack, enemyAttack, fire, ice, heal, enemyFire, enemyIce, sp, spGain
    print("-----------------UPGRADE-----------------")
    print("[1] ATK++ = Aprimora seu ataque físico em 4. Diminui magia em 2.")
    print("[2] MAG++ = Aprimora sua magia em 4. Diminui ataque base em 2.")
    print("[3] DEF++ = Aprimora sua defesa em 3.")
    print("[4] ENG++ = Aprimora ganho de SP quando defendendo.")
    print("-----------------------------------------")
    upgrade = 0
    try:
        upgrade = int(input("Escolha seu upgrade: "))
    except ValueError:
        pass
    while upgrade not in [1, 2, 3, 4]:
        try:
            upgrade = int(input("Escolha um número válido: "))
        except ValueError:
            pass
    if upgrade == 1:
        print("Recebeu +4 de ataque físico e -2 em magia.")
        playerAttack += 4
        fire -= 2
        ice -= 2
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
    elif upgrade == 2:
        print("Magia recebeu aumento de +4. Ataque base reduzido por -2.")
        playerAttack -= 2
        fire += 4
        ice += 4
        heal += 4
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
    elif upgrade == 3:
        print("Defesa aumentada por +3.")
        enemyAttack -= 3
        enemyFire -= 3
        enemyIce -= 3
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
    elif upgrade == 4:
        print("Ganho de SP aumentando por 2.")
        spGain += 2


# o jogo
while hp > 0 and enemyhp > 0:
    stats()
    playerActions()
    if enemyhp <= 0:
        break
    enemyActions()
    turns += 1
    if turns > 0 and turns % 3 == 0:
        playerCards()

if hp <= 0:
    print(f"Você perdeu. womp womp. Total de turnos: {turns}")
elif enemyhp <= 0:
    print(f"Você venceu! yippi! Total de turnos: {turns}")
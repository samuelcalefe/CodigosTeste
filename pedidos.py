# processa o pedido
import random
import time
itens = 0

# determinação de orçamento
print("------------------------")
while True:
    try:
        dinheiro = float(input("Determine quanto dinheiro tem para gastar: "))
        break
    except ValueError:
        print("Digite um valor numérico válido para o dinheiro.")

# determina o dia da semana
print("1 - Domingo | 2 - Segunda | 3 - Terça | 4 - Quarta | 5 - Quinta | 6 - Sexta | 7 - Sábado")
dia = 0
while dia not in [1, 2, 3, 4, 5, 6, 7]:
    try:
        dia = int(input("Digite qual é o dia da semana: "))
    except ValueError:
        print("Escolha um número válido.")

# determina se usuário é membro
membro = str(input("Você é um membro da lojinha? [y/n]: ")).lower()
while membro not in ["y", "n"]:
    membro = str(input("Digite y para sim e n para não: ")).lower()


while True:
    # mostra o cardapio de itens
    print("--------CARDÁPIO--------")
    print("1 - Hambúrgers   | 2 - Sucos")
    print("3 - Pastéis      | 4 - Caldos de Cana")
    print("5 - Coxinhas     | 6 - Refrigerantes")
    print("------------------------")

    # escolha de itens
    try:
        escolha = int(input("Escolha um item (ou 0 para fechar): "))
    except ValueError:
        print("Escolha um item válido.")
        continue


    # hambúrgers
    if escolha == 1:
        if dia == 4:
            print("--------QUARTA DO HAMBÚRGER--------")
            print("[1] X-Burger = R$12  | [2] X-Salada = R$17")
            print("[3] X-Tudo = R$19    | [4] X-Frango = R$18")
            try:
                burger = int(input("Escolha um hambúrger: "))
            except ValueError:
                print("Escolha um número válido.")
                continue
            while burger not in [1, 2, 3, 4]:
                try:
                    burger = int(input("Escolha um valor válido: "))
                except ValueError:
                    pass
            if burger == 1:
                sure = str(input("O X-Burger custa R$12. Confirmar? [y/n]: ")).lower()
                while sure not in ["y", "n"]:
                    sure = str(input("Digite y para sim e n para não: ")).lower()
                if sure == "y":
                    if membro == "y":
                        print("Desconto de membro! Adicionado R$9 ao pedido.")
                        time.sleep(2)
                        itens += 9
                    elif membro == "n":
                        print("Adicionado R$12 ao pedido.")
                        time.sleep(2)
                        itens += 12
            elif burger == 2:
                sure = str(input("O X-Salada custa R$17. Confirmar? [y/n]: ")).lower()
                while sure not in ["y", "n"]:
                    sure = str(input("Digite y para sim e n para não: ")).lower()
                if sure == "y":
                    if membro == "y":
                        print("Desconto de membro! Adicionado R$13 ao pedido.")
                        time.sleep(2)
                        itens += 13
                    elif membro == "n":
                        print("Adicionado R$17 ao pedido.")
                        time.sleep(2)
                        itens += 17
            elif burger == 3:
                sure = str(input("O X-Tudo custa R$19. Confirmar? [y/n]: ")).lower()
                while sure not in ["y", "n"]:
                    sure = str(input("Digite y para sim e n para não: ")).lower()
                if sure == "y":
                    if membro == "y":
                        print("Desconto de membro! Adicionado R$15 ao pedido.")
                        time.sleep(2)
                        itens += 15
                    elif membro == "n":
                        print("Adicionado R$19 ao pedido.")
                        time.sleep(2)
                        itens += 19
            elif burger == 4:
                sure = str(input("O X-Frango custa R$18. Confirmar? [y/n]: ")).lower()
                while sure not in ["y", "n"]:
                    sure = str(input("Digite y para sim e n para não: ")).lower()
                if sure == "y":
                    if membro == "y":
                        print("Desconto de membro! Adicionado R$14 ao pedido.")
                        time.sleep(2)
                        itens += 14
                    elif membro == "n":
                        print("Adicionado R$18 ao pedido.")
                        time.sleep(2)
                        itens += 18
        else:
            print("--------HAMBÚRGERS--------")
            print("[1] X-Burger = R$15  | [2] X-Salada = R$20")
            print("[3] X-Tudo = R$23    | [4] X-Frango = R$21")
            try:
                burger = int(input("Escolha um hambúrger: "))
            except ValueError:
                print("Escolha um valor válido.")
                continue
            while burger not in [1, 2, 3, 4]:
                try:
                    burger = int(input("Escolha um número válido: "))
                except ValueError:
                    pass
            if burger == 1:
                sure = str(input("O X-Burger custa R$15. Confirmar? [y/n]: ")).lower()
                while sure not in ["y", "n"]:
                    sure = str(input("Digite y para sim e n para não: ")).lower()
                if sure == "y":
                    if membro == "y":
                        print("Desconto de membro! Adicionado R$12 ao pedido.")
                        time.sleep(2)
                        itens += 12
                    elif membro == "n":
                        print("Adicionado R$15 ao pedido.")
                        time.sleep(2)
                        itens += 15
            elif burger == 2:
                sure = str(input("O X-Salada custa R$20. Confirmar? [y/n]: ")).lower()
                while sure not in ["y", "n"]:
                    sure = str(input("Digite y para sim e n para não: ")).lower()
                if sure == "y":
                    if membro == "y":
                        print("Desconto de membro! Adicionado R$16 ao pedido.")
                        time.sleep(2)
                        itens += 16
                    elif membro == "n":
                        print("Adicionado R$20 ao pedido.")
                        time.sleep(2)
                        itens += 20
            elif burger == 3:
                sure = str(input("O X-Tudo custa R$23. Confirmar? [y/n]: ")).lower()
                while sure not in ["y", "n"]:
                    sure = str(input("Digite y para sim e n para não: ")).lower()
                if sure == "y":
                    if membro == "y":
                        print("Desconto de membro! Adicionado R$19 ao pedido.")
                        time.sleep(2)
                        itens += 19
                    elif membro == "n":
                        print("Adicionado R$23 ao pedido.")
                        time.sleep(2)
                        itens += 23
            elif burger == 4:
                sure = str(input("O X-Frango custa R$21. Confirmar? [y/n]: ")).lower()
                while sure not in ["y", "n"]:
                    sure = str(input("Digite y para sim e n para não: ")).lower()
                if sure == "y":
                    if membro == "y":
                        print("Desconto de membro! Adicionado R$18 ao pedido.")
                        time.sleep(2)
                        itens += 18
                    elif membro == "n":
                        print("Adicionado R$21 ao pedido.")
                        time.sleep(2)
                        itens += 21


    # sucos
    if escolha == 2:
        print("--------SUCOS--------")
        print("[1] Laranja = R$7  | [2] Morango = R$8 ")
        print("[3] Uva = R$7      | [4] Maracujá = R$8")
        try:
            suco = int(input("Escolha o sabor do suco: "))
        except ValueError:
            print("Escolha um valor válido.")
            continue
        while suco not in [1, 2, 3, 4]:
            try:
                suco = int(input("Escolha um número válido: "))
            except ValueError:
                pass
        if suco == 1:
            sure = str(input("O Suco de Laranja custa R$7. Confirmar? [y/n]: ")).lower()
            while sure not in ["y", "n"]:
                sure = str(input("Digite y para sim e n para não: ")).lower()
            if sure == "y":
                if membro == "y":
                    print("Desconto de membro! Adicionado R$5 para o pedido.")
                    time.sleep(2)
                    itens += 5
                elif membro == "n":
                    print("Adicionado R$7 para o pedido.")
                    time.sleep(2)
                    itens += 7
        elif suco == 2:
            sure = str(input("O Suco de Morango custa R$8. Confirmar? [y/n]: ")).lower()
            while sure not in ["y", "n"]:
                sure = str(input("Digite y para sim e n para não: ")).lower()
            if sure == "y":
                if membro == "y":
                    print("Desconto de membro! Adicionado R$6 para o pedido.")
                    time.sleep(2)
                    itens += 6
                elif membro == "n":
                    print("Adicionado R$8 para o pedido.")
                    time.sleep(2)
                    itens += 8
        elif suco == 3:
            sure = str(input("O Suco de Uva custa R$7. Confirmar? [y/n]: ")).lower()
            while sure not in ["y", "n"]:
                sure = str(input("Digite y para sim e n para não: ")).lower()
            if sure == "y":
                if membro == "y":
                    print("Desconto de membro! Adicionado R$5 para o pedido.")
                    time.sleep(2)
                    itens += 5
                elif membro == "n":
                    print("Adicionado R$7 para o pedido.")
                    time.sleep(2)
                    itens += 7
        elif suco == 4:
            sure = str(input("O Suco de Maracujá custa R$8. Confirmar? [y/n]: ")).lower()
            while sure not in ["y", "n"]:
                sure = str(input("Digite y para sim e n para não: ")).lower()
            if sure == "y":
                if membro == "y":
                    print("Desconto de membro! Adicionado R$6 para o pedido.")
                    time.sleep(2)
                    itens += 6
                elif membro == "n":
                    print("Adicionado R$8 para o pedido.")
                    time.sleep(2)
                    itens += 8
    
    
    # pasteis
    if escolha == 3:
        print("--------PASTEIS--------")
        print("[1] Carne = R$9    | [2] Frango = R$9 ")
        print("[3] Pizza = R$8    | [4] Chocolate = R$11")
        try:
            pastel = int(input("Escolha um pastel: "))
        except ValueError:
            print("Escolha um valor válido.")
            continue
        while pastel not in [1, 2, 3, 4]:
            try:
                pastel = int(input("Escolha um número válido: "))
            except ValueError:
                pass
        if pastel == 1:
            sure = str(input("O Pastel de Carne custa R$9. Confirmar? [y/n]: ")).lower()
            while sure not in ["y", "n"]:
                sure = str(input("Digite y para sim e n para não: ")).lower()
            if sure == "y":
                if membro == "y":
                    print("Desconto de membro! Adicionado R$7 para o pedido.")
                    time.sleep(2)
                    itens += 7
                elif membro == "n":
                    print("Adicionado R$9 para o pedido.")
                    time.sleep(2)
                    itens += 9
        elif pastel == 2:
            sure = str(input("O Pastel de Frango custa R$9. Confirmar? [y/n]: ")).lower()
            while sure not in ["y", "n"]:
                sure = str(input("Digite y para sim e n para não: ")).lower()
            if sure == "y":
                if membro == "y":
                    print("Desconto de membro! Adicionado R$7 para o pedido.")
                    time.sleep(2)
                    itens += 7
                elif membro == "n":
                    print("Adicionado R$9 para o pedido.")
                    time.sleep(2)
                    itens += 9
        elif pastel == 3:
            sure = str(input("O Pastel de Pizza custa R$8. Confirmar? [y/n]: ")).lower()
            while sure not in ["y", "n"]:
                sure = str(input("Digite y para sim e n para não: ")).lower()
            if sure == "y":
                if membro == "y":
                    print("Desconto de membro! Adicionado R$5 para o pedido.")
                    time.sleep(2)
                    itens += 5
                elif membro == "n":
                    print("Adicionado R$8 para o pedido.")
                    time.sleep(2)
                    itens += 8
        elif pastel == 4:
            sure = str(input("O Pastel de Chocolate custa R$11. Confirmar? [y/n]: ")).lower()
            while sure not in ["y", "n"]:
                sure = str(input("Digite y para sim e n para não: ")).lower()
            if sure == "y":
                if membro == "y":
                    print("Desconto de membro! Adicionado R$9 para o pedido.")
                    time.sleep(2)
                    itens += 9
                elif membro == "n":
                    print("Adicionado R$11 para o pedido.")
                    time.sleep(2)
                    itens += 11

    # caldos de cana
    if escolha == 4:
        print("--------CALDOS DE CANA--------")
        print("[1] Abacaxi = R$9  | [2] Limão = R$9 ")
        try:
            cana = int(input("Escolha um caldo de cana: "))
        except ValueError:
            print("Escolha um valor válido.")
            continue
        while cana not in [1, 2]:
            try:
                cana = int(input("Escolha um número válido: "))
            except ValueError:
                pass
        if cana == 1:
            sure = str(input("O Caldo de Cana de Abacaxi custa R$9. Confirmar? [y/n]: ")).lower()
            while sure not in ["y", "n"]:
                sure = str(input("Digite y para sim e n para não: ")).lower()
            if sure == "y":
                if membro == "y":
                    print("Desconto de membro! Adicionado R$7 para o pedido.")
                    time.sleep(2)
                    itens += 7
                elif membro == "n":
                    print("Adicionado R$9 para o pedido.")
                    time.sleep(2)
                    itens += 9
        elif cana == 2:
            sure = str(input("O Caldo de Cana de Limão custa R$9. Confirmar? [y/n]: ")).lower()
            while sure not in ["y", "n"]:
                sure = str(input("Digite y para sim e n para não: ")).lower()
            if sure == "y":
                if membro == "y":
                    print("Desconto de membro! Adicionado R$7 para o pedido.")
                    time.sleep(2)
                    itens += 7
                elif membro == "n":
                    print("Adicionado R$9 para o pedido.")
                    time.sleep(2)
                    itens += 9

    # coxinha
    if escolha == 5:
        if dia == 6:
            print("--------SEXTA DA COXINHA--------")
            print("[1] Coxinha de Carne = R$5   | [2] Coxinha de Frango = R$5")
            print("[3] Coxinha de Pizza = R$4   | [4] Coxinha de Frango com Catupiry = R$6")
            try:
                coxinha = int(input("Escolha uma coxinha: "))
            except ValueError:
                print("Escolha um número válido.")
                continue
            while coxinha not in [1, 2, 3, 4]:
                try:
                    coxinha = int(input("Escolha um valor válido: "))
                except ValueError:
                    pass
            if coxinha == 1:
                sure = str(input("A coxinha de carne custa R$5. Confirmar? [y/n]: ")).lower()
                while sure not in ["y", "n"]:
                    sure = str(input("Digite y para sim e n para não: ")).lower()
                if sure == "y":
                    if membro == "y":
                        print("Desconto de membro! Adicionado R$3 ao pedido.")
                        time.sleep(2)
                        itens += 3
                    elif membro == "n":
                        print("Adicionado R$5 ao pedido.")
                        time.sleep(2)
                        itens += 5
            elif coxinha == 2:
                sure = str(input("A coxinha de frango custa R$5. Confirmar? [y/n]: ")).lower()
                while sure not in ["y", "n"]:
                    sure = str(input("Digite y para sim e n para não: ")).lower()
                if sure == "y":
                    if membro == "y":
                        print("Desconto de membro! Adicionado R$3 ao pedido.")
                        time.sleep(2)
                        itens += 3
                    elif membro == "n":
                        print("Adicionado R$5 ao pedido.")
                        time.sleep(2)
                        itens += 5
            elif coxinha == 3:
                sure = str(input("A coxinha de pizza custa R$4. Confirmar? [y/n]: ")).lower()
                while sure not in ["y", "n"]:
                    sure = str(input("Digite y para sim e n para não: ")).lower()
                if sure == "y":
                    if membro == "y":
                        print("Desconto de membro! Adicionado R$2 ao pedido.")
                        time.sleep(2)
                        itens += 2
                    elif membro == "n":
                        print("Adicionado R$4 ao pedido.")
                        time.sleep(2)
                        itens += 4
            elif coxinha == 4:
                sure = str(input("A coxinha de frango com catupiry custa R$6. Confirmar? [y/n]: ")).lower()
                while sure not in ["y", "n"]:
                    sure = str(input("Digite y para sim e n para não: ")).lower()
                if sure == "y":
                    if membro == "y":
                        print("Desconto de membro! Adicionado R$4 ao pedido.")
                        time.sleep(2)
                        itens += 4
                    elif membro == "n":
                        print("Adicionado R$6 ao pedido.")
                        time.sleep(2)
                        itens += 6
        else:
            print("--------COXINHAS--------")
            print("[1] Coxinha de Carne = R$7   | [2] Coxinha de Frango = R$7")
            print("[3] Coxinha de Pizza = R$6   | [4] Coxinha de Frango com Catupiry = R$8")
            try:
                coxinha = int(input("Escolha uma coxinha: "))
            except ValueError:
                print("Escolha um valor válido.")
                continue
            while coxinha not in [1, 2, 3, 4]:
                try:
                    coxinha = int(input("Escolha um número válido: "))
                except ValueError:
                    pass
            if coxinha == 1:
                sure = str(input("A coxinha de carne custa R$7. Confirmar? [y/n]: ")).lower()
                while sure not in ["y", "n"]:
                    sure = str(input("Digite y para sim e n para não: ")).lower()
                if sure == "y":
                    if membro == "y":
                        print("Desconto de membro! Adicionado R$5 ao pedido.")
                        time.sleep(2)
                        itens += 5
                    elif membro == "n":
                        print("Adicionado R$7 ao pedido.")
                        time.sleep(2)
                        itens += 7
            elif coxinha == 2:
                sure = str(input("A coxinha de frango custa R$7. Confirmar? [y/n]: ")).lower()
                while sure not in ["y", "n"]:
                    sure = str(input("Digite y para sim e n para não: ")).lower()
                if sure == "y":
                    if membro == "y":
                        print("Desconto de membro! Adicionado R$5 ao pedido.")
                        time.sleep(2)
                        itens += 5
                    elif membro == "n":
                        print("Adicionado R$20 ao pedido.")
                        time.sleep(2)
                        itens += 7
            elif coxinha == 3:
                sure = str(input("A coxinha de pizza custa R$6. Confirmar? [y/n]: ")).lower()
                while sure not in ["y", "n"]:
                    sure = str(input("Digite y para sim e n para não: ")).lower()
                if sure == "y":
                    if membro == "y":
                        print("Desconto de membro! Adicionado R$4 ao pedido.")
                        time.sleep(2)
                        itens += 4
                    elif membro == "n":
                        print("Adicionado R$6 ao pedido.")
                        time.sleep(2)
                        itens += 6
            elif coxinha == 4:
                sure = str(input("A coxinha de frango com catupiry custa R$8. Confirmar? [y/n]: ")).lower()
                while sure not in ["y", "n"]:
                    sure = str(input("Digite y para sim e n para não: ")).lower()
                if sure == "y":
                    if membro == "y":
                        print("Desconto de membro! Adicionado R$6 ao pedido.")
                        time.sleep(2)
                        itens += 6
                    elif membro == "n":
                        print("Adicionado R$8 ao pedido.")
                        time.sleep(2)
                        itens += 8
            

    # refrigerantes
    if escolha == 6:
            print("--------REFRIGERANTES--------")
            print("[1] Coca-Cola = R$6  | [2] Fanta = R$5")
            print("[3] Pepsi = R$5      | [4] Guaraná = R$4")
            try:
                refri = int(input("Escolha um refrigerante: "))
            except ValueError:
                print("Escolha um valor válido.")
                continue
            while refri not in [1, 2, 3, 4]:
                try:
                    refri = int(input("Escolha um número válido: "))
                except ValueError:
                    pass
            if refri == 1:
                sure = str(input("A Coca-Cola custa R$6. Confirmar? [y/n]: ")).lower()
                while sure not in ["y", "n"]:
                    sure = str(input("Digite y para sim e n para não: ")).lower()
                if sure == "y":
                    if membro == "y":
                        print("Desconto de membro! Adicionado R$4 ao pedido.")
                        time.sleep(2)
                        itens += 4
                    elif membro == "n":
                        print("Adicionado R$6 ao pedido.")
                        time.sleep(2)
                        itens += 6
            elif refri == 2:
                sure = str(input("A Fanta custa R$5. Confirmar? [y/n]: ")).lower()
                while sure not in ["y", "n"]:
                    sure = str(input("Digite y para sim e n para não: ")).lower()
                if sure == "y":
                    if membro == "y":
                        print("Desconto de membro! Adicionado R$3 ao pedido.")
                        time.sleep(2)
                        itens += 3
                    elif membro == "n":
                        print("Adicionado R$5 ao pedido.")
                        time.sleep(2)
                        itens += 5
            elif refri == 3:
                sure = str(input("A Pepsi custa R$5. Confirmar? [y/n]: ")).lower()
                while sure not in ["y", "n"]:
                    sure = str(input("Digite y para sim e n para não: ")).lower()
                if sure == "y":
                    if membro == "y":
                        print("Desconto de membro! Adicionado R$3 ao pedido.")
                        time.sleep(2)
                        itens += 3
                    elif membro == "n":
                        print("Adicionado R$5 ao pedido.")
                        time.sleep(2)
                        itens += 5
            elif coxinha == 4:
                sure = str(input("O Guaraná custa R$4. Confirmar? [y/n]: ")).lower()
                while sure not in ["y", "n"]:
                    sure = str(input("Digite y para sim e n para não: ")).lower()
                if sure == "y":
                    if membro == "y":
                        print("Desconto de membro! Adicionado R$2 ao pedido.")
                        time.sleep(2)
                        itens += 2
                    elif membro == "n":
                        print("Adicionado R$4 ao pedido.")
                        time.sleep(2)
                        itens += 4

    # pede se usuario deseja escolher outro item
    again = str(input("Escolher outro item? [y/n]: ")).lower()
    while again not in ["y", "n"]:
        again = str(input("Digite y para sim e n para não: ")).lower()
        
    # se nao, mostra a tela de confirmação
    if again == "n":
        print("------------------------")
        confirm = str(input(f"Seu pedido final custou R${itens}. Confirmar? [y/n]: ")).lower()
        while confirm not in ["y", "n"]:
            confirm = str(input("Digite y para sim e n para não: ")).lower()
        if confirm == "y":
            # olha se a pessoa tem dinheiro suficiente e determina o cargo dela
            if itens < dinheiro:
                print("Pedido registrado.")
                pedido = random.randint(1,50)
                cargo = str(input("Você é um funcionário ou cliente?[f/c]: ")).lower()
                while cargo not in ["f", "c"]:
                     cargo = str(input("Digite f para funcionário e c para cliente: ")).lower()
                if cargo == "c":
                    print("[1] Débito | [2] Crédito | [3] Pix")
                    try:
                        pagamento = int(input("Escolha forma de pagamento: "))
                    except ValueError:
                        pass
                    while pagamento not in [1, 2, 3]:
                        pagamento = int(input("Escolha uma forma válida: "))
                    if pagamento == 1:
                        print("Débito selecionado.")
                        print(f"Você gastou R${itens} e seu saldo restante é R${dinheiro - itens}")
                        break
                    elif pagamento == 2:
                        print("Crédito selecionado.")
                        print(f"Você gastou R${itens} e seu saldo restante é R${dinheiro - itens}")
                        break
                    elif pagamento == 3:
                        print("Pix selecionado.")
                        print(f"Você gastou R${itens} e seu saldo restante é R${dinheiro - itens}")
                        break

                elif cargo == "f":
                    print(f"O código do pedido é {pedido} e o total foi R${itens}.")
                    break
            elif itens > dinheiro:
                print("Saldo insuficiente.")
                break         
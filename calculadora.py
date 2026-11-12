while True:

    # inserting values
    print("---------------------------------------------------")
    num1 = float(input("1º Número: "))
    print("\nAdição = + | Subtração = - | Multiplicação = * | Divisão = / | Potenciação = ^")
    op = str(input("Operação: "))

    # check for invalid inputs
    while op not in ["+", "-",  "*", "/", "^"]:
        op = str(input("Digite uma operação válida: "))
    
    num2 = float(input("\n2º Número: "))

    # addition
    if op == "+":
        add = num1 + num2
        print(f"{num1} + {num2} = {add}")

    # subtraction
    elif op == "-":
        sub = num1 - num2
        print(f"\n{num1} - {num2} = {sub}")

    # multiplication
    elif op == "*":
        mul = num1 * num2
        print(f"\n{num1} x {num2} = {mul}")

    # division
    elif op == "/":
        if num2 == 0:
            print("\nImpossível dividir por 0.")   
        else:
            div = num1 / num2
            print(f"\n{num1} ÷ {num2} = {div}")

    # potentiation
    elif op == "^":
        pot = num1 ** num2
        print(f"\n{num1} ^ {num2} = {pot}")
    
    # run another calculation if prompted
    print("---------------------------------------------------")
    again = str(input("Fazer outro cálculo? [y/n]: ")).lower()
    while again not in ["y", "n"]:
        again = str(input("Digite y para sim e n para não: "))
    if again == "n":
        print("Entendido. Obrigado!")
        break
        
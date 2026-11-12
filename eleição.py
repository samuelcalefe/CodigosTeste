# registro de candidatos
lula = 0
bolsonaro = 0
renan = 0

# inserção de dados
while True:

    print("---------------Eleição---------------")
    print("Bolsonaro = 22 | Lula = 13 | Renan = 14")

    voto = int(input("Digite o seu voto: "))
    while voto not in [22, 13, 14]:
        voto = int(input("Selecione um candidato valido: "))

    # contagem de dados
    if voto == 22:
        print("Voto selecionado para Bolsonaro")
        bolsonaro += 1
    elif voto == 13:
        print("Voto selecionado para Lula")
        lula += 1
    elif voto == 14:
        print("Voto selecionado para Renan")
        renan += 1

    # loop
    print("-------------------------------------")
    again = str(input("Votar denovo? [y/n]: ")).lower()
    while again not in ["y", "n"]:
        again = str(input("Selecione y para sim e n para não: "))
    
    # encerra o loop e mostra os resultados
    if again == "n":
        print("-------------------------------------")
        print(f"Votos no Bolsonaro: {bolsonaro}")
        print(f"Votos no Lula: {lula}")
        print(f"Votos no Renan: {renan}")
        break

print("-------------------------------------")
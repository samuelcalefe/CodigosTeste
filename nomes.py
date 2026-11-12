samuel = 0

for nomes in range (1, 10, 1):
    nomes = input("digite seu nome: ")
    if nomes == "samuel":
        samuel += 1
    
print(f"a quantidade de samuels é {samuel}")
print(f"a quantidade de nomes é {nomes}")
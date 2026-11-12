player1 = {
    "p1": str(input("Digite nome do 1º jogador: ")),
    "p1hp": 100,
    "p1MaxHP": 100
    }

player2 = {
    "p2": str(input("Digite nome do 2º jogador: ")),
    "p2hp": 80,
    "p2MaxHP": 80
    }
print(player1["p1"],"'s hp: ", player1["p1hp"],"/", player1["p1MaxHP"], sep="")
print(player2["p2"],"'s hp: ", player2["p2hp"],"/", player2["p2MaxHP"], sep="")
numjogadores=int(input("Digite o número de jogadores"))
soma_altura=0
for i in range(numjogadores):
    alturajogadores=float(input("Escreva a altura dos jogadores"))
soma_altura+=alturajogadores
print("A média de altura dos jogadores é:" ,soma_altura/numjogadores)
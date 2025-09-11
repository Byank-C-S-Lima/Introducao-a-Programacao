numjogadores=int(input("Digite o número de jogadores"))
soma_altura=0
i=0
while i<numjogadores:
    if i<numjogadores:
        altura=float(input("Digite a altura do jpgador em cm:"))
        soma_altura+=altura
    i+=1
mediaaltura=(soma_altura)/numjogadores
print("A média de altura dos jogadores é:" ,mediaaltura)
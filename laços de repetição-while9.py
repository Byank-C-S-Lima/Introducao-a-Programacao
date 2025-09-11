numero=int(input("Digite um número:"))
cont=0
i=1
while i<=numero:
    if numero%i==0:
        cont+=1
    i+=1
if cont==2:
    print("O número",numero,"é primo")
else:
    print("O número",numero,"não é primo")

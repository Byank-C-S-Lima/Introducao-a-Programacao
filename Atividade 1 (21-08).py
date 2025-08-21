somaValor=0
contNegativo=0
for i in range(20):
    valor=int(input("Digite o valor:"))
    if valor>=0:
        somaValor+=valor
    else:
        contNegativo+1
print("A soma dos valores positivos é:",somaValor)
print("A quantidade de valores negativos é",contNegativo)
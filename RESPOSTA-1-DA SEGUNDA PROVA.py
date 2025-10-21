numero=int(input("Digite um numero:"))
resto=0
resultado=0
while(numero%10!=0):
    resto=numero%10
    resultado=resultado+resto
    numero=numero//10
print(resultado)
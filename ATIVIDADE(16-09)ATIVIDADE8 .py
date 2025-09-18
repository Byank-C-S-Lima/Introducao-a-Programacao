print("**********OPERAÇÕES MATEMÁTICAS**********")
print("Escolha uma das opções abaixo. Para encerrar digite sair!!!")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - par ou ímpar")
print("6 - primo")
print("7 - fatorial")
print("1 - soma\n2 - subtração\n3 - multiplicação\n4 - divisão\n5 - par ou ímpar\n6 - primo\n7 - fatorial\nsair - encerrar o programa")
opção = input("Digite a opção desejada ou sair para encerrar: ")
opçãoMaiusc= opção.upper()
while opçãoMaiusc != "SAIR":
    if opção == "1":
        numero1=int(input("Digite o primeiro valor: "))
        numero2=int(input("Digite o segundo valor: "))
        print("O resultado da soma entre ",numero1,"e",numero2,"é",numero1+numero2,".")
    if opção == "2":
        numero1=int(input("Digite o primeiro valor: "))
        numero2=int(input("Digite o segundo valor: "))
        print("O resultado da subtração entre ",numero1,"e",numero2,"é",numero1-numero2,".")
    if opção == "3":
        numero1=int(input("Digite o primeiro valor: "))
        numero2=int(input("Digite o segundo valor: "))
        print("O resultado da multiplicação entre ",numero1,"e",numero2,"é",numero1*numero2,".")
    if opção == "4":
        numero1=int(input("Digite o primeiro valor: "))
        numero2=int(input("Digite o segundo valor: "))
        if numero2 == 0:
            print("O resultado da divisão entre ",numero1,"e",numero2,"é",numero1/numero2,".")
    if opção == "5":
        numero=int(input("Digite o numero para saber se ele é ímpar ou par:"))
        if numero%2==0:
            print("O número",numero,"é par!!!")
        else:
            print("O número",numero,"é ímpar!!!")
    input("Pressione ENTER para voltar a OPERAÇÕES MATEMÁTICAS!")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - par ou ímpar")
print("6 - primo")
print("7 - fatorial")

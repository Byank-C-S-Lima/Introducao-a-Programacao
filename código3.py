quantidade = int(input("Quantas temperaturas serão analisadas? "))

# Ler a primeira temperatura antes do for
primeira = float(input("Digite a temperatura: "))

maior = primeira
menor = primeira
soma = primeira
acima_30 = 0
abaixo_15 = 0

# Contar se a primeira está nos limites
if primeira > 30:
    acima_30 = acima_30 + 1

if primeira < 15:
    abaixo_15 = abaixo_15 + 1

# Loop para as demais temperaturas
for i in range(quantidade - 1):
    temperatura = float(input("Digite a temperatura: "))

    if temperatura > maior:
        maior = temperatura

    if temperatura < menor:
        menor = temperatura

    soma = soma + temperatura

    if temperatura > 30:
        acima_30 = acima_30 + 1

    if temperatura < 15:
        abaixo_15 = abaixo_15 + 1

media = soma / quantidade

print("Maior temperatura:", maior)
print("Menor temperatura:", menor)
print("Média das temperaturas:", media)
print("Leituras acima de 30 °C:", acima_30)
print("Leituras abaixo de 15 °C:", abaixo_15)

diferenca = maior - menor

if diferenca > 20:
    print("ALERTA: Variação térmica extrema!")
else:
    print("Variação dentro do esperado.")


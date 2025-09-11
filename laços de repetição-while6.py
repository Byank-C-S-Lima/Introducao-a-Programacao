maiorMedia=0
menorMedia=9999
alunosRep=0
alunosAp=0
i=0
while i<10:
    N1= float(input("Digite a nota 1: "))
    N2= float(input("Digite a nota 2: "))
    N3= float(input("Digite a nota 3: "))
    medAluno= (N1+N2+N3)/3
    if medAluno>maiorMedia:
        maiorMedia=medAluno
    if medAluno<menorMedia:
        menorMedia=medAluno
    if medAluno>=6:
        alunosAp+=1
    else: alunosRep+=1
    i+=1
print("A maior média é: ", maiorMedia)
print("A menor média é ", menorMedia)
print("A quantidade de alunos aprovados é: ", alunosAp)
print("A quantidade de alunos reprovados é ", alunosRep)
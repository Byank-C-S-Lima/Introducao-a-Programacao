bateria=int(input("Digite o nível de bateria:"))
temperatura=int(input("Digite a temperatura:"))
umidade=int(input("Digite a umidade do solo:"))
modo=input("Digite um modo de operação (plantio, colheita ou irrigação):")
if bateria<20:
    print("Bateria muito baixa! Retorne imediatamente para a base.")
if bateria >=20:
    if bateria  <50:
        print("Atenção: Bateria em nível moderado")
if bateria >=50:
    print("Bateria suficiente para operação.")
if temperatura>40:
    print("Temperatura crítica! Operação suspensa.")
if temperatura<=5:
    print("Frio extremo! Modo de economia ativado.")
if umidade<30:
    print("Solo muito seco! Recomendo iniciar irrigação.") 
if umidade>80:
    print("Solo encharcado! Suspenda irrigação imediatamente.")
if modo=="plantio":
    print("Iniciando modo de PLANTIO.")
if modo=="colheita":
    print("Iniciando modo de COLHEITA.")
if modo=="irrigação":
    print("Iniciando modo de IRRIGAÇÃO.")   
if bateria>=50:
    bateria_ok=1
if bateria<50:
    bateria_ok=0
if temperatura>=10:
    if temperatura<=35:
        temperatura_ok=1
if temperatura<10:
    temperatura_ok=0
if temperatura>35:
    temperatura_ok=0
if umidade>=30:
    if umidade<=80:
        umidade_ok=1
if umidade<30:
    umidade_ok=0
if umidade>80:
    umidade_ok=0
if bateria_ok==1:
    if temperatura_ok==1:
        if umidade_ok==1:
            print("Robô autorizado a iniciar a operação!")
if bateria_ok==0:
    print("Operação negada! Verifique as condiçoes do ambiente.")
if temperatura_ok==0:
    print("Operação negada! Verifique as condiçoes do ambiente.")
if umidade_ok==0:
    print("Operação negada! Verifique as condiçoes do ambiente.")

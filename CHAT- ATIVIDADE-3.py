user=input("Digite seu nome:")
senha= input("Digite sua senha:")
if user== "admin":
    print("O usuário está correto!")
    if senha=="1234":
        print("A senha está correta!")
        print("Login realizado com sucesso!")
else:
    if user!="admin":
        print("Usuário incorreto!")
        if senha!="1234":
           print("Senha incorreta!")
           print("Usuário ou senha incorretos!")
    




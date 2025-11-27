total_da_compra = 0
quantidade_de_produtos = 0
produto_mais_caro = 0

continuar_comprando = "s"

while continuar_comprando == "s":
    
    preco_do_produto = -1
    while preco_do_produto < 0:
        preco_do_produto = float(input("Preço do produto: R$ "))
        if preco_do_produto < 0:
            print("Preço inválido! Digite um valor maior ou igual a zero.")

    total_da_compra += preco_do_produto
    quantidade_de_produtos += 1

    if preco_do_produto > produto_mais_caro:
        produto_mais_caro = preco_do_produto

    continuar_comprando = ""
    while continuar_comprando != "s" and continuar_comprando != "n":
        continuar_comprando = input("Deseja adicionar outro produto? (s/n): ").lower()
        if continuar_comprando != "s" and continuar_comprando != "n":
            print("Digite apenas s ou n.")

valor_medio = total_da_compra / quantidade_de_produtos

print("\n--- Resultado ---")
print("Total da compra: R$", total_da_compra)
print("Quantidade de produtos:", quantidade_de_produtos)
print("Valor médio por produto: R$", valor_medio)
print("Produto mais caro: R$", produto_mais_caro)

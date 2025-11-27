total_da_compra = 0
quantidade_de_produtos = 0
produto_mais_caro = 0

continuar_comprando = 1

while continuar_comprando == 1:

    preco_do_produto = -1
    while preco_do_produto < 0:
        preco_do_produto = float(input("Digite o preço do produto: R$ "))
        if preco_do_produto < 0:
            print("Preço inválido! Digite um valor maior ou igual a zero.")

    total_da_compra = total_da_compra + preco_do_produto
    quantidade_de_produtos = quantidade_de_produtos + 1

    if preco_do_produto > produto_mais_caro:
        produto_mais_caro = preco_do_produto

    continuar_comprando = int(input("Deseja adicionar outro produto? (1 para continuar / 2 para parar): "))

    while continuar_comprando != 1 and continuar_comprando != 2:
        print("Resposta inválida! Digite apenas 1 ou 2.")
        continuar_comprando = int(input("Deseja adicionar outro produto? (1 para continuar / 2 para parar): "))

valor_medio_por_produto = total_da_compra / quantidade_de_produtos

print("\n--- Resultado Final ---")
print("Total da compra: R$", total_da_compra)
print("Quantidade de produtos:", quantidade_de_produtos)
print("Valor médio por produto: R$", valor_medio_por_produto)
print("Produto mais caro: R$", produto_mais_caro)

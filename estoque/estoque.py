# Dicionário contendo o estoque de produtos.
# Cada chave é o nome de um produto e cada valor é uma lista [quantidade, preço].
estoque = {
    "tomate": [1000, 2.30],
    "alface": [500, 0.45],
    "batata": [2001, 1.20],
    "feijão": [100, 1.50],
}

# Variável para armazenar o total das vendas.
total = 0

# Exibe o cabeçalho da seção de vendas.
print("Vendas:\n")

# Loop infinito para permitir a entrada contínua de produtos vendidos.
while True:
    # Solicita o nome do produto.
    produto = input("Nome do produto (fim para sair): ")
    # Se o usuário digitar "fim", o loop é interrompido.
    if produto == "fim":
        break
    # Verifica se o produto está no estoque.
    if produto in estoque:
        try:
            # Solicita a quantidade do produto vendida.
            quantidade = int(input("Quantidade: "))
            # Verifica se há quantidade suficiente no estoque.
            if quantidade <= estoque[produto][0]:
                # Obtém o preço do produto.
                preço = estoque[produto][1]
                # Calcula o custo da venda.
                custo = preço * quantidade
                # Exibe os detalhes da venda.
                print(f"{produto:12s}: {quantidade:3d} x {preço:6.2f} = {custo:6.2f}")
                # Atualiza a quantidade do produto no estoque.
                estoque[produto][0] -= quantidade
                # Adiciona o custo da venda ao total.
                total += custo
            else:
                # Mensagem de erro se a quantidade solicitada não está disponível.
                print("Quantidade solicitada não disponível")
        except ValueError:
            # Mensagem de erro se a entrada de quantidade não for um número inteiro válido.
            print("Por favor, insira um número inteiro válido para a quantidade")
    else:
        # Mensagem de erro se o nome do produto não está no estoque.
        print("Nome de produto inválido")

# Exibe o custo total das vendas.
print(f"\nCusto total: {total:6.2f}\n")

# Exibe o estoque atualizado.
print("Estoque:\n")
for chave, dados in estoque.items():
    # Exibe a descrição do produto.
    print("Descrição: ", chave)
    # Exibe a quantidade disponível no estoque.
    print("Quantidade: ", dados[0])
    # Exibe o preço do produto.
    print(f"Preço: {dados[1]:6.2f}\n")

    #Carlos Roberto
# Este programa calcula o preço total de uma compra

# Solicita informações sobre o produto ao usuário
nome_produto = input("Digite o nome do produto:" )
preco_unitario = float(input("Digite o valor do produto: "))
quantidade = int(input("Digite a quantidade de produtos:" ))

#Calculadora de preço total
preco_total = preco_unitario * quantidade

#Exibe o resultado
print(f"\nProduto: {nome_produto}")
print(f"Preco unitário: R$ {preco_unitario:.2f}")
print(f"Quantidade: {quantidade}")
print(f"Total: R$ {preco_total:.2f}")
"""

Calculadora de Preço Total

Desenvolva um programa que calcule o preço total de uma compra. Use as seguintes informações:

Nome do produto: "Cadeira Infantil"
Preço unitário: R$ 12.40
Quantidade: 3 
O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.
"""
# Definindo as variáveis
nome_produto = "Cadeira Infantil"
preco_unitario = 12.40  # em reais
quantidade = 3
# Calculando o preço total
preco_total = preco_unitario * quantidade

# Exibindo as informações
print(f"Produto: {nome_produto}")
print(f"Preço unitário: R${preco_unitario:.2f}")
print(f"Quantidade: {quantidade}")
print(f"Preço total: R${preco_total:.2f}")
# Exibindo o resultado final
print(f"O preço total da compra é: R${preco_total:.2f}")

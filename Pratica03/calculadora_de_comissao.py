"""
6- Calculadora de Comissão


Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas
efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão
sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais. 

Entrada: O arquivo de entrada contém um texto (primeiro nome do vendedor) e 2 valores de
dupla precisão (double) com duas casas decimais, representando o salário fixo do vendedor e
montante total das vendas efetuadas por este vendedor, respectivamente. 

Saída: Imprima o total que o funcionário deverá receber, conforme exemplo fornecido.

"""
#Solicita o nome do vendedor
nome = input("Digite o nome do vendedor: ")

# Solicita o salário fixo e o total de vendas
salario_fixo = float(input("Digite o salário fixo do : "))
total_vendas = float(input("Digite o total de vendas : "))

comissão = total_vendas * 0.15

salario_Total = salario_fixo + comissão

print(f"TOTAL = R$ {salario_Total:.2f}")


"""
 Calculadora de Número Inteiro
Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).

Entrada: O arquivo de entrada contém 4 valores inteiros. 
Saída: Imprima a mensagem "DIFERENCA = " com todas as letras maiúsculas.
"""
# Definindo as variáveis
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))
D = int(input("Digite o valor de D: "))
# Calculando a diferença    
print("A formula da diferença é (A * B) - (C * D)")
DIFERENCA = (A * B) - (C * D)
# Exibindo a mensagem com o resultado
print("DIFERENCA = ", end="")
print(DIFERENCA)
# Exibindo o resultado final
print(f"A diferença do produto de A e B pelo produto de C e D é: {DIFERENCA}")
# Exibindo o resultado final
print(f"O resultado final da diferença é: {DIFERENCA}")
# Exibindo o resultado final
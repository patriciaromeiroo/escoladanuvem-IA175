"""
2- Classificador de Idade
Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:
Criança (0-12 anos),
Adolescente (13-17 anos),
Adulto (18-59 anos)
Idoso (60 anos ou mais)."""

idade = int(input("Digite sua idade: "))

# Classificação da idade


if 0 <= idade <= 12:
    print("Você é uma criança")
elif 13 <= idade <= 17:
    print("Você é um Adolescente")
elif 18 <= idade <= 59:
    print("Você é um Adulto")
else:
    print("Você é um idoso")


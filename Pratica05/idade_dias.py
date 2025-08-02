"""Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento."""

def calcular_idade_em_dias(ano_nascimento, ano_atual):
    idade = ano_atual - ano_nascimento
    dias_idade = idade * 365  # Considerando anos de 365 dias
    return dias_idade

ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))
idade_em_dias = calcular_idade_em_dias(ano_nascimento, ano_atual)
print(f"A idade em dias é: {idade_em_dias} dias.")

    
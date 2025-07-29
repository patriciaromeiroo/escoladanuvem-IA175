"""
5- Verificador de Ano Bissexto
Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.
"""
#Insira o ano
ano = int(input("Digite um ano para verificar se é bissexto: "))

if ano % 4 == 0: # Se o ano é divisível por 4, ele pode ser bissexto
    if ano % 100 == 0: # Se o ano é divisível por 100, ele precisa ser analisado 
        if ano % 400 == 0:
            print(f"{ano} é um ano bissexto.")
        else:
            print(f"{ano} não é um ano bissexto.")
    else: # se o ano for divisivel por 4, mas não por 100 então ele é bissexto
        print(f"{ano} é um ano bissexto.")

else: # Se o ano não for divisível por 4, ele não é bissexto
    print(f"{ano} não é um ano bissexto.")
        
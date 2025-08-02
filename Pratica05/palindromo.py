"""Crie uma função que verifique se uma palavra ou frase é um palíndromo 
(lê-se igual de trás para frente, ignorando espaços e pontuação). 
Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.
"""

def eh_palindromo(texto):
    # Remove espaços e converte para minúsculas
    texto_limpo = ''.join(c.lower() for c in texto if c.isalnum())
    # Verifica se o texto é igual ao seu reverso
    return texto_limpo == texto_limpo[::-1]

entrada = input("Digite uma palavra ou frase: ")
if eh_palindromo(entrada):
    print("Sim, é um palíndromo.")
else:
    print("Não, não é um palíndromo.")

 




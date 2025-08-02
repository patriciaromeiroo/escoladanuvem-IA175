"""Crie um programa que gera um perfil de usuário aleatório usando a API 'Random User Generator'.
 O programa deve exibir o nome, email e país do usuário gerado.
"""



import requests

#obter um usuário aleatório da API 'Random User Generator'
def obter_usuario_aleatorio():
    url = "https://randomuser.me/api/"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        dados = response.json()['results'][0]
        nome = f"{dados['name']['first']} {dados['name']['last']}"
        email = dados['email']
        pais = dados['location']['country']
        return f"Nome: {nome}\nEmail: {email}\nPaís: {pais}"
    except requests.RequestException as e:
        print(f"Erro ao obter usuário: {e}")

print("Gerando usuário aleatório...")
usuario = obter_usuario_aleatorio()
print(usuario)

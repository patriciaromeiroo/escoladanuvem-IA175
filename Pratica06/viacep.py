"""Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário, utilizando a API ViaCEP. 
O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado.
"""

import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        dados = response.json()
        
        if 'erro' in dados:
            return "CEP não encontrado."
        
        logradouro = dados.get('logradouro', 'Não informado')
        bairro = dados.get('bairro', 'Não informado')
        cidade = dados.get('localidade', 'Não informado')
        estado = dados.get('uf', 'Não informado')
        
        return f"Logradouro: {logradouro}\nBairro: {bairro}\nCidade: {cidade}\nEstado: {estado}"
    
    except requests.RequestException as e:
        return f"Erro ao consultar CEP: {e}"
def main():
    cep = input("Digite o CEP (somente números): ").strip()
    
    if not cep.isdigit() or len(cep) != 8:
        print("CEP inválido. Deve conter 8 dígitos.")
        return
    
    resultado = consultar_cep(cep)
    print(resultado)
if __name__ == "__main__":
    main()
    

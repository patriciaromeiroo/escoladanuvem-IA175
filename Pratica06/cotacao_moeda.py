"""
Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL).
O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), 
e o programa deve exibir o valor atual, máximo e mínimo da cotação,
 além da data e hora da última atualização. 
 Utilize a API da AwesomeAPI para obter os dados de cotação.
 """


import requests
from datetime import datetime

def obter_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        dados = response.json()
        cotacao = dados[f"{moeda}BRL"]
        return f"""
        Moeda: {moeda} para BRL
        Valor: R$ {float(cotacao['bid']):.2f}
        Máximo: R$ {float(cotacao['high']):.2f}
        Mínimo: R$ {float(cotacao['low']):.2f}
        Data e Hora: {cotacao['create_date']}
        Data e Hora Atual: {datetime.fromtinestamp(int(cotacao['timestamp']))}
        """
    except requests.exceptions.RequestException as e:
        return f"Erro ao consultar a cotação: {e}"
    except KeyError:
        return f"Moeda {moeda} não encontrada ou não suportada."

        
        def main():
            moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper()
            print("\nObtendo cotação...")
            resultado = obter_cotacao(moeda)
            print(resultado)


        if __name__ == "__main__":
            main()
            
# Aplicação para calcular cotação de moedas

import requests

def obter_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
    response = requests.get(url)
    response.raise_for_status()
    dados = responde.json()
    return f"Moedas: {moeda}/BRL\n Valor: R${dados['bid']}\Maximo: R$R${dados['high']}\nMinimo: R$R${dados['low']}\n Atualização:{dados['create_date']}" 

moeda = input("Digite o código da moeda (USD, EUR): ")
print(obter_cotacao(moeda))
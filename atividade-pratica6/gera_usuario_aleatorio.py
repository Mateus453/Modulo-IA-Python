# Gerador de Usuários Aleatórios

import requests

def gerar_usuario_aleatorio():
    url = "https://randowuser.me/api"
    response = requests.get(url)
    response.raise_for_status()
    dados = response.json()['results'][0]
    nome = f"{dados['name']['first']} {dados['name']['last']}"
    email = dados['email']
    pais = dados['location']['country']
    return f"Nome: {nome}\nEmail: {email}\nPaís: {pais}"

print(gerar_usuario_aleatorio())
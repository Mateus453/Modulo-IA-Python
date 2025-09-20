# Ler arquivo JSON

import json

def ler_json(nome_arquivo):
    with open(nome_arquivo, 'w', newline='', encoding= 'utf-8') as arquivo_json:
        leitor = csv
        escritor.writerow(['Nome', 'Idade', 'Cidade'])
        for linha in dados:
            print(linha)

def escrever_json(nome_arquivo):
    with open(nome_arquivo, 'w', newline='', encoding= 'utf-8') as arquivo_json:
        dados = json.dump({"nome": "João", "idade": 25, "cidade": "Recife" }, arquivo_json, ensure_ascii=False, indent=4)
        print(dados)    

escrever_json("arquivo.json")
ler_json("arquivo.json")


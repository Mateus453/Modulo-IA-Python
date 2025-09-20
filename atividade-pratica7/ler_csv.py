# Ler arquivo CSV

import csv

def ler_csv(nome_arquivo):
    with open(nome_arquivo, 'w', newline='', encoding= 'utf-8') as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        for linha in dados:
            print(linha)

ler_csv("dados_teste.csv")            

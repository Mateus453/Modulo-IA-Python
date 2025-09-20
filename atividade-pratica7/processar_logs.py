# Processador de logs

import pandas as pd

def processar_logs(nome_arquivo):
    df = pd.read_csv(nome_arquivo)
    media_tempo = df['tempo_execução'].mean()
    desvio_padrao = df['tempo_execução'].std()
    print(f"Tempo de Execução:\nMédia: {media_tempo:.2f}\nDesvio Padrão: {desvio_padrao:.2f}")

arquivo = input("Digite o nome do arquivo: ") 
processar_logs(arquivo)

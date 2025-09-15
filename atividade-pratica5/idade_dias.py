# Aplicação para cálculo de dias vividos (sem contagem de dias bissextos)

import datetime

def calculo_idade_dias(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365 
    return idade_dias

ano_nasc = int(input("Digite o ano de nascimento: "))

idade_dias = calculo_idade_dias(ano_nasc)
print(f"Sua idade aproximada em dias é: {idade_dias} dias")

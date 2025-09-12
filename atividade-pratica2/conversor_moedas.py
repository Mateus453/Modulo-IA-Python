#Conversor de moedas com base no Real Brasileiro

valor_em_reais = float(input("Digite o valor desejado à conversão: "))

cotacao_do_dolar = 5.41
cotacao_do_euro = 6.33

#Conversão
conversao_dolares = valor_em_reais / cotacao_do_dolar
coversao_euros = valor_em_reais / cotacao_do_euro

#Exibição dos resultados 
print(f"Saldo em Reais: R$ {valor_em_reais:.2f}")
print(f"Valor em Dolares: $ {conversao_dolares}")
print(f"Valor em Euros: £ {conversao_dolares}")
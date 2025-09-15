# Calculadora de porcentagem de gorjeta

def calculo_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

total_conta = float(input("Digite o total da sua conta no restaurante: "))
porcentagem = float(input("Quantos porcentos você deseja pagar de gorjeta: "))
gorjeta = calculo_gorjeta(total_conta, porcentagem)
print(f"Para uma conta de R${total_conta:.2f}, você deseja pagar {porcentagem:.2f}% gorjeta = R$ {gorjeta:.2f} ")

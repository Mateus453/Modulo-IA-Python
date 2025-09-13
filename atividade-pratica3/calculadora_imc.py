# Calculadora para verificação de indice de massa corporal

peso = float(input("Digite o seu peso em Kg: "))
altura =  float(input("Digite a sua altura em metros: "))

imc = peso / (altura **2)

if imc < 18.5:
     classificacao = "Abaixo do peso"
elif imc > 18.5 and imc < 25:
     classificacao = "Peso normal"
elif imc > 25 and imc <= 30:
     classificacao = "Acima do peso"
else:
     classificacao = "Obeso"

print(f"Seu IMC: {imc:.1f}")
print(f"Classificação: {classificacao}")
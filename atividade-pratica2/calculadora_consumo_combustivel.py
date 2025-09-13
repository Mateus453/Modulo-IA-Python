# Calculadora de consumo de combustível 

#Dados de viagem
distancia_percorrida = int( input("Digite a distãncia percorrida em Km: "))
combustivel_gasto =  int(input("Digite a quantidade gasta de combustível em Litros: "))

# Cálculo de consumo
consumo = distancia_percorrida / combustivel_gasto

# Exibição do resultado
print("\nDados da viagem: ")
print(f"Distância Percorrida: {distancia_percorrida} km")
print(f"Combustível Gasto: {combustivel_gasto} Litro(s)")
print(f"Consumo Médio: {consumo:.2f} km/l")
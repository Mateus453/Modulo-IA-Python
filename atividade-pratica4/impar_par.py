# Aplicação para a diferenciacão de números impares e pares

def analisador_numeros():
    numeros_pares = 0
    numeros_impares = 0

    while True:
        entrada = input("Digite um número inteiro ou (sair para encerrar o programa): ")

        if entrada.lower() == 'sair':
           break 

        try:
            numero = int(entrada)
            if numero % 2 == 0:
               print("O número {numero} é par")
               numeros_pares += 1
            else:
                print(f"O número {numero} é impar")   
                numeros_impares +=1
        except ValueError:
            print("Entrada inválida! Por favor, digite um número inteiro.")
            continue
        print(f"\nResultado")
        print(f"Total de número impares: {numeros_impares}")
        print(f"Total de numeros pares: {numeros_pares}")

analisador_numeros()     
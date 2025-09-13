# Calculadora para as 4 operações fundamentais

def calculadora():
    while True:
        try:
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número: "))
            operacao = input("Digite a operação (+ - * /): ")

            if operacao == '+':
                resultado = numero1 + numero2
            elif operacao == '-':
                resultado = numero1 - numero2
            elif operacao == '*':
                resultado = numero1 * numero2
            elif operacao == '/':
                resultado = numero1 / numero2
            else:
                raise ValueError("Operação invalida")

        except ValueError as e:
            print(f"Erro: {e}. Tente novamente! ")     
        except ZeroDivisionError:
            print("Invalido: Divisão por zero não é permitida. Tente novamente!")   
        else:
            print(f"Resultado: {numero1} {operacao} {numero2} {resultado}")   

calculadora()            



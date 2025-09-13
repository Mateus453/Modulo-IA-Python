# Aplicação para a criação de uma senha segura

def verica_senha():
    while True:
        senha = input("Digite uma senha uma senha ou ('sair' para encerrar o programa): ")

        if senha.lower() == 'sair': 
            print("Programa encerrado!")
            break

        if len(senha) < 8:
            print("Por questões de segurança digite uma senha com no minimo 8 caracteres:") 
            continue

        if not any(letra.isdigit() for letra in senha):
           print("Por questões de segurança sua senha deve possuir pelo menos um número")
           continue

        print("Senha forte e válida")
        break

verica_senha()        
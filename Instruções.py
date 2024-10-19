from datetime import datetime

def calcular_idade():
    ano_atual = 2022
    
    nome = input("Digite seu nome completo: ")

    while True:
        try:
            ano_nascimento = int(input("Digite seu ano de nascimento (entre 1922 e 2021): "))
            if 1922 <= ano_nascimento <= 2021:
                break  
            else:
                print("Erro: O ano deve estar entre 1922 e 2021. Tente novamente.")
        except ValueError:
            print("Erro: Por favor, digite um número válido para o ano.")

    idade = ano_atual - ano_nascimento

    print(f"{nome}, você completou ou completará {idade} anos em {ano_atual}.")

calcular_idade()

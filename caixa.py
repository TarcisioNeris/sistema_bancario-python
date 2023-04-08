"""
 _______       _            _     _          ______        _                 _ 
(_______)     (_)       _  (_)   | |        (____  \      (_)               | |
 _______  ____ _  ___ _| |_ _  __| |_____    ____)  ) ____ _ _____ ____   __| |
|  ___  |/ ___) |/___|_   _) |/ _  | ___ |  |  __  ( / ___) (____ |  _ \ / _  |
| |   | | |   | |___ | | |_| ( (_| | ____|  | |__)  ) |   | / ___ | | | ( (_| |
|_|   |_|_|   |_(___/   \__)_|\____|_____)  |______/|_|   |_\_____|_| |_|\____|
    
Auteur: lauli(lauli.pro@gmail.com) 
caixa.py(Ɔ) 2023
Description : Saisissez la description puis « Tab »
Créé le :  samedi 8 avril 2023, 18:41:36 
Dernière modification : samedi 8 avril 2023, 18:46:08
"""
'''sitema bancario : ,desafio dio    fortr :https://github.com/digitalinnovationone/trilha-python-dio/tree/00_fundamentos/00%20-%20Fundamentos'''
menu = '''

[d] deposito
[s] sacar
[e] Extrato
[q] Sairsa
=> '''
saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor de depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f'Deposito: R$ {valor:.2f}\n'

        else:
            print('Operação falha! o valor infornado é invalido.')

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = valor > numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operaração falhou! Voc~e não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! Ovalor do saque excede o limite")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques execedido são três diario.")

        elif valor > 0:
            saldo -= valor
            extrato += f'Saques: R${valor:.2f}\n'
            numero_saques += 1

        else:
            print("Operação falhou o valor  informado é invalido.")

    elif opcao == "e":
        print("\n============ EXTRATO ===============")
        print("Não foram realizada movimentações." if not extrato else extrato)
        print(f'\nSaldo:R$ {saldo:.2f}')
        print("=======================================")

    elif opcao == "q":
        break

    else:
        print("Operação invalida, por fovor selecione novamento a operação desejado.")

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> 
"""

saldo = 0
limite = 500
extrato = ""
numeros_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu).lower()

    if opcao == 'd':
        print("Depósito")
        dep = float(input('Digite o valor que deseja depositar: '))
        if dep < 0:
            print('Operação não concluida. Valor negativo.')
        else:
            saldo += dep
            extrato += f'Depósito: R$ {dep:.2f}\n'
            print(f'Depósito de R$ {dep:.2f} efetuado com sucesso.')

    elif opcao == 's':
        print("Saque")
        if numeros_saques < LIMITE_SAQUES:
            saq = float(input('Digite o valor que deseja sacar: '))
            if saq < 0:
                print('Operação não concluida. Valor negativo')
            elif saq > saldo:
                print(f'Saldo insuficiente. O seu saldo atual é de R$ {saldo:.2f}.')
            elif saq > 500:
                print(f'Limite diário de saques ultrapassado. Digite um valor menor do que R$ {limite:.2f}.')
            else:
                saldo -= saq
                numeros_saques += 1
                extrato += f'Saque: R$ {saq:.2f}\n'
                print(f'Saque de R$ {saq:.2f} efetuado com sucesso.')
                print(f'Você ainda pode efetuar {LIMITE_SAQUES - numeros_saques} saque(s).')
        else:
            print(f'Operação não efetuada. Número total de saques atingido.')

    elif opcao == 'e':
        print("==========Extrato==========")
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'Saldo atual: R$ {saldo:.2f}')
        print('===========================')

    elif opcao == 'q':
        break

    else:
        print("Opção incorreta, digite alguma das opções disponiveis no menu!!")

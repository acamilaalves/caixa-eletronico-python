print("BEM-VINDO AO CAIXA ELETRÔNICO")
print("-----------------------------------------")

saldo = 1000.0
extrato = []

while True:
    print("\nMENU INICIAL:")
    print("1 - Saldo Atual")
    print("2 - Saque")
    print("3 - Depósito")
    print("4 - Extrato")
    print("0 - Sair")
    print("-----------------------------------------")

    try:
        opcao = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Opção inválida! Digite apenas números.")
        continue

    # SALDO
    if opcao == 1:
        print(f"Seu saldo atual é R$ {saldo:.2f}")

    # SAQUE
    elif opcao == 2:
        try:
            saque = float(input("Informe o valor que deseja sacar: "))
        except ValueError:
            print("Valor inválido!")
            continue

        if saque <= 0:
            print("O valor do saque deve ser maior que zero.")
        elif saque > saldo:
            print("Saldo insuficiente!")
        else:
            saldo -= saque
            extrato.append(f"Saque: R$ {saque:.2f}")
            print(f"Saque realizado com sucesso! Saldo: R$ {saldo:.2f}")

    # DEPÓSITO
    elif opcao == 3:
        try:
            deposito = float(input("Informe o valor que deseja depositar: "))
        except ValueError:
            print("Valor inválido!")
            continue

        if deposito <= 0:
            print("O valor do depósito deve ser maior que zero.")
        else:
            saldo += deposito
            extrato.append(f"Depósito: R$ {deposito:.2f}")
            print(f"Depósito realizado com sucesso! Saldo: R$ {saldo:.2f}")

    # EXTRATO
    elif opcao == 4:
        print("\n------- EXTRATO -------")
        if not extrato:
            print("Nenhuma movimentação realizada.")
        else:
            for movimento in extrato:
                print(movimento)
        print(f"Saldo atual: R$ {saldo:.2f}")

    # SAIR
    elif opcao == 0:
        print("Encerrando o atendimento. Obrigado por usar o caixa eletrônico!")
        break

    else:
        print("Opção inválida! Escolha uma opção válida.")

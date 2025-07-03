menu = """

============= MENU =============

    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [S] - Sair


================================

=> """

saldo = 0 
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        print("\n============= DEPÓSITO =============")
        quantia = float(input("Informe o Valor do Depósito: "))

        if quantia > 0:
            saldo += quantia
            extrato += f"Depósito: R$ {quantia:.2f}\n"
            print(f"\nDepósito de R$ {quantia:.2f} realizado com sucesso!")

        else:
            print("O valor informado é inválido, favor informar nova opção.")
    

    elif opcao == "2":
        print("\n============= SAQUE =============")
        quantia = float(input("Informe o Valor do Saque: "))

        ultrapassou_limite_saldo = quantia > saldo

        ultrapassou_limite = quantia > limite

        ultrapassou_limite_saques = numero_saques >= LIMITE_SAQUES

        if ultrapassou_limite_saldo:
            print("FALHA! Não há saldo suficiente.")
            print(f"\nSaldo Total: R$ {saldo:.2f}")

        elif ultrapassou_limite:
            print("FALHA! O valor do saque ultrapassou o limite.")
            print(f"\nLimite Total: R$ 500.00")

        elif ultrapassou_limite_saques:
            print("FALHA! Número máximo de 3 saques ultrapassado.")

        elif quantia > 0:
            saldo -= quantia
            extrato += f"Saque: R$ {quantia:.2f}\n"
            numero_saques += 1
            print(f"\nSaque de R$ {quantia:.2f} realizado com sucesso!")
            

        else:
            print("O valor informado é inválido, favor informar nova opção.")

    elif opcao == "3":
        print("\n============= EXTRATO =============")
        print("Não existem movimentações." if not extrato else extrato)
        print(f"\nSaldo Total: R$ {saldo:.2f}")
        print("\n==========================================")


    elif opcao == "S":
        print("Obrigado por usar nosso sistema!!!!")
        break

    else:
        print("Opção invalida, por favor selecione novamente a opção desejada.")
        
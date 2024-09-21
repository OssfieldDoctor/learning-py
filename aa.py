import datetime

MAX_SAQUE = 500
saldo = 1412.00
num_saques = 0
extrato = {}


while(True):


    print("\n------------BANCO SIMULATOR-----------")
    opcao = int(input("\n[1] SACAR \n[2] DEPOSITAR \n[3] EXTRATO\n[0] SAIR\n\nDIGITE A OPÇÃO DESEJADA: "))




    if opcao == 1: #SAQUE
        print("\n=============SAQUE=============")
        if num_saques < 3:
            saque = float(input("Informe quanto deseja sacar: "))

            if saque > MAX_SAQUE:
                print(f"Não foi possível realizar o saque, pois o valor informado excedeu o valor limite. Faça saque de até {MAX_SAQUE}.")
            else:
                print(f"Valor sacado: {saque}")
                saldo -= saque
                num_saques += 1
                extrato[datetime.datetime.now()] = "Saque" , saque
        else:
            print("A quantidade de saques diários foi excedida!")
        print("===============================\n")
    elif opcao == 2: #DEPOSITO
        print("\n============DEPÓSITO============")
        valorDepositar = float(input("Informe o valor a ser depositado: "))
        saldo += valorDepositar
        extrato[datetime.datetime.now()] = "Depósito:" , valorDepositar
        print(f"R$ {valorDepositar} foi depositado")
        print("================================\n")

    elif opcao == 3: #EXTRATO
        print("\n=============EXTRATO=============")

        if extrato == {}:
            print("Não foi realizado nenhuma movimentação.")
        else:
            for data, valor in extrato.items():
                print(f"Data: {data.strftime('%d/%m/%Y %H:%M:%S')} - {valor}")
        print(f"Saldo atual é R$ {saldo}")
        print("=================================\n")

    elif opcao == 0:
        print("\nObrigado por utilizar nosso serviço!")
        break

    else:
         print("\nSelecione uma operação válida!")

menu = '''
 =========== MENU INICIAL ===========                             
|                                    |
|          [dep] Depositar           | 
|          [sac] Sacar               |  
|          [ext] Extrato             | 
|          [quit] Sair               | 
|                                    |
*====================================*

=>  '''

saldo = 0
limite = 1000
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "dep":
        valor = int(input("\n Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"\n Depósito de R$ {valor:.2f} realizado com sucesso.")
            print(f"\n Saldo: R$ {saldo:.2f}")

        else:    
            print("\n Operação falhou! O valor informado é inválido.")

    elif opcao == "sac":
        valor = int(input("Informe o valor do saque: "))

        if numero_saques >= LIMITE_SAQUES:
            print("\n Não é possível realizar esta operação. Você excedeu o número de saques permitidos no dia.")
        
        elif valor > saldo:
            print("\n Não é possível realizar esta operação. Saldo insuficiente.")

        elif valor > limite:
            print(f"\n Não é possível realizar esta operação. Limite de saque permitido = R$ {limite:.2f}")    

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"\n Saque de R$ {valor:.2f} realizado com sucesso.")
            print(f"\n Saldo: R$ {saldo:.2f}")

        else:
            print("\n Não é possível realizar esta operação. O valor informado é inválido.")
  
    elif opcao == "ext":
        print("\n ============== EXTRATO ==============")
        print("\n \n Não foram realizadas movimentações." if not extrato else extrato)  
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("\n =====================================")   

    elif opcao == "quit":
        print("\n Obrigado por ultilizar nosso sistema. Volte Sempre!\n\n")
        break

    else:
        print("\n Opção inválida. Por favor selecione novamente a operação desejada.")
           
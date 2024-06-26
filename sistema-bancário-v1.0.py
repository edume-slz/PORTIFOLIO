saldo = 0
limite_saque = 500
extrato = ""
numero_saques = 0
LIMITE_DIARIO = 3

menu = (""" O QUE DESEJA FAZER HOJE?
             
             [1] DEPÓSITO
             [2] SAQUE
             [3] EXTRATO
             [0] SAIR

            OPÇÃO DESEJADA: """)

while True:
    opcao = int(input(menu))
    
    if opcao == 1:
        valor_deposito = float(input("VALOR PARA DEPÓSITO: "))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print(f"DEPÓSITO DE {valor_deposito:.2f} REALIZADO COM SUCESSO")

    elif opcao == 2:
        valor_saque = float(input("INSIRA O VALOR PARA SAQUE: R$ "))
        
        if valor_saque > saldo:
            print("SALDO INSUFICIENTE!")
        elif valor_saque > limite_saque:
            print(f"O VALOR INFORMADO EXCEDE SEU LIMITE DE SAQUE! LIMITE R$ {limite_saque:.2f}")
        elif numero_saques >= LIMITE_DIARIO:
            print("LIMITE DIÁRIO DE SAQUE EXCEDIDO! VÁ ATÉ SUA AGÊNCIA.")
        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numero_saques += 1
            print(f"SAQUE DE R$ {valor_saque:.2f} REALIZADO COM SUCESSO")
        else:
            print("VALOR INVÁLIDO PARA SAQUE!")

    elif opcao == 3:
        print(f"""                  BANCO OKOTISU
<<============================================================>>
  Operação número: ID28900034000128900
  Cliente: Fulano Galenguer Miller
<<============================================================>>

Saldo: R$ {saldo:.2f}
{extrato if extrato else "Sem transações"}
Limite diário por saque: R$ {limite_saque:.2f}
Saques realizados hoje: {numero_saques} de {LIMITE_DIARIO}

""")
        
    elif opcao == 0:
        print()
        print()
        print("OBRIGADO POR UTILIZAR NOSSO SISTEMA!")
        break

    else:
        print("OPÇÃO INVÁLIDA, POR FAVOR TENTE NOVAMENTE!")
import textwrap

def menu():
    menu = f"""INFORME A OPÇÃO DESEJADA:

[1] DEPOSITAR 
[2] SACAR 
[3] EXTRATO
[4] NOVO USUÁRIO
[5] NOVA CONTA
[6] LISTAR CONTAS
[0] SAIR

-> : """
    return input(menu)

def depositar_dinheiro(saldo, valor_depositado, extrato, /):
    if valor_depositado > 0:
        saldo += valor_depositado
        extrato += f"VALOR DEPOSITADO R$ {valor_depositado:.2f}\n"
        print("DEPÓSITO REALIZADO COM SUCESSO, AGUARDE O COMPROVANTE!")
    else:
        print("VALOR INCOMPATÍVEL")
    return saldo, extrato

def sacar_dinheiro(*, saldo, valor_saque, extrato, numero_saques, limite_saque, numero_saques_diario):
    excedeu_saldo = valor_saque > saldo
    excedeu_limite_saque = valor_saque > limite_saque
    excedeu_numero_saque = numero_saques >= numero_saques_diario

    if excedeu_saldo:
        print("\n### SALDO INSUFICIENTE, VERIFIQUE SEU EXTRATO ###")
    elif excedeu_limite_saque:
        print("### LIMITE DE SAQUE EXCEDIDO, ATUALIZE SUA CONTA NO APP OU FALE COM SUA AGÊNCIA! ###")
    elif excedeu_numero_saque:
        print("### NÚMERO DE SAQUES DIÁRIOS EXCEDIDO! ATUALIZE SUA CONTA ###")
    elif valor_saque > 0:
        saldo -= valor_saque
        numero_saques += 1
        extrato += f"- R$ {valor_saque:.2f}\n"
        print("### AGUARDE A CONTAGEM DAS CÉDULAS!... ###")
    else:
        print("### OPERAÇÃO NÃO RECONHECIDA ###")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato, numero_saques, numero_saques_diario):
    print("\n########## EXTRATO ############")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print(f"\n\nNÚMERO DE SAQUES REALIZADOS: {numero_saques} DE {numero_saques_diario}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe seu CPF - somente números: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe uma conta com este CPF cadastrada, deseja fazer login? ")
        return
    
    nome = input("Informe seu nome completo: ")
    aniversario = input("Informe a data de seu aniversário (Ex: dd-mm-aa): ")
    endereco = input("Informe seu endereço (Ex: Avenida 03, 08, Bairro - Cidade/Estado): ")

    usuarios.append({"nome": nome, "data_nascimento": aniversario, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    numero_saques_diario = 3
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar_dinheiro(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar_dinheiro(
                saldo=saldo,
                valor_saque=valor,
                extrato=extrato,
                numero_saques=numero_saques,
                limite_saque=limite,
                numero_saques_diario=numero_saques_diario,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato, numero_saques=numero_saques, numero_saques_diario=numero_saques_diario)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()

menu = """
        Bem vindo ao Banco Novo

        [1] Depositar
        [2] Sacar
        [3] Extrato Bancario
        [4] Encerrar

        Selecione a opção desejada: """

# informações da conta -------------
saldo = 1300
limite = 500
extrato = ""
numero_saque = 0
limite_saque = 3

def exibir_mensagem(mensagem):
    print(mensagem)

def validar_valor(valor):
    return valor > 0

while True:
    opcao = input(menu)

    if opcao == "1":
        while True:
            valor = float(input("Informe o valor do depósito: "))

            if validar_valor(valor):
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                exibir_mensagem(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
                exibir_mensagem(f"Seu novo saldo é: R${saldo:.2f}")
                break
            else:
                exibir_mensagem("Valor inserido inválido, insira um valor válido.")

    elif opcao == "2":
        while True:
            valor = float(input("Informe o valor de saque: "))

            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saque = numero_saque >= limite_saque

            if excedeu_saldo:
                exibir_mensagem("Saque não efetuado: Saldo Insuficiente.")
                break
            elif excedeu_limite:
                exibir_mensagem("Saque não efetuado: O valor excede o limite diário.")
                break
            elif excedeu_saque:
                exibir_mensagem("Saque não efetuado: Limite de saques atingido.")
                break
            elif validar_valor(valor):
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saque += 1
                exibir_mensagem(f"Saque de R$ {valor:.2f} realizado com sucesso.")
                exibir_mensagem(f"Seu novo saldo é: R${saldo:.2f}")
                break
            else:
                exibir_mensagem("Valor inserido inválido, insira um valor válido.")

    elif opcao == "3":
        print("\n==================== EXTRATO ====================")
        print("Não foram realizadas movimentações em sua conta." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===================================================")

    elif opcao == "4":
        exibir_mensagem("###### O Banco Novo agradece pela sua preferência. ######")
        break

    else:
        exibir_mensagem("\nValor inserido inválido, insira um valor válido.\n")

from colorama import Fore, Style, init

init(autoreset=True)

def bem_vindo():
    print(Fore.GREEN + "=============================")
    print(Fore.CYAN + "    Bem-vindo ao Python Bank  ")
    print(Fore.GREEN + "=============================")
    print(Style.BRIGHT + Fore.YELLOW + "Seu banco digital para o futuro!")
    print("\n")

def exibir_menu():
    print(Fore.BLUE + "\nEscolha uma opção:")
    print("[1] Depositar")
    print("[2] Sacar")
    print("[3] Ver extrato")
    print("[0] Sair")
    return input("Digite o número da operação desejada: ")

def depositar(saldo, extrato):
    valor = float(input(Fore.YELLOW + "Digite o valor para depósito: R$ "))
    if valor > 0:
        saldo += valor
        extrato.append(Fore.GREEN + f"Depósito: R$ {valor:.2f}")
        print(Fore.GREEN + f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print(Fore.RED + "Valor inválido para depósito!")
    return saldo, extrato

def sacar(saldo, extrato, limite, saques_realizados, LIMITE_SAQUES):
    valor = float(input(Fore.YELLOW + "Digite o valor para saque: R$ "))
    if valor > saldo:
        print(Fore.RED + "Saldo insuficiente para realizar o saque.")
    elif valor > limite:
        print(Fore.RED + f"Saque acima do limite permitido (Limite: R$ {limite:.2f}).")
    elif saques_realizados >= LIMITE_SAQUES:
        print(Fore.RED + "Número máximo de saques diários atingido!")
    else:
        saldo -= valor
        extrato.append(Fore.RED + f"Saque: R$ {valor:.2f}")
        saques_realizados += 1
        print(Fore.GREEN + f"Saque de R$ {valor:.2f} realizado com sucesso!")
    return saldo, extrato, saques_realizados

def exibir_extrato(saldo, extrato):
    print(Fore.YELLOW + "\n===== Extrato =====")
    if extrato:
        for operacao in extrato:
            print(operacao)
    else:
        print(Fore.CYAN + "Nenhuma transação foi realizada.")
    print(Fore.YELLOW + f"\nSaldo atual: R$ {saldo:.2f}")
    print("====================")

def main():
    saldo = 0
    limite = 500
    extrato = []
    saques_realizados = 0
    LIMITE_SAQUES = 3

    bem_vindo()

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == "2":
            saldo, extrato, saques_realizados = sacar(saldo, extrato, limite, saques_realizados, LIMITE_SAQUES)

        elif opcao == "3":
            exibir_extrato(saldo, extrato)

        elif opcao == "0":
            print(Fore.CYAN + "Obrigado por usar o Python Bank! Até logo.")
            break

        else:
            print(Fore.RED + "Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
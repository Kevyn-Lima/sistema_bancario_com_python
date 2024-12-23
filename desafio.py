menu = f"""
    [1] Depositar
    [2] Sacar
    [3] Extrato 
    [4] Saldo
    [0] Sair

    =>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    opcao = input(menu)
    
    if opcao == "1":

        deposito = float(input("Qual valor deseja depositar? "))

        if deposito <= 0:
            print("Voce não pode depositar um valor negativo.")
        else:
            saldo += deposito
            extrato += f"Deposito: R$ {deposito:.2f}\n"

    elif opcao =="2" and numero_saques < LIMITE_SAQUES:

        sacar = float(input("Digite o valor do saque: "))

        if sacar <= saldo and saldo != 0 and sacar <= 500:
            saldo -= sacar
            extrato += f"Saque: R$ {sacar:.2f}\n"
            numero_saques = numero_saques + 1
        elif saldo < sacar or sacar == 0:
            print("Saldo insuficiente")

        elif sacar > 500:
            print("Voce nao pode realizar um saque tao alto")
        

    elif opcao == "4":
        print(f"Saldo: R${saldo}")

    elif opcao == "3":
        print(f"Extrato: {extrato}")

    elif opcao == "0":
        break

    else: 
        print("Operação inválida, ou voce atingiu seus 3 saques diarios, por favor selecione novamente a operação desejada.")
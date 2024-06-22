#Ailton Vasconcelos github: AkowsS
numDeSaqueAtual = 0
LIMITE_SAQUES = 3
limiteMaximoDeSaque = 500
saldo = 0
extrato = ""

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=>"""

while True:

  opcao = input(menu)

  if opcao == "d":
    print("Deposito\n")

    valorDeposito = float(input("Digite o valor de Deposito: "))

    if valorDeposito > 0:
      saldo += valorDeposito
      extrato += f"Depósito: R$ {valorDeposito:.2f}\n"
    else:
      print("A operação falhou, o valor informado é inválido")

  elif opcao == "s":
    print("Saque\n")
    valorSaque = float(input("Digite o valor de Saque: "))
    if (valorSaque <= saldo) and (valorSaque > 0) and (valorSaque < limiteMaximoDeSaque) and (numDeSaqueAtual < LIMITE_SAQUES):
      saldo -= valorSaque
      numDeSaqueAtual += 1
      extrato += f"Saque: R$ {valorSaque:.2f}\n"
      print("Numero de saque atual: ", numDeSaqueAtual, "\nMaximo diário: ",LIMITE_SAQUES)
    else:
      if (valorSaque > saldo): print("Erro! Você não possui saldo suficiente.")
      if (valorSaque <= 0): print("Valor digitado é inválido.")
      if (valorSaque > limiteMaximoDeSaque): print("Valor maximo permitido por saque é R$500.00.")
      if (numDeSaqueAtual >= LIMITE_SAQUES): print("Você atingiu a quantidade maxima de saques diários.")

  elif opcao == "e":
    print("///////////////Extrato///////////////\n")
    print("Não foram realizados movimentações." if not extrato else extrato)
    print(f"Saldo: R${saldo:.2f}")
    print("=====================================")

  elif opcao == "q":
    break
  
  else:
    print("Opção digitada é inválida, por favor tente novamente.")


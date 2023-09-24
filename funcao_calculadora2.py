def calculadora():
  """
  Calculadora simples que permite ao usuário escolher entre as seguintes operações:

  1: Soma
  2: Subtração
  3: Multiplicação
  4: Divisão
  0: Sair

  O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair.
  """

  # Variáveis globais

  opções = ["Soma", "Subtração", "Multiplicação", "Divisão", "Sair"]

  # Loop infinito

  while True:
    # Exibe as opções
    print("Escolha uma opção:")
    for i, opção in enumerate(opções):
      print(f"{i + 1}: {opção}")

    # Lê a opção do usuário
    opção_escolhida = input("Opção: ")

    # Valida a opção
    try:
      opção_escolhida = int(opção_escolhida)
    except ValueError:
      print("Essa opção não existe")
      continue

    # Realiza a operação
    if opção_escolhida == 0:
      break

    # Lê os dois valores
    print("Digite o primeiro valor:")
    primeiro_valor = float(input())
    print("Digite o segundo valor:")
    segundo_valor = float(input())

    # Calcula o resultado
    result = 0
    if opção_escolhida == 1:
      result = primeiro_valor + segundo_valor
    elif opção_escolhida == 2:
      result = primeiro_valor - segundo_valor
    elif opção_escolhida == 3:
      result = primeiro_valor * segundo_valor
    elif opção_escolhida == 4:
      result = primeiro_valor / segundo_valor

    # Exibe o resultado
    print(f"O resultado é: {result}")


calculadora()
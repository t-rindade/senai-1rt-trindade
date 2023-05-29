def menu():
  print("\nOperações: ")
  print("+ Adição")
  print("- Subtração")
  print("/ Divisão")
  print("* Multiplicação")
  operator = (input("\nSelecione uma operação: "))

  match operator:
    case "+":
      print("\nAdição Selecionada!")
    case "-":
      print("\nSubtração Selecionada!")
    case "/":
      print("\nDivisão Selecionada!")
    case "*":
      print("\nMultiplicação Selecionada!")
    case _:
      print("\nSelecione uma opção válida!")
      menu()
      
  x = float(input("Valor de X: "))
  y = float(input("Valor de Y: "))
  
  match operator:
    case "+":
      soma = x + y
      print(f"\n{x} + {y}\nResultado: {soma}")
      input("\nPressione ENTER para voltar ao menu\n")
      menu()
    case "-":
      subtração = x - y
      print(f"\n{x} - {y}\nResultado: {subtração}")
      input("\nPressione ENTER para voltar ao menu\n")
      menu()
    case "/":
      divisao = x / y
      print(f"\n{x} / {y}\nResultado: {divisao}")
      input("\nPressione ENTER para voltar ao menu\n")
      menu()
    case "*":
      multiplicacao = x * y
      print(f"\n{x} * {y}\nResultado: {multiplicacao}")
      input("\nPressione ENTER para voltar ao menu\n")
      menu()
    case _:
      menu()

menu()
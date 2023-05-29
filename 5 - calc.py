import sys

def somaf():
  x = float(input("Valor de X: "))
  y = float(input("Valor de Y: "))
  soma = x + y
  print(f"\nResultado dos valores: {soma}")
  print("\nDesejar voltar para o menu?\n1-SIM 2-NÃO")
  selecao = int(input("> "))
  match selecao:
    case 1:
      menu()
    case 2:
      sys.exit

def multiplicacaof():
  x = float(input("Valor de X: "))
  y = float(input("Valor de Y: "))
  multiplicacao = x * y
  print(f"\nResultado dos valores: {multiplicacao}")
  print("\nDesejar voltar para o menu?\n1-SIM 2-NÃO")
  selecao = int(input("> "))
  match selecao:
    case 1:
      menu()
    case 2:
      sys.exit

def maiorf():
  x = float(input("Valor de X: "))
  y = float(input("Valor de Y: "))
  maior = max(x,y)
  print(f"\nResultado dos valores: {maior}")
  print("\nDesejar voltar para o menu?\n1-SIM 2-NÃO")
  selecao = int(input("> "))
  match selecao:
    case 1:
      menu()
    case 2:
      sys.exit

def menorf():
  x = float(input("Valor de X: "))
  y = float(input("Valor de Y: "))
  menor = min(x,y)
  print(f"\nResultado dos valores: {menor}")
  print("\nDesejar voltar para o menu?\n1-SIM 2-NÃO")
  selecao = int(input("> "))
  match selecao:
    case 1:
      menu()
    case 2:
      sys.exit

def menu():
  print("\nOperações:")
  print("a. Somar")
  print("b. Multiplicar")
  print("c. Maior número")
  print("d. Menor número")
  print("0. Sair")
  selecao = input("\nSelecione uma operação: ")

  match selecao:
    case "a":
      print("\nSoma selecionada!")
      somaf()
    case "b":
      print("\nMultiplicação selecionada!")
      multiplicacaof()    
    case "c":
      print("\nMaior número selecionada!")
      maiorf()
    case "d":
      print("\nMenor número selecionada!")
      menorf()
    case "0":
      sys.exit
    case _:
      print("Digite uma opção válida!")
      menu()

menu()
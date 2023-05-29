def verificar_par(num1):
  sobra = num1%2
  if sobra == 0:
    print("Par!")
  else:
    print("Ímpar!")

x = int(input("Digite o valor de X: "))
verificar_par(x)
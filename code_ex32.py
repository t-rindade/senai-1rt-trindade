

while True:
  x = int(input("Insira o valor de X: "))
  verificacao = x%2

  if x < 0:
    print("NEGATIVO!")
    break
  elif verificacao == 0:
    print("PAR!")
  elif verificacao > 0:
    print("ÍMPAR!")
  
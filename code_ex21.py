velo = int(input("Insira a velocidade do carro em KM/H: "))


if velo > 80:
  dif = velo - 80
  dif2 = float(dif * 7)
  print(f"\nMultado!\nKM/H Acima da velocidade: {dif}\nValor da multa: R${dif2:.2f}")
else:
  print("Tudo OK!")
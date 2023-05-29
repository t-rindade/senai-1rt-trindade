velo = int(input("Insira a velocidade em KM/H: "))

dif = velo - 80

if velo > 80:
  print(f"\nExcesso de velocidade: ({dif}KM/H acima do permitido) - MULTADO")
else:
  print("\nTudo OK")
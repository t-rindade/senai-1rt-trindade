salario = float(input("Sálario atual do funcionário: R$"))

if salario > 8250:
  salario = salario + (salario * 0.10)
  print(f"Reajuste de 10% = RS{salario:.2f}")
elif salario <= 8250:
    salario = salario + (salario * 0.15)
    print(f"Reajuste de 15% = RS{salario:.2f}")
else:
  print("Insira um valor válido")
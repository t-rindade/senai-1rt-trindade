def maior(num1, num2, num3):
  major = max(num1, num2, num3)
  return major

x = float(input("Valor de X: "))
y = float(input("Valor de Y: "))
z = float(input("Valor de Z: "))

print(f"Maior valor: {maior(x, y, z)}")
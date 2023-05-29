x = float(input("Valor de X: "))
y = float(input("Valor de Y: "))
z = float(input("Valor de Z: "))

major = max(x, y, z)
minor = min(x, y, z)

print("\nX:{:.2f} | Y:{:.2f} | Z:{:.2f}".format(x,y,z))
print("\nO maior valor é: {:.2f}".format(major))
print("O menor valor é: {:.2f}".format(minor))

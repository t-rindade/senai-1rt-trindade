x = float(input("Valor da nota 1: "))
y = float(input("Valor da nota 2: "))
z = float(input("Valor da nota 3: "))

media = (x + y + z) / 3

print(f"\nNota 1: {x}")
print(f"Nota 2: {y}")
print(f"Nota 3: {z}")
print("Média das notas: {:.2f}".format(media))
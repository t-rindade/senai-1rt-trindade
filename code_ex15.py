nota1 = float(input("Informe a nota 1: "))
nota2 = float(input("Informe a nota 2: "))
nota3 = float(input("Informe a nota 3: "))

media = (nota1 + nota2 + nota3)/3

if media >= 6:
  print(f"\nMédia final: {media:.2f} - APROVADO")
elif media > 5:
  print(f"\nMédia final: {media:.2f} - RECUPERAÇÃO")
else:
  print(f"\nMédia final: {media:.2f} - REPROVADO")
distance = int(input("Distancia da viagem: "))


if distance <= 200:
  distance = float(distance * 0.50)
  print(f"Preço da passagem R${distance:.2f}")
elif distance > 200:
  distance = float(distance * 0.45)
  print(f"Preço da passagem R${distance:.2f}")
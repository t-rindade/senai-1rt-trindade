nota = float(input("Insira a nota do competidor: "))

if nota <= 50:
  print(f"Baseado na nota {nota} - Certificado de Participação")
elif nota <= 60:
    print(f"Baseado na nota {nota} - Certificado de Mensão Honrosa")
elif nota <= 70:
    print(f"Baseado na nota {nota} - Medalha de Bronze")
elif nota <= 90:
    print(f"Baseado na nota {nota} - Medalha de Prata")
elif nota > 90:
    print(f"Baseado na nota {nota} - Medalha de Ouro")
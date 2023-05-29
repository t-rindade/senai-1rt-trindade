def areaterreno(largura, comprimento):
  area = largura * comprimento
  return area

largura = float(input("Digite a largura: "))
comprimento = float(input("Digite a comprimento: "))
print(f"A área do terreno é: {areaterreno(largura, comprimento)}")
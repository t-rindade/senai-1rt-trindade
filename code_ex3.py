#import modulo sys
import sys

#matriz de meses
meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

#informe de nome
nome = str(input("Informe seu PRIMEIRO NOME: "))
if not nome.isalpha():
    sys.exit("Insira um NOME válido!")

#seleção de dia
dia = int(input("Informe o DIA do seu nascimento: "))
if not 1 <= dia <= 30:
    sys.exit("Insira um DIA válido!")    

#seleção de mês
print("\nSelecione o MÊS do seu nascimento: ")
for i in range(1, 13):
    print(f"{i}- {meses[i-1]}")

mnum = int(input("\nEntre um número de 1 a 12: "))
if not 1 <= mnum <= 12:
    sys.exit("Insira um MÊS válido")

#seleção de ano
ano = int(input("Informe o ANO do seu nascimento: "))
if not 1900 <= ano <= 2017:
    sys.exit("Insira um ANO válido!")

mnome = meses[mnum-1]
print (f"\nOlá {nome}. Você nasceu dia {dia} de {mnome} de {ano}.")
#Projeto de calculamento de IMC (Indice de Massa Muscular)
#Autor: Matheus Ruivo

name = input('Qual é seu nome?')
altura = float(input('Qual é sua altura atualmente em metros?'))
peso = float(input("Qual é seu peso (kg)?"))
imc = peso / (altura ** 2)
 # print(name, "você tem", altura,"e pesa", peso,"seu imc é", imc)
print(f"{name} você tem {altura} metros e pesa {peso} seu imc é {imc}") #Evolução

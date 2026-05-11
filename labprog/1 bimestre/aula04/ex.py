valor1 = float(input("escreva: "))
valor2 = float(input("escreva: "))
valor3 = float(input("escreva: "))

total = valor1 + valor2 + valor3

print("resultado: ",total)
print()

print("ex2")

prov1 = float(input("escreva o valor da prova 1: "))
prov2 = float(input("escreva o valor da prova 2: "))
trab2 = float(input("escreva o valor do trabalho: "))
part3 = float(input("escreva o valor da participção: "))

provas = 3 * prov1 + 3 * prov2

media = ( provas + 3 * trab2 + part3) / 10

print("valor da media á: ", media )
print()


print("ex 3")

alt1 = float(input("informe sua altura1: "))
homem = ( 72.7 * alt1 ) - 58
mulher = (62.1 * alt1 ) - 44.7

print(" se for mulher seu peso ideal sera: ",mulher,"se for homem seu peso ideal sera: ",homem)

#todos os numeros pares de um intervalo
num = int(input("numero 1: "))
num1 = int(input("numero 2: "))
soma = 0
for i in range( num, num1 + 1):
    if(i%2 == 0):
        soma = soma + i
print(f'a soma é {soma}')
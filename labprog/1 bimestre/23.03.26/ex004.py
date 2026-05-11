import random
x = int(input("digite o numero: "))
contador = 0
soma = 0
while contador <= x:
    numero_sorte = random.randint(1,10)
    print(numero_sorte)
    contador = contador + 1
    soma = soma + x
print(f'a soma é: {soma}')


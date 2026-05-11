import random
x = int(input("digite o numero: "))
soma = 0
for contador in range(x):
    numero_sorte = random.randint(1,10)
    print(numero_sorte)
    soma = soma + x
print(f'a soma é: {soma}')
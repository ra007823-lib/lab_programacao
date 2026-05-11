import random
num = int(input("ditia um numero ai de 1 a 10: "))
soma = 0
num_sort = random.randint(1,10)
print(f'numero sorteados: {num_sort}')
while num != num_sort:
    soma = soma + num_sort
    num_sort = random.randint(1,10)
    print(f'numero sorteados: {num_sort}')
print(f'a soma é: {soma}')
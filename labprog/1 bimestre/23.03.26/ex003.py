import random
num = int(input("ditia um numero ai de 1 a 10: "))
soma = 0
contador = 0 #verificar quantas vezes ele passou pelo while
num_sort = random.randint(1,10)
print(f'numero sorteados: {num_sort}')
while num != num_sort:
    soma = soma + num_sort
    contador = contador + 1 # formula para verificar
    num_sort = random.randint(1,10)
    print(f'numero sorteados: {num_sort}')
print(f'a soma é: {soma}')
print(f'tentativas: {contador}')
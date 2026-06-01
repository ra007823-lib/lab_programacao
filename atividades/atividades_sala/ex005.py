lista = []

for i in range(1,7):
    v = int(input(f'digite o {i}° numero: '))
    lista.append(v)
num = int(input('digite um num para teste: '))

cont = lista.count(num)
posição = lista.index(num)

print(f'a quantidade de vezes que o numero buscado aparece é de {cont}')
print(f'a primeira posição em que ele aparece é a {posição}°')
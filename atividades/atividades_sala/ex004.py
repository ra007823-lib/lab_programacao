lista = []

for i in range(1,6):
    l = float(input(f'digite a {i}° nota: '))
    lista.append(l)
print(f'a nota dos alunos foram: {lista}')

men = min(lista)
print(f'a menor nota foi de: {men}')

if men in lista:
    lista.remove(men)
    
print(f'após a remoção da menor a lista ficou assim: {lista}')
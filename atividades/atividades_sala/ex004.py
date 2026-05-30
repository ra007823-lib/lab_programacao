lista = []

for i in range(1,6):
    l = float(input(f'digite a {i}° nota: '))
    lista.append(l)

men = min(lista)
print(men)

if men in lista:
    lista.remove(men)
print(lista)
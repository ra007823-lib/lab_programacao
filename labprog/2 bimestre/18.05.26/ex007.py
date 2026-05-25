lista1 = [1,2,3]
lista2 = []
for e in lista1:
    lista2.append(e)
lista1[0] = 10
print(lista1)
print(lista2)
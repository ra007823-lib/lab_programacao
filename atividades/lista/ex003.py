# lista1 = [1,2,3,4]
# lista2 = [10,20,30,40,50,60]

# lista_inter = []

# for i in range(4):
#     lista_inter.append(lista1[i])
#     lista_inter.append(lista2[i])
# lista_inter.append(50)
# lista_inter.append(60)
# print(lista_inter)

# lista1 = [1,2,3,4]
# lista2 = [10,20,30,40,50,60]

# lista_inter = []

# for i in range(len(lista2)):
#     if i < len(lista1):
#         lista_inter.append(lista1[i])
#     lista_inter.append(lista2[i])
# print(lista_inter)

# #nesse caso o i representa o index da lista 

lista = [1,2,3,4]
lista2 = [10,20,30,40,50,60]

if len(lista) <= len(lista2):
    menor, maior = lista, lista2
else:
    maior, menor = lista,lista2

lista_inter = []

for i in range(len(maior)):
    if i < len(menor):
        lista_inter.append(menor[i])
    lista_inter.append(maior[i])
print(lista_inter)
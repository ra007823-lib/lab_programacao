num = int(input('digite um numero int posi: '))

lista = []
produto = 1

# for i in range(num+1):
#     if i %2 != 0:
#         lista.append(i)
#         produto *= i

for i in range(1,num+1,2):
    lista.append(i)
    produto *= i
print(lista)
print(f'o produto obitodo dos numero {num} é: {produto}')
    
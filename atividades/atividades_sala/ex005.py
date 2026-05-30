lista = []

for i in range(1,7):
    v = int(input(f'digite o {i}° numero: '))
    lista.append(v)
num = int(input('digite um num para teste: '))

cont = 0
for e in lista:
    if e == num:
        cont +1
cont = lista.count(num)

x =0

for e in lista:
    if x in lista:
     x = lista.index(num)
print(cont)
print(x)
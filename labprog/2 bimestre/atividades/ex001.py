lista = []
teste = []
for i in range(10):
    listas = int(input(f'digite o {i+1} valor: '))
    lista.append(listas)

for y in lista:
    if y not in teste:
        teste.append(y)

print('o teste ralizado resultou em: ',len(teste))
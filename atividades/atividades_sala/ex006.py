nomes = []
nomesinv = []
for i in range(1,6):
    n = input(f'digite o {i}° nome: ')
    nomes.append(n)

nomesinv.append(nomes)
nomesinv = nomes[::-1]

print(f'lista: {nomes}')
print(f'lista invertida: {nomesinv}')
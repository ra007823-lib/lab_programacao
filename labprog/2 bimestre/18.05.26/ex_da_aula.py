import random

um,dois,tres,quatro,cinco,seis =0,0,0,0,0,0
lancamento = []

dados = []

for i in range(100):
    resultado =  random.randint(1,6)
    dados.append(resultado)
    if resultado == 6:
        seis +=1
    if resultado == 5:
        cinco+=1
    if resultado == 4:
        quatro +=1
    if resultado == 3:
        tres +=1
    if resultado == 2:
        dois +=1
    if resultado == 1:
        um +=1
print(f'resultado obtido em 100 lançamentos foi: {dados}')
print(f'A quantidade de resultado 1 foi de:{um}')
print(f'A quantidade de resultado 2 foi de:{dois}')
print(f'A quantidade de resultado 3 foi de:{tres}')
print(f'A quantidade de resultado 4 foi de:{quatro}')
print(f'A quantidade de resultado 5 foi de:{cinco}')
print(f'A quantidade de resultado 6 foi de:{seis}')


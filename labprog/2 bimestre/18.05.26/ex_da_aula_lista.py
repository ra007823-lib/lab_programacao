import random

dados = []

for i in range(100):
    resultado =  random.randint(1,6)
    dados.append(resultado)

frequencia = []
for face in range(1,7):
    quantidade = dados.count(face)
    frequencia.append(quantidade)

print('vetor de lançamento 100x')
print(dados)
print('\n vetor de frequencias (quantidae de vezes das faces: 1, 2, 3, 4, 5, 6.)')
print(frequencia)
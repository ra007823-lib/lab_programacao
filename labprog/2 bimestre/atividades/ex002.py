vetor = []
for i in range(5):
    vetores = int(input(f'digite o {i+1} valor: '))
    vetor.append(vetores)
valor = int(input('digit eum valor para teste: '))
posicao = -1

for i in range(len(vetor)):
    if vetor[i] == valor:
        posicao = i
        break
print(posicao)
    


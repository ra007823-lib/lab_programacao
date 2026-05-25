vetor = [2.5,7.5,10,4]
media = sum(vetor)/len(vetor)

prox_media = vetor[0]
menor_dist = abs(vetor[0]-media)

for valor in vetor:
    dist_atual = abs(valor - media)
    if dist_atual < menor_dist:
        menor_dist = dist_atual
        prox_media = valor

print(f'vetor: {vetor}')
print(f'media: {media:.1f}')
print(f'Valor mais proximo da media: {prox_media}')
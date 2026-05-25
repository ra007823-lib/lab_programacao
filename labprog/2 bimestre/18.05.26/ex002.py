notas = [8.2,5.0,7.1]
turma = 'B'
media = 0
for i in range(len(notas)):
    media = media + notas[i]
media = media/len(notas)
print(media,notas,turma)

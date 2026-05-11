nomes = []
notas = []
media = 0
for x in range(3):
    nomes.append(input(f'o nome do {x+1}° aluno:'))
    notas.append(float(input(f'nota do {x+1}° aluno: ')))
    media = media + notas[x]

media = media / 3
print(f'\na media da turma é: {media:.2f}\n')

if (notas[x] > media):
    print(f'Parabens {nomes[x]}! Sua nota foi {notas[x]}.')

nomes = []
notas = []
for x in range(3):
    nomes.append(input(f'o nome do {x+1}° aluno:'))
for x in range(3):
    notas.append(float(input(f'nota do {x+1}° aluno: ')))

media = notas[x]/ 3

print(f'a media da turma é: {media:.2f}')

if (notas[0] > media) or (notas[1] > media) or (notas[2] > media):
    print(f'Parabens {nomes}, sua nota {notas}')

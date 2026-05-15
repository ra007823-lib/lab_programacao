notas = [0]*3
soma = 0
for i in range(len(notas)):
    msg = f'{i+1}° nota do aluno: '
    notas[i] = float(input(msg))
    soma += notas[i]
print(f'a media da turma é: {soma/3:.2f}.')
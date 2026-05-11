nome1 = input('nome aluno 1: ')
nome2 = input('nome aluno 2: ')
nome3 = input('nome aluno 3: ')

nota1 = float(input(f'Nota de {nome1}: '))
nota2 = float(input(f'Nota de {nome2}: '))
nota3 = float(input(f'Nota de {nome3}: '))

media = (nota1 + nota2 + nota3) / 3 
print(f'a media da turma é: {media:.2f}')

if nota1 > media:
    print(f'Parabens {nome1}, sua nota {nota1}')

if nota2 > media:
    print(f'Parabens {nome2}, sua nota {nota2}')

if nota3 > media:
    print(f'Parabens {nome3}, sua nota {nota3}')


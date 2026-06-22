def media(valor):
    if valor > 6:
        print('aprovado')
    elif 4 < valor < 6:
        print('verificação suplementar')
    else:
        print('reprovado')

valor = float(input('digite a media do aluno: '))
media(valor)
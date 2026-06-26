nome = input('Digite seu nome: ')

resultado = ''
InicioPalavra = True

for letra in nome:
    if letra != ' ':
        if InicioPalavra:
            resultado += letra + '. '
            InicioPalavra = False
    else:
        InicioPalavra = True

print(f'As inicias são: {resultado}')
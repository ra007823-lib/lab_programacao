frase = input('Digite uma frase: ').lower()

palaSoma = 0
palavra = False

for pala in frase:
    if pala != " ":
        if palavra == False:
            palaSoma += 1
            palavra = True
    else:
        palavra = False

print(f'A quantidade de palavras informadas foi: {palaSoma}')
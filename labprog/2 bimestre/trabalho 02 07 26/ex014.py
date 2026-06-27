entrada = input('Digite a frase: ')
palavras = entrada.split()
saida = []

for i in palavras:
    if i.startswith('#'):
        saida.append(i)

print('as palavras com hashtag são: ',saida)
entrada = input('digite uma palavra para texte: ').lower()
palavraNova = ''

for i in entrada:
    if i == 'a':
        palavraNova +='*'
    else:
        palavraNova += i

print(palavraNova)

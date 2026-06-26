frase = input('Digite uma frase: ').lower()

palavra = ''
fraseAjust = ''

for i in range(len(frase) -1,-1,-1):
    if frase[i] != ' ':
        palavra = frase[i] + palavra 
    else:
        fraseAjust += palavra + ' '
        palavra = ''

fraseAjust += palavra

print(fraseAjust)

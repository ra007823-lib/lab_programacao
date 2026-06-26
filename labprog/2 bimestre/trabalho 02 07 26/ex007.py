frase = input('Digite uma frase: ').lower()

ajustada = ''
espaco = False

for l in frase:
    if l != " ":
        ajustada += l
        espaco = False
    else:
        if ajustada != "" and espaco == False:
            ajustada += " "
            espaco = True

if ajustada != "" and ajustada[-1] == " ":
    ajustada = ajustada[:-1]

print(ajustada)
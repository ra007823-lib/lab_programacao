entradaFrase = input('Digite uma frase: ').lower()
entradaPalavra = input('Digite a palavra da frase para contar: ').lower()

contador = 0
frase = ''

for letra in entradaFrase:
    if letra == " " or letra == "." or letra == "," or letra == "!" or letra == "?":
        if frase == entradaPalavra:
            contador += 1
        frase =''
    else:
        frase += letra
if frase == entradaPalavra:
    contador += 1
print(f'a palavra {entradaPalavra} informada apareceu {contador} vezes!')

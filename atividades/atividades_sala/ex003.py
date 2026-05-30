palavra = input('digite uma palavra: ').lower()

vogais=0
for letra in palavra:
    if letra in 'a''e''i''o''u':
        vogais+=1
print(vogais)

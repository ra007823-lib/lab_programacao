entrada = input('digite algo para alterar: ').lower()
alterado = ''

for letra in entrada:
    if letra =='z':
        alterado +='a'
    else:
        alterado += chr(ord(letra) + 1)
print('ateração aplicada:',alterado)
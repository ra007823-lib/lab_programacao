entrada = input('digite 11 numeros: ')
conversao = ''

for num in range(len(entrada)):
    conversao += entrada[num]

    if num == 2  or num ==5:
        conversao += '.'
    elif num == 8:
        conversao +='-'
print(f'o valor tratado para o formato CPF: {conversao}')

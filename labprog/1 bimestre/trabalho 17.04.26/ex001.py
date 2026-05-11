senha = input('digite uma senha: ')
num = False
letra = False
tem_8_dig = False


if len(senha) >=8:
    tem_8_dig = True

for x in senha:
    if x.isdigit():
        num = True
    if x.isalpha():
        letra = True

if tem_8_dig:
    print('possui 8 caracteres!')
else:
    print('erro na quantidade de caracteres!')
print('-'*60)
if num:
    print('possui numeros!')
else:
    print('não possui numeros!')
print('-'*60)
if letra:
    print('possui letras')
else:
    print('não possui letras')
print('-'*60)

if tem_8_dig and num and letra:
    print('senha valida!')
else:
    print('senha invalida!')
print('-'*60)
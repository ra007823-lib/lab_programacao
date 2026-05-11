numero = int(input('digite um numero: '))
contador = 0
if numero == 0:
    contador = 1
else:
    temp = numero
    while temp > 0:
        temp //= 10
        contador = contador + 1
print(f'o numero {numero} possui {contador} digitos!')



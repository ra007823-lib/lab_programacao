op = input("deseja somar (S) ou multiplicar (M)? ")
x = float(input("digite o primeiro numero: "))
y = float(input("digite o segundo numero: "))

if (op == 'S'):
    r = x + y
    print('O resultado da soma é: ', r)
else:
    r = x * y
    print('O resultado da multiplicação é:', r)
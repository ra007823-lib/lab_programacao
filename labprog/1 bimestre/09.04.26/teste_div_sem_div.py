x = float(input('Digite o dividendo(x): '))
y = float(input('Digite o divisor(y): '))
#guardar os valores originais
dividendo = x
divisor=y
quociente=0

#a logica: subitrair enquanto o x for maior ou igual ao divisor

while x > y:
    x -= y
    quociente +=1
resto = x
print('-'*110)
print(f'O resultado do {dividendo} / {divisor}: ')
print(f'Quociente (divisão inteira): {quociente}')
print(f'Resto: {resto}')
print('-'*110)


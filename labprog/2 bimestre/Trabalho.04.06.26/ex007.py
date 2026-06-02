n = int(input('digite o numero que deseja testar: '))

x = 1
test = False
while x * (x + 1) * (x + 2) <= n:
    
    if x * (x + 1) * (x + 2) == n:
        print(f'foi encontrado um numero satisfatorios, valor o pois {n} é resultado de : {x} * {x+1} * {x+2} = {n}')
        test = True
        break
    x +=1 
if not test:
    print(f'o valor informado {n} não possiu essa propriedade')
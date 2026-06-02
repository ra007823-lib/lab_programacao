print('para o teste a < b')
a = int(input('digite um valor para a: '))
b = int(input('digite um valor para b: '))

soma= []

if a < b:
    for i in range(a,b+1):
        if i % 2 != 0:
            soma.append(i)
    print(f'Foram encontrados {len(soma)} numeros impares e o valor da soma foi de: {soma} = \033[32m{sum(soma)}\033[0m')
else:
    print('\033[31merro!\033[m')
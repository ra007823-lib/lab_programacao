n = int(input('Digite um número para verificar se é produto de 3 consecutivos: '))
i = 1
# testamos enquanto o produto for menor ou igual a N

while i * (i + 1) * (i + 2) <= n:
    if i * (i + 1) * (i + 2) == n:
        print(f'Sim! {n} é o produto de {i}x{i+1}x{i+2}')
        break
    i += 1
else:
    print(f'O numero {n} não é produto de 3 inteiros consecutivos')
n = int(input('Quantos valores você deseja inserir: '))
soma_quadrado = 0

for i in range(0, n):
    valor = float(input(f'Digite o {i+1}° valor: '))
    #o quadrado pode ser o valor x valor ou valor^2
    soma_quadrado += valor**2
print(f'\nA soma dos quadrados dos {n} valores é: {soma_quadrado}')
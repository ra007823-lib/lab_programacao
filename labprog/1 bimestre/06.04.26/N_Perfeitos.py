n_desejados = int(input("quantos numeros perfeitos vc deseja encontrar: "))
encontrados = 0
numeros_testados = 2 # começamos do 2 (1 não é perfeito)
print(f'Buscamos os {n_desejados} primeiros números perfeitos.')
while encontrados < n_desejados:
    soma_divisores = 0
    # encontra os divisores do 'numero testado'
    for i in range(1, numeros_testados):
        if numeros_testados %i == 0:
            soma_divisores += i
    
    #verificar se a some é igual ao número
    if soma_divisores == numeros_testados:
        encontrados += 1
        print(f'{encontrados}° número perfeito encontrado: {numeros_testados}')
    numeros_testados += 1
    
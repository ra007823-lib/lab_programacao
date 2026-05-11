while True:
    num=int(input('*\nDigite um numero inteiro positivo: '))
    qtde_divisores = 0
    print(f'divisores de {num}:',end=" ")
    #looping para encontrar e exibri divisores
    for i in range(1,num+1):
        if num % i==0:
            print(i,end=" ")#exibe os divisores
            qtde_divisores += 1
    #verificar se o numero é primo baseado no verificador
    print()
    if qtde_divisores == 2:
        print(f'conclusão: o numero {num} é primo!')
    else:
        print(f'conclusão: o numero {num} não é primo(possui {qtde_divisores} divisores!)')
    # opção de inserir um novo numero
    continuar = input('\nDeseja analisar outro numero?(s/n):').upper()
    if continuar != 's':
        break
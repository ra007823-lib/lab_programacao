while True:

    num = int(input('digite um numero para teste: '))
    div = []

    for i in range(1, num + 1):
        if num % i == 0:
            div.append(i)
    print(div)
    if len(div) == 2:
        print('é primo!')
    else:
        print('não é primo!')

    continuar = input('deseja continuar: (s/n) ').lower()

    if continuar == 's':
        print('ok vamos continuar')
    else:
        print('até mais!')
        break
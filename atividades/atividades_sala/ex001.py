while True:
    num = int(input('digite um numero para teste (0 para sair): '))
    if 10 < num < 50:
        print('dado valido!')
    if num == 0:
        break
    else:
        print('dado invalido')
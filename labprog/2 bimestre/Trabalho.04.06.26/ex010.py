senha = input('cadastre sua senha: ')
entrada = input('digite sua senha: ')

if entrada != senha:
    for i in range(2):
        print('tente novamente')
        entrada = input('digite sua senha: ')
        if entrada == senha:
            print('acesso liberado')
            break
        else:
            print('acesso negado')
else:
    print('acesso liberado')
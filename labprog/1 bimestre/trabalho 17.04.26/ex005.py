num_placa = input('digite o numero da sua placa')
ultimo = num_placa[-1]

if ultimo in '12':
    print('probido na segunda, pois o final é terminado em 1 ou 2.')
elif ultimo in '34': 
    print('proibido na terça, pois o final é terminado em  3 ou 4.')
elif ultimo in '56': 
    print('proibido na quarta, pois o final é terminado em 5 ou 6.')
elif ultimo in '78': 
    print('proibido na quinta, pois o final é terminado em 7 ou8.')
elif ultimo in '90':
    print('proibido na sexta, pois o final é terminado em 9 ou 0.')
else:
    print('erro!')
    
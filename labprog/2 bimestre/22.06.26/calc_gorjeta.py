def calc_gorjeta(valor, percentual=10):
    return valor * percentual/100

gorjeta = calc_gorjeta(400)
print(f'o valor da gorjeta de 10% de uma conta de R$400,00 é {gorjeta}')
gorjeta = calc_gorjeta(400,5)
print(f'o valor da gorjeta de 5% de uma conta de R$400,00 é {gorjeta}')
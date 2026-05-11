cliente = input('Vocẽ é um cliente: Comum(c), Premium(p) ou Vip(v)').upper
valor_compra = float(input('Informe o valor da compra: '))

if cliente == 'C':
    print('infelizmente não sera aplicado desconto.')
if cliente == 'P':
    print(f'o desconto sera de R${(valor_compra *0.1):.2f} e o total a ser pador de R${(valor_compra - (valor_compra*0.1)):.2f}')
else:
    cliente == 'V'
    print(f'o desconto sera de R${(valor_compra *0.2):.2f} e o total a ser pador de R${(valor_compra - (valor_compra*0.2)):.2f}')

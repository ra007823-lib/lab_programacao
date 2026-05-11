distancia = float(input('qua a distancia em KM que sera entregue a mercadoria: '))
peso = float(input(' qual o peso da mercadoria em KG: '))
frete = 20
valor_dist = 0
valor_peso = 0
if distancia >= 100 or peso >= 10:
    valor_dist = ((distancia - 100)*0.1)
    valor_peso =  ((peso -10)*5)
    total = valor_dist + valor_peso + frete
    print(f'o valor do frete sera de R${total}')
else:
    print(f'frete sera do frete sera de R${frete}')

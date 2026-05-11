p, m, g = 10, 12, 15

quant_p = int(input('informe a quantidade de camisas P que deseja:'))
quant_m = int(input('informe a quantidade de camisas M que deseja:'))
quant_g = int(input('informe a quantidade de camisas G que deseja:'))

valor_total = ((quant_p * p) + (quant_m * m) + (quant_g * g))

print(f'o valor total é de R${valor_total:.2f}')
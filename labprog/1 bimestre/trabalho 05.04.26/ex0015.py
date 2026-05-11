valor_info = int(input('Digite o valor em centavos: '))

moeda1 = moeda050 = moeda025 = moeda010 = moeda005 = moeda001 = 0

while valor_info > 0:
    if valor_info >= 100:
        moeda1 += 1
        valor_info -= 100
    elif valor_info >= 50:
        moeda050 += 1
        valor_info -= 50
    elif valor_info >= 25:
        moeda025 += 1
        valor_info -= 25
    elif valor_info >= 10:
        moeda010 += 1
        valor_info -= 10
    elif valor_info >= 5:
        moeda005 += 1
        valor_info -= 5
    else:
        moeda001 += 1
        valor_info -= 1

print(f'Moedas de 1 real: {moeda1}')
print(f'Moedas de 50 centavos: {moeda050}')
print(f'Moedas de 25 centavos: {moeda025}')
print(f'Moedas de 10 centavos: {moeda010}')
print(f'Moedas de 5 centavos: {moeda005}')
print(f'Moedas de 1 centavo: {moeda001}')
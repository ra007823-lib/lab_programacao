import random
ladoseis = 0
dados = []
for i in range(50):
    resultado =  random.randint(1,6)
    dados.append(resultado)
    if resultado == 6:
        ladoseis +=1
porcen = (ladoseis / 50) * 100
print(f'resultado obtido em 50 tentaivas do lado 6: {ladoseis}')
print(f'a porcentagem obtida foi de: {porcen:.2f}%')
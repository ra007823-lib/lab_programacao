import random
ladoseis = 0
for i in range(50):
    resultado =  random.randint(1,6)
    if resultado == 6:
        ladoseis +=1
print(f'resultado obtido em 50 tentaivas do lado 6: {ladoseis}')


    
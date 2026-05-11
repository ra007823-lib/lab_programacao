import random
contador = 5
num_sorteado = random.randint(0,20)
while contador > 0:  
    num_entrada = int(input('digite um numero de 1 a 20: '))
    if num_entrada > num_sorteado:
        print('o numero esta a baixo.')
    elif num_entrada < num_sorteado:
        print('o numero esta a cima.')
    else:
        num_entrada == num_sorteado
        print(f'você acertou, o numero sorteado era {num_sorteado}')
        break
    contador -=1
if contador == 0 and num_entrada != num_sorteado:
    print(f'limite de tentativas atingido, o numero era {num_sorteado}')
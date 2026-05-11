F1 = []
variaveis = ['x','y','z']
for i in range(3):
    num = float(input(f'F1 - {variaveis[i]}: '))
    F1.append(num)

F2 = []
for i in range(3):
    num = float(input(f'F2 - {variaveis[i]}: '))
    F2.append(num)

RX = F1[0] + F2[0]
RY = F1[1] + F2[1]
RZ = F1[2] + F2[2]

Forca_resultante = (RX,RY,RZ)

print('-'*30)
print(f'A força resultante no espaço 3d é: {Forca_resultante}')
print(f'Componentes individuas -> x: {RX}, y -> {RY}, rz -> {RZ}.')

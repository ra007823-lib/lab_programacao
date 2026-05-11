print('Informe as coordenadas da primeira força: ')

f1 = []

f1.append(float(input('F1 - x: ')))
f1.append(float(input('F1 - y: ')))
f1.append(float(input('F1 - z: ')))

f2 = []

f2.append(float(input('F2 - x: ')))
f2.append(float(input('F2 - y: ')))
f2.append(float(input('F2 - z: ')))

rx = f1[0] + f2[0]
ry = f1[1] + f2[1]
rz = f1[2] + f2[2]

forca_resultante = (rx,ry,rz)

print('-'*30)
print(f'A força resultante no espaço 3d é: {forca_resultante}')
print(f'Componentes individuas -> x: {rx}, y -> {ry}, rz -> {rz}.')
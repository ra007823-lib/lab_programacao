hist = []

while True:
    valor = float(input('digite o valor: '))
    if valor == 0:
        print('\nencerrando')
        break
    hist.append(valor)

#hist= [x for x in hist if x>= 5]

for i in range(len(hist) -1, -1, -1):
    if abs(hist[i]) > -5 and abs(hist[i]) < 5:
        del hist[i]

print('-'*25)
print('O histórico do seu saldo é:')
for valor in hist:
        print('-'*25)
        print(f'\t\033[33mR${valor:.2f}\033[m')
print('\n')
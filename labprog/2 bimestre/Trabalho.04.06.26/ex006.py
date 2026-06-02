capital = float(input('digite quanto deseja investir: '))
rendimento = float(input('digite o juros que sera aplicado: '))

saldo = 0

while True:

    for i in range(12):
  
            saldo += capital
            saldo *= (1+rendimento/100)

            print(f'o valor total do investimento no {i+1}° mês foi de R${saldo:.2f}')
    
    cont = input('deseja continuar: (s/n)').lower()
    
    if cont == 's':
        print('resultado de mais um ano de investimento: ')
    if cont =='n':
        print('Até a proxima.')
        break
moeda001, moeda005, moeda010, moeda025, moeda050, moeda1 = 0.001 , 0.005, 0.010, 0.025, 0.050, 1

valor001 = int(input('informe a quantidade de moedas de 1 centavo: '))
valor005 = int(input('informe a quantidade de moedas de 5 centavos: '))
valor010 = int(input('informe a quantidade de moedas de 10 centavos: '))
valor025 = int(input('informe a quantidade de moedas de 25 centavos: '))
valor050 = int(input('informe a quantidade de moedas de 50 centavos: '))
valor1 = int(input('informe a quantidade de moedas de 1 real: '))

total = (valor001*moeda001)+(valor005*moeda005)+(valor010*moeda010)+(valor025*moeda025)+(valor050*moeda050)+(valor1*moeda1)

print(f'o total economizado foi de R${total:.2f}')
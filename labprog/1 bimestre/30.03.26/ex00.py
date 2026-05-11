invest_mes = float(input('investimento: '))
taxa_juros = float(input('juros mes: '))/100
saldo = 0
ano_atual = 1
while True:
    for mes in range(1,13):
        saldo += invest_mes
        saldo += saldo* taxa_juros

    print(f'\nSaldo do investimento após{ano_atual} ano($): R${saldo:.2f}')
    opção = input("deseja processar mais 1 ano?(S/N): ").upper()
    if opção == "S":
        ano_atual +=1
    else:
        print("simulação finalizada!")
        break
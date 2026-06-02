valor_ant = 0
valor_atual = 1

busca = int(input('digite qual o valor deseja calcular: '))

for i in range (busca):
    print(valor_atual)
    valor_ant, valor_atual = valor_atual, valor_ant + valor_atual
    

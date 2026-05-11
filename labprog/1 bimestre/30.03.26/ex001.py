n_termos = int(input('NUMERO DE TERMOS: '))

a, b = 0,1
contador = 0
print('sequencia de fibonacci')
while contador <= n_termos:
    print(a,end=','if contador < n_termos else"")
    #logica de atualização f(n) = f(n-1) + f(n-2)
    proximo = a + b #1
    a = b #1
    b = proximo #1
    contador +=1 
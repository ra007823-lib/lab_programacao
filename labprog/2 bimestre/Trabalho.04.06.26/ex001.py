vetor = [1,2,3,4,5,6,7,8,9,10]

for i in range(10):
    for x in range(10):
        result = vetor[i]*x
        print('-'*40)
        print(f'o resultado da tabuado {i+1} é: {result}')
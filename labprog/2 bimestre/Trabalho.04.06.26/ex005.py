num_perf = int(input('digite quantos numeros deseja testar: '))

encon = 0
num = 1

while encon < num_perf:
    soma = 0
    for i in range(1, num):
        if num % i == 0:
            soma += i

    if soma == num:
        print(num)
        encon +=1
    num +=1


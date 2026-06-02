num = int(input('informe um numero para teste: '))
base = num
resultado =[]
while num != 1:
    if num %2 == 0:
        num = num // 2
        resultado.append(num) 
    else:
        num = num * 3 + 1
        resultado.append(num)
print(f'\033[94mo resultado obtido atraves desse processor matematico foi de\033[0m :\033[92m\033[47m{base} = {resultado}\033[0m')
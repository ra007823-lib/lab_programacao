entrada = input('digite a string contendo letras e numeros: ')

num = 0

for n in entrada:
    if n >= '0' and n <= '9':
        num+=1
print(num)
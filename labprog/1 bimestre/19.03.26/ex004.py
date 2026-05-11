#somar pares.py
num = int(input("numero 1: "))
num1 = int(input("numero 2: "))
contador_pares = 0
soma = 0
while num <= num1:
    if(num%2 == 0):
        contador_pares += 1 
        soma = num + soma
    num = num + 1    
print(contador_pares)
print(f'a soma é {soma}')

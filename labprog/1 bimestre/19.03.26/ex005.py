#fatorial.py
numero = int(input("digite um numero interio positivo: "))
fatorial = 1
while numero > 0:
    fatorial *= numero
    numero -= 1
print(f'o fatorial desse numero é {fatorial}')
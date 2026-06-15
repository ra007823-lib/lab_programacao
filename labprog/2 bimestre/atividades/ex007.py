pares = []
impares = []

while len(pares) + len(impares) < 10:
    numero = int(input("Digite um número inteiro: "))

    if numero in pares or numero in impares:
        print("Número já informado! Digite outro.")
        continue
    
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("\nLista de pares:", pares)
print("Lista de ímpares:", impares)
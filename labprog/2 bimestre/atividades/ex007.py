pares, impares = [], []

while len(pares) + len(impares) < 10:
    n = int(input("Digite um número inteiro: "))

    if n in pares + impares:
        print("Número já informado!")
        continue

    (pares if n % 2 == 0 else impares).append(n)

print("Lista de pares:", pares,'\nLista de ímpares:', impares)
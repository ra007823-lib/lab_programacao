#eleabore um programa que leia 10 numeros inteiros do teclado. á medida que os numeros forem lidos, os pares devem ser inseridos em uma lista chamada pares e os impares em uma lista chamada impares. porem se o usuario digitar um numero que já foi inserido anteriormente em qualquer uma das listas, o programa deve recusar o numero e pedir para digitar outro.

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

print("Lista de pares:", pares)
print("Lista de ímpares:", impares)
numero = int(input("Digite um número inteiro positivo: "))

produto = 1

for i in range(1, numero + 1):
    if i % 2 != 0:
        produto *= i

print("Resultado do produto dos números ímpares:", produto)
texto = input("Digite uma frase: ")
qtd_proib = int(input('Digite quantas palavras deseja priobir na frase: '))
proibidas = []

for i in range(qtd_proib):

    a = input("Digite as palavras priobidas: ")
    proibidas.append(a)

palavras = texto.split()

for i in range(len(palavras)):
    if palavras[i] in proibidas:
        palavras[i] = "***"

resultado = " ".join(palavras)

print(resultado)
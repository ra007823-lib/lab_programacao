frase = input("Digite uma frase: ")

vetor = []
palavra = ""

for caractere in frase:
    if caractere != " ":
        palavra += caractere
    else:
        if palavra != "":
            vetor.append(palavra)
            palavra = ""

if palavra != "":
    vetor.append(palavra)

print(vetor)
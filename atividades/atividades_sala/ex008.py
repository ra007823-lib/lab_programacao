#sem usar comando .split() nativo Python, faça um programa que receba uma frase curta separada por espaços(ex: 'Banco de dados')  e transforme cada palavra em um elemento de um vetor (ex:['Banco','de','dados']).
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
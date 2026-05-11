frase = input('Digite uma frase: (ex: Aula 01 de SQL) ')
contador_letra = 0
contador_numero = 0
for caracter in frase:
    if caracter.isalpha():#isalpha é usado para contar letras
        contador_letra +=1
    elif caracter.isdigit():#isdigit é usado para contar numeros
        contador_numero +=1

print(f'na sua frase existem {contador_letra} letras e {contador_numero} números')


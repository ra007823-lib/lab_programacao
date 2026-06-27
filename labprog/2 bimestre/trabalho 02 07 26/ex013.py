nome = input("Digite o nome completo: ")

partes = nome.split()

sobrenome = partes[-1].upper()
restante = " ".join(partes[:-1])

print(sobrenome + ", " + restante)
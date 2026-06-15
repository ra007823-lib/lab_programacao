while True:
    numero = int(input("Digite um numero: "))
    if numero == 0:
        print("Saindo do programa...")
        break
    elif 10 <= numero <= 50:
        print("Dado valido.")
    else:
        print("Dado invalido.")
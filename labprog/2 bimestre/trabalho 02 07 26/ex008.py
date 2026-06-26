def validação(senha):
    maiuscula = False
    minuscula = False
    numero = False
    especial = False

    for validacao in senha:
        if validacao.isupper():
            maiuscula = True
        elif validacao.islower():
            minuscula = True
        elif validacao.isdigit():
            numero = True
        elif not validacao.isalnum():
            especial = True

    if len(senha) < 8:
        print("Erro: a senha deve ter no mínimo 8 caracteres.")
    elif not minuscula:
        print("Erro: deve conter pelo menos uma letra minúscula.")
    elif not maiuscula:
        print("Erro: deve conter pelo menos uma letra maiúscula.")
    elif not numero:
        print("Erro: deve conter pelo menos um número.")
    elif not especial:
        print("Erro: deve conter pelo menos um caractere especial.")
    else:
        print("Senha segura!")

entrada = input('Digite sua senha: ')
validação(entrada)
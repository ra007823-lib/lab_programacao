def permitir_acesso(ano):
    entrada = 2026 - ano
    acesso = []
    if entrada < 18:
        acesso = False
    else:
        acesso = True
    if acesso == True:
        return 'Bem vindo'
    else:
        return'Bloqueio'

nascimento = int(input('Boa noite, informe sua data de nascimento para que possamos avaliar se sua idade é compativel para a entrada no estabelecimento: '))
print(permitir_acesso(nascimento))
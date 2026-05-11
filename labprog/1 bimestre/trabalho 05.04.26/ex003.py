orig = float(input("informe o valor original: "))
desc = float(input("informe a porcentagem de desconto: "))# o desconto deve ser informado na forma de decimais!
valor = orig * (1 - desc)
print(f'o valor a ser pago é de: {valor:.2f}')
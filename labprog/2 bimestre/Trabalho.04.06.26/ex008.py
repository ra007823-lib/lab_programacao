x = int(input("Digite o dividendo (x): "))
y = int(input("Digite o divisor (y): "))
div = x
divisor = y
quociente = 0

while x >= y:
    x -= y
    quociente += 1

resto = x

print(f"O resultado do {div} / {divisor} = {quociente}, com resto {resto}.")

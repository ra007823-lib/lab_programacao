massa = float(input("informe seu peso: "))
altura = float(input("informe sua altura: "))

imc = massa / (altura**2)

if imc < 18.5:
    categoria = "abaixo do peso"
elif imc <= 24.99: 
    categoria = "saudavel"
elif imc <= 29.99:
    categoria = "peso em excesso"
elif imc <= 34.99: 
    categoria = "obesidade grau 1"
elif imc <= 39.99: 
    categoria = "obesidade grau 2"
else:
    categoria = "obesidade grau 3"

print("-"*30)#passa um traço
print(f"seu imc é: {imc:.2f}")
print(f"sua classicação é: {categoria}")
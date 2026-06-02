import random

num = random.randint(1,100)
contador = 0
for i in range(10):
    x = int(input("Descubra o número secreto: "))
    contador +=1
    if x > num:
        print("O número secreto está abaixo")
    elif x < num:
        print("O número secreto está acima")
    else:
        print(f"Você acertou o número secreto: {num}")
        break

if contador <= 5:
    print("Ganhou um bônus.")
elif contador <= 9:
    print("Acertou, mas sem direito ao bonus de 5 tentativas")
else:
    print("não foi dessa vez.")
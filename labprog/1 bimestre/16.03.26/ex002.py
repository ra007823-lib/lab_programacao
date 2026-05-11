idade = int(input("leia idade: "))

if (idade < 5 ):
    categoria = ("muito jovem")
elif (idade <= 7):
    categoria = ("infantil a")
elif (idade <= 11):
    categoria = ("infantil b")
elif (idade <= 17):
    categoria = ("juvenil")
else:
    categoria = ("adulto")

print(f"o atleta pertence a categoria: {categoria}")
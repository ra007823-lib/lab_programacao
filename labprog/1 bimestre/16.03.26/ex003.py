porcentagem = float(input("informe a quantidade de agua: "))

if porcentagem >= 90:
    nivel = "critico"
elif porcentagem >= 50:
    nivel = "adequado"
elif porcentagem >=20:
    nivel ="baixo"
else:
    nivel = "vazio"
print(f"o nivel da agua esta: {nivel}")
# 1 - defina a cosntante fisica( velocidade do som em m/s)

velocidade_som = 340

# leia temp -  temp em segundos

tempo = float(input("digite o tempo entre o clarão e o trovão( em segundos): "))
# processamento
# distancia em metros= velocidade * tempo

distancia_metros = velocidade_som * tempo

# convertendo para KM

distancia_km = distancia_metros / 1000

print(f"O raio caiu a uma distancia aproximada de {distancia_km:.2f} km")
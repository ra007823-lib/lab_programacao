def calc_temp(velocidade,distancia):
    tempo = distancia / velocidade
    return tempo
def calc_dist(temp,velocidade):
    distancia = velocidade * temp
    return distancia
t = calc_temp(10,5)
print(t)
d = calc_dist(5,4)
print(d)

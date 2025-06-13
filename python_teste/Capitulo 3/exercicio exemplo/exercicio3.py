#raio = int(input("Escolha um numero para o Raio: "))
#pi = 3.14159
#circuferencia = 2
#diametro = (2 * raio) * pi
#area = pi * raio ** 2
#print("O Circuferência: ", circuferencia)
#print("O Diamêtro: ", diametro)
#print("A área: ", area)

def calcula_diametro(raio):
    return 2 * raio

def calcula_circuferencia(raio, pi):
    return (2 * raio) * pi

def calculaAreaCircuferencia(pi, raio):
    return pi * (raio ** 2)

#main
pi= 3.14159
raio = int(input("Qual é o valor de raio: "))

diametro = calcula_diametro(raio)
circuferencia= calcula_circuferencia(raio, pi)
area_circuferencia = calculaAreaCircuferencia(pi, raio)

print("O valor do diametro é: ", diametro)
print("O valor da circuferencia: ", circuferencia)
print("O valor da area da circuferencia é: ", area_circuferencia)
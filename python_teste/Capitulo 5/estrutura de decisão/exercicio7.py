def verificarnumero(abacaxi):
    if abacaxi == 0:
        print("E ZERO")
    elif abacaxi > 0:
        print("E positivo")
    else:
        print("E negativo")

n1 = float(input("Digite um número "))

verificarnumero(n1)
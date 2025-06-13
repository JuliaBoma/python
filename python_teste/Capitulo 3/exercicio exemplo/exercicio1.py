def soma(numero, numero2):
    print("O resultado da soma é: ", numero + numero2)

def subtracao(numero, numero2):
    print("O Resultado da subtração é: ", numero - numero2)

def multiplicacao(numero, numero2):
    print("O resultado da multiplicação é: ", numero * numero2)

def divisao(numero, numero2):
    resultado_divisao = numero / numero2
    print("O resultado da divisão é: ",resultado_divisao)

numero = int(input("Digite o 1º número: "))
numero2 = int(input("Digite o 2º número: "))

soma(numero, numero2)
subtracao(numero, numero2)
multiplicacao(numero, numero2)
divisao(numero, numero2)

def calculadora (n1, n2):
    soma = n1 + n2
    print(f"A soma é: {soma}")

    subtracao = n1 - n2
    print(f"A subtração é: {subtracao}")

    divisao = n1 / n2
    print(f"A divisão é: {divisao}")

    multiplicacao = n1 * n2
    print(f"A multiplicação é: {multiplicacao}")

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))

calculadora(n1, n2)
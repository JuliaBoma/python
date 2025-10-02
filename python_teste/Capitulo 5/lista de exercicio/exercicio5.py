def calculaPeso(altura):
    peso = (62.1 * altura) - 44.7
    print(f"Seu peso ideal é {peso}")

altura = float(input("Digite a sua altuta: "))

calculaPeso(altura)
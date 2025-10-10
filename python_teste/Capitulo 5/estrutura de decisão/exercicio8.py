def verificar (numero):
    if (num % 2 == 0 and num % 3 == 0):
        print("O numero é divisivel por 2 e por 3")
    else:
        print(f"O {numero} não é divisivel por 2 e 3")

num = int(input("Digite um número qualquer: "))

verificar(num)
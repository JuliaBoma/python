def verificar5ou3(num):
    if num % 5 == 0:
        print(f"O {num} divisivel por 5")
    elif num % 3 == 0:
        print(f"o {num} divisivel por 3")
    else:
        print(f"O {num} não é divisivel por 5 ou 3")

num = int(input("Digite um numero: "))

verificar5ou3(num)
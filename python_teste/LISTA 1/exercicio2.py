numero = int(input("Digite 5 números: "))
dig1 = numero // 10000
dig2 = (numero % 10000) // 1000
dig3 = (numero % 1000) // 100
dig4 = (numero % 100) // 10
dig5 = numero % 10
print(dig1)
print(dig2)
print(dig3)
print(dig4)
print(dig5)
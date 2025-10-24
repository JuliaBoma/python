maior = 0;
menor = 0;

for i in range (0,6):
    n1 = int(input("Digite um número: "))

    if (i == 0):
        maior = n1
        menor = n1
    if (n1 > maior):
        maior = n1
    elif(n1 < menor):
        menor = n1

print(f"O maior numero é {maior}")
print(f"O menor numero é {menor}")
def soma(n1, n2, n3, n4):
    total = 0

    if(n1 % 2 == 0):
        total+= n1
    if(n2 % 2 == 0):
        total+= n2
    if(n3 % 2 == 0):
        total+= n3
    if(n4 % 2 == 0):
        total+= n4
    return total


def contaPar(n1, n2, n3, n4):
    total = 0

    if(n1 % 2 == 0):
        total+=1
    if(n2 % 2 == 0):
        total += 1
    if(n3 % 2 == 0):
        total += 1
    if(n4 % 2 == 0):
        total += 1

    return total

def main():
    n1 = int(input("Digite a 1° número: "))
    n2 = int(input("Digite a 2° número: "))
    n3 = int(input("Digite a 3° número: "))
    n4 = int(input("Digite a 4° número: "))

    totalSoma = soma(n1, n2, n3, n4)
    totalPares = contaPar(n1, n2, n3, n4)
    media = totalSoma/totalPares
    print(f"A soma dos número é: {totalSoma}")
    print(f"A média dos número é: {media}")

if __name__ == "__main__":
        main()
def numMaior(num1, num2, num3):
    if(num1>num2):
        if(num1>num3):
            print("O" ,num1, "é maior" )

    if(num2>num1):
        if(num2>num3):
            print("O ", num2, "é maior")

    if(num3>num1):
        if(num3>num2):
            print("O ", num3, "é maior")


num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número novamente: "))
num3 = int(input("Digite um número novamente: "))

numMaior(num1,num2, num3)

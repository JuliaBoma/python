def validaIdade (idade):
    if(idade>= 18):
        print("Você é de maior de idade")
    else:
        print("Você é de menor")


idade = int(input("digite a sua idade: "))

validaIdade(idade)
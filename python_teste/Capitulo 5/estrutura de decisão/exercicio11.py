def verificarCodigo(codigo):
    if codigo == 1:
        print("Alimento não-perecível")
    elif codigo > 1 and codigo <= 4:
        print("Alimento perecível")
    elif codigo == 5 or codigo == 6:
        print("Vestuário")
    elif codigo == 7:
        print("Higiene pessoal")
    else:
        print("ERRO!")

codigo = int(input("Digite o código: "))

verificarCodigo(codigo)

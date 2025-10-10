def verificarConsumo(consumo):
    match consumo:
        case "A":
            print(f"MUITO EFICIENTE")
        case "B":
            print(f"EFICIENTE")
        case "C":
            print(f"POUCO EFICIENTE")
        case "D":
            print(f"INEFICIENTE")

def main():
    consumo = input("Qual é o consumo da sua geladeira: ")

    verificarConsumo(consumo)

if __name__ == "__main__":
    main()
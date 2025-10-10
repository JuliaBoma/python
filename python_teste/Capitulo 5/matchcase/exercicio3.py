def verificarFeriado(mes, dia):
    match mes:
        case 1:
            match dia:
                case 1:
                    print(f"Dia {dia} é Ano Novo")
                case _:
                    print("Esse dia não tem feriado")
        case _:
            print("Neste mês não tem feriado")



def main():
    dia = int(input("Selecione um dia: "))
    mes = int(input("Selecione um mês: "))

    verificarFeriado(mes, dia)
if __name__ == "__main__":
    main()
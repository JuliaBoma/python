def calculaKm(inicio,final, litro):
    totalKm = (inicio - final) / litro
    print(f"O valor total do seu KM foi: {totalKm}")

def Lucro(combustivel, valorTotal, litro):
    totalLucro = valorTotal - (litro * combustivel)
    print(f"Seu lucro do dia é : {totalLucro}")

combustivel = float(input("Qual é o preço do combústivel: "))
inicio = float(input("Qual o seu KM do inicio: "))
final = float(input("Qual o seu KM do final: "))
litro = float(input("Quantos litros de combustível foi gasto: "))
valorTotal = float(input("Quantos passageiros foram recebidos: "))

calculaKm(inicio, final, litro)
Lucro(combustivel, valorTotal, litro)
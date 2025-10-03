def calculaMedia(nota1, nota2, nota3, prova):
    somaNota= (nota1+nota2+nota3)/3
    totalbimestral = prova * 0.7
    mediaBimestral = ((somaNota * 0.3) + totalbimestral)
    print(f"A média do Bimestre: {mediaBimestral}")

nota1 = float(input("Qual é a sua primeira nota: "))
nota2 = float(input("Qual é a sua segunda nota: "))
nota3 = float(input("Qual é a terceira nota: "))
prova = float(input("Qual é a sua nota da prova do bimestre: "))

calculaMedia(nota1, nota2, nota3, prova)
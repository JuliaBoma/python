#Função dentro de outra função.
def mostrar_Nome_Inteiro(nome, sobrenome):
    print(nome)
    sobreNome(sobrenome)

def sobreNome(sobrenome):
    print(sobrenome)

nome = "Julia"
sobrenome = "Boma"
mostrar_Nome_Inteiro(nome, sobrenome)
def right_justify(palavra, tamanho_palavra):
    espaco = ' '
    resultado = espaco * (70 - tamanho_palavra)
    return resultado + palavra

palavra = str(input("Digite uma palavra: "))
tamanho_palavra = len(palavra)

justificado = right_justify(palavra, tamanho_palavra) #chama de função recebe argumento

print(justificado)
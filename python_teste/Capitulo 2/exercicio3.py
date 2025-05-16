print('Tempo do primeiro trecho: 8min e 15seg')
minutoPrimeiroTrecho = 8 * 60
segundoPrimeiroTrecho = 15

print("Tempo do segundo trecho em segundos: 7min e 12seg")
minutoSegundoTrecho = (7 * 3) * 60
segundosSegundoTrecho = 12 * 3

print("Tempo do terceiro trecho: 8min e 15seg")
minutoTerceiroTrecho = 8 * 60
segundoTerceiroTrecho = 15

#Soma o total de minutos e Converte todos os minutos em segudos.
totalTempoTodosTrechosMinutos = (minutoPrimeiroTrecho + minutoSegundoTrecho + minutoTerceiroTrecho) / 60

#Soma valor total dos segundos.
totalTempoSegundoTrecho = (segundoPrimeiroTrecho + segundosSegundoTrecho + segundoTerceiroTrecho)

restanteMinutos = int(totalTempoSegundoTrecho / 60)
restanteSegundos = totalTempoSegundoTrecho % 60

totalMinutos = totalTempoTodosTrechosMinutos + restanteMinutos
totalSegundos = restanteSegundos

print("Soma de tempo de todos os trechos: ", totalMinutos, "Minutos")
print("Soma de tempo de todos os trechos: ", totalSegundos, "Segundos")

horaSegundosInicial = (6 * 60) * 60
minutoSegunodsInicial = (52*60)
horarioInicialSegundos = horaSegundosInicial + minutoSegunodsInicial

tempoTrechoMinutosSegundos = totalMinutos * 60

horasChegadas = int(((horarioInicialSegundos + tempoTrechoMinutosSegundos) / 60) / 60)
minutosChegadas = int(((minutoSegunodsInicial + tempoTrechoMinutosSegundos) / 60) % 60)

print("O tempo de Chegada foi de: ", horasChegadas, ":", minutosChegadas, restanteSegundos)

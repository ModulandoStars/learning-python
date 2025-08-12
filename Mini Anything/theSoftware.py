import chooseThings as anything
import os

clear = lambda: os.system("cls")
clear()

quantEventos = int(input("quantos eventos você quer que ocorra: "))
eventosFeitos = 0

if quantEventos > 0:
    eventosFeitos = quantEventos
    print('---- start ----')


while quantEventos <= 0:
    print("menor que 1 não dá ne parça")
    quantEventos = int(input("quantos eventos você quer que ocorra: "))
    if quantEventos > 0:
        eventosFeitos = quantEventos
        print('---- start ----')
        break

while eventosFeitos > 0:
    anything.event(numPessoas=1, numLugares=1)
    eventosFeitos -= 1
else:
    print("---- end ----")
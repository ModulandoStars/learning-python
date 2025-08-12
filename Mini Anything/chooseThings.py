import random as rand

pessoas = (
    "Daniel",
    "Julio",
    "Eric",
    "Mirella",
    "Nicole",
    "Agatha"
)

acoesEmLugares = (
    "causou um incêndio em",
    "foi expulso de",
    "ganhou o jogo de",
    "fez o inferno em",
    "tacou o putero na",
)

lugares = (
    "escola",
    "casa",
    "centro da cidade",
    "puteiro",
    "clube de strippers"
)

def event(numPessoas, numLugares):
    
    pessoaEscolhida = pessoas[rand.randint(0, len(pessoas)-1)]
    eventoAleatorio = acoesEmLugares[rand.randint(0, len(acoesEmLugares)-1)]
    lugarAleatorio = lugares[rand.randint(0, len(lugares)-1)]

    if numPessoas > len(pessoas)-1 / numLugares > len(lugares)-1:
        print("Um dos valores está acima da quantidade do 'tuple'")
        
    else:
        print(pessoaEscolhida + " " + eventoAleatorio + " " + lugarAleatorio)

    
#   print("o numero de pessoas são: "+str(len(pessoas))+ " sendo eles " + pessoas)
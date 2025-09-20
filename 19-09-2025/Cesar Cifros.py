import random

NumAleatorio = random.randint(1,10)
alfabeto = ["a", "b", "c", "d","e", "f",
            "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", 
            "s", "t", "u", "v", "w", "x",
            "y", "z"]

def IsNumEven(num):
    if num % 2 == 0:
        return True
    #print("é par") # Even 
    else:
        return False
    #print("é impar") # Odd

Letra = 0

try:
    EscolhaDoUsuario = input("Escolhe uma letra: ")
    if type(EscolhaDoUsuario) == str:
        Letra = alfabeto.index(EscolhaDoUsuario)
        print(alfabeto[Letra])

    elif type(EscolhaDoUsuario) == int:
        Letra = EscolhaDoUsuario
        print(alfabeto[Letra])

    elif type(EscolhaDoUsuario) == float:
        Letra = int(EscolhaDoUsuario)
        print(alfabeto[Letra])
        
except:
    pass

Palavra = input("Palavra: ")
StringLeft = len(Palavra)

PalavaEmNumeros = []
while StringLeft > 0:
    if Palavra[StringLeft-1] == " ":
        PalavaEmNumeros.insert(0, "space")
    elif Palavra[StringLeft-1] not in alfabeto:
        PalavaEmNumeros.insert(0, 'invalid')
    else:
        PalavaEmNumeros.insert(0, alfabeto.index(Palavra[StringLeft-1])) 
    StringLeft -= 1
#print(PalavaEmNumeros)

Diferenca = random.randint(-5,5)
while Diferenca == 0:
    Diferenca += random.randint(-1,1)

Codigo = PalavaEmNumeros
print("antes da mudança")
print(Codigo)
ListAmount = len(Codigo)


RandomEffect = random.randint(1,5)

while ListAmount > 0:
    if Codigo[ListAmount-1] == "space" or Codigo[ListAmount-1] == 'invalid':
        ListAmount -= 1
        continue
    
    NumEven = False
    if ListAmount % 2 == 0:
        NumEven = True
    else:
        NumEven = False

    if NumEven == True:
        Codigo[ListAmount-1] += RandomEffect
        pass
    else:
        Codigo[ListAmount-1] -= RandomEffect
        pass
    ListAmount -= 1

print("depois da mudança")
print(Codigo)
print('o número aleatório é' + str(RandomEffect))
def ConverterNumStr(List):
    global alfabeto
    print(alfabeto)
    ListLength = len(List)
    print(ListLength)

    convertedList = []
    while ListLength > 0:
        while List[ListLength-1] >= len(alfabeto)-1:
            List[ListLength-1] -= 26
            print("ultrapassou")
        if List[ListLength-1] == "space":
            convertedList.insert(0, " ")
            ListLength -= 1
            continue
        elif List[ListLength-1] == "invalid":
            ListLength -= 1
            continue
        elif len(alfabeto) >= List[ListLength-1] >= -1:
            convertedList.insert(0, alfabeto[List[ListLength-1]])
        else:
            ListLength -= 1
            continue
        ListLength -= 1

    ListLength = len(List)
    print(convertedList)
    print(len(convertedList))
    text = ""
    while ListLength > 0:
        text = convertedList[ListLength-1] + text
        ListLength -= 1
    print(text)

    return convertedList


print(ConverterNumStr(Codigo))



#print(alfabeto[Letra])
#print(alfabeto[Letra+num])
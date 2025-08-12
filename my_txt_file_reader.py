import os

clear = lambda: os.system("cls")
clear()

print("welcome to the txt file reader - modulandostars 2025")


def readTehFile(file):
    try:
        print("reading '"+file+"' as text...")
        textFile = open(file, "rt")
    except:
        askForFile(input("algo deu errado, tente novamente: "))
    else:
        print(textFile.read())
        textFile.close()
#        askForFile(input("especifique um caminho pra um arquivo de texto pls: "))



def askForFile(path):
    print("o arquivo é: '" + path + "', está correto? (y/n)")
    yesOrNah = input("")

    if yesOrNah == "y":
        readTehFile(path)

    elif yesOrNah == "n":
        askForFile(input("especifique um caminho pra um arquivo de texto pls: "))

#askForFile(input("especifique um caminho pra um arquivo de texto pls: "))
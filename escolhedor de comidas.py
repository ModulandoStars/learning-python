def theQuestion():   
    print("levamos isso muito a sério sabe.. Menu: " \
    "1- Hamburginho yummy " \
    "2- batatinhas fritas " \
    "3- coca cola :3 " \
    "4- Pepsi " \
    "5- Pudim ")

option1 = "Hamburginho yummy"
option2 = "batatinhas frita"
option3 = "coca cola :3"

userOption = ""

theQuestion()

userOption = input("pedimos que você escolha entre uma dessas opções:")

if int(userOption) == 1:
    print("yay you chose " + option1)
    theQuestion()
elif int(userOption) == 2:
    print("yay you chose " + option2)
    theQuestion()

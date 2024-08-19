import random 
while True:
    def sintax():
        randomchose = random.randint(1,3)

    def choise():
        ("Pedra","Papel","Tesoura")


    if sintax() == 1:
        choise() == "Pedra"
    elif sintax == 2:
        choise() == "Papel"
    else:
        choise() == "Tesoura"
    
    print("Vamos começar!")
    print("Pedra Papel Tesoura..")

    opc = input("Qual voce vai escolher? ")

    if opc == "Pedra" and choise() == 3:
        print("Ganhou!")
    elif opc == "Pedra" and choise() == 1:
        print("Empate.")
    else:
        print("Perdeu..")
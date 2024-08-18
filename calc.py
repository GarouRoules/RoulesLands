
def adicao(x,y):
    return x + y

def subtracao(x,y):
    return x - y

def multiplicacao(x,y):
    return x * y

def divisao(x,y):
    if y == 0:
        print("Erro,divisao por 0")
    return x / y

def calculo():
    while True:
        print("1.Adição")
        print("2.Subtração")
        print("3.Multiplicação")
        print("4.Divisão")

        escolha = input("Escolha uma dessas opçoes: ")

        if escolha in ("1","2","3","4"):
            num1 = float(input("Escolha o primeiro valor: "))
            num2 = float(input("Escolha o segundo valor: "))
            if escolha == "1":
                print(f"{adicao(num1, num2)}")
            if escolha == "2":
                print(f"{subtracao(num1, num2)}")
            if escolha == "3":
                print(f"{multiplicacao(num1, num2)}")
            if escolha == "4":
                print(f"{divisao(num1, num2)}")
            
        else:
                print("Opção invalida")
    
    
calculo()
    



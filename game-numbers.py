
#Base
import random
def game():
    number_random = random.randint(1,100)
    attempts = 0

#Game
    print("Bem Vindo ao Game Numbers")
    print("Estou pensando em um numero de 1 a 100.")

    while True:
        attempt = int(input("Qual numero eu pensei? "))
        attempts +=1
    
        if attempt < number_random:
            print("Muito Baixo,Tente um numero mais alto!")
        
        elif attempt > number_random:
                print("Muito Alto,Tente um numero mais baixo!")
        
        else:
            print(f"Parábens! Você tentou {attempts} vezes!")
            break

    gameloud = input("Deseja jogar novamente?(s/n): ").lower()
    if gameloud == 's':
            game()
    else:
            print("Obrigado por jogar!")
            
game()
import random


def jogar():

    print("********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("********************************\n")

    numero_secreto = random.randrange(1, 100)
    total_de_tentativas = 0
    pontos = 1000

    print("O computador sorteou um número secreto!!\n")
    print("Tente adivinhá-lo!!\n")

    nivel = int(input("---> Escolha em qual nivel voce deseja jogar: (1)FACIL, (2)MEDIO, (3)DIFICIL: "))

    facil = nivel == 1
    medio = nivel == 2
    dificil = nivel == 3

    if(facil):
         total_de_tentativas = 20
         print("\nNível escolhido:")
         print(" ----- FÁCIL ----- \n")
         print("Voce tera 20 tentativas para acertar o numero secreto\n")
    elif(medio):
        total_de_tentativas = 10
        print("\nNível escolhido:")
        print(" ----- MÉDIO ----- \n")
        print("Voce tera 10 tentativas para acertar o numero secreto\n")
    elif(dificil):
         total_de_tentativas = 5
         print("\nNível escolhido:")
         print(" ----- DÍFICIL ----- \n")
         print("Voce tera 5 tentativas para acertar o numero secreto\n")

    count = 1
    pontos = 1000

    print(f"\n +++ PONTUAÇÃO INICIAL --->  {pontos}\n")

    for tentativa in range(1, total_de_tentativas +1):
        print(f"\n-> Tentativa {count} de {total_de_tentativas}:")
        chute_str = input("Digite um numero entre 1 e 100 ->  ")
        chute = int(chute_str)
        if(chute < 1 or chute > 100):
            print("\nVOCE DEVE DIGITAR UM NUMERO ENTRE 1 E 100!")
        else:
            count = count + 1

            acertou = chute == numero_secreto
            maior = chute > numero_secreto
            menor = chute < numero_secreto

            if(acertou):
                print(f"\n\n--- ----- PARABÉNS!! ----- ---")
                print(f"Voce acertou e finalizou o jogo com {round(pontos)} ")
                break

            else:
                if(maior):
                    print("Voce errou! Seu numero é maior que o numero secreto.")

                elif(menor):
                    print("Voce errou! Seu numero é menor que o numero secreto.")

            if(tentativa == total_de_tentativas):
                print("\nVOCE NÃO ADIVINHOU O NUMERO SECRETO!!")
                print(f"O numero secreto era {numero_secreto}\n")

            pontos = abs(pontos - chute)/3


    print(f"+++ PONTUAÇÃO ATUAL --->  {round(pontos)}\n")

    print("************")
    print("FIM DO JOGO!")
    print("************")

if __name__ == "__main__":
    jogar()

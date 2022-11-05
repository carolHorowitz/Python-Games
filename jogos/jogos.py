import forca
import adivinhacao


def escolhe_jogo():
    jogo = int(input("Digite 1 para jogar forca e 2 para jogar adivinhação:"))

    if jogo == 1:
        print("Bem vindo ao jogo da FORCA!")
        forca.jogar()
    elif jogo == 2:
        print("Bem vindo ao jogo de ADIVINHAÇÃO!")
        adivinhacao.jogar()

    #print("************")
    #print("FIM DO JOGO!")
    #print("************")


if __name__ == "__main__":
    escolhe_jogo()

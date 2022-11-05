import random

def jogar():
    msg_abertura()

    #carrega todas as palavras do arquivo
    carrega_palavras()

    #seleciona uma palavra dentro do arquivo de palavras
    numero = input('Digite um numero de 0 a 7:')

    palavra_secreta = carrega_palavra_secreta(numero)

    #carrega espaços vazios de acordo com a palavra secreta
    letras_certas = inicializa_letras_certas(palavra_secreta)

    tentativas = 2 * len(palavra_secreta)
    print("\nA palavra secreta é {}:\n".format(letras_certas))
    print('Você tem {} tentativas para descobrir a palavra secreta!\n'.format(tentativas))

    chutes_realizados = []

    while (tentativas >= 0):
        chute = recebe_chute(chutes_realizados)

        if (chute in palavra_secreta):
            letras_certas = marca_chute_correto(chute, letras_certas, palavra_secreta)
            if ("_" not in letras_certas):
                msg_vencedor()
                break

        if (chute not in palavra_secreta):
            letras_certas = marca_chute_errado(tentativas, letras_certas)


     
def msg_abertura():
    print("***************************")
    print("BEM VINDO AO JOGO DA FORCA!")
    print("***************************")

def inicializa_letras_certas(palavra):
    return ['_' for letra in palavra]

def carrega_palavra_secreta(numero):
    return carrega_palavra(numero).upper()

def carrega_palavras():
    return array_de_palavras()

def carrega_palavra(index):
    return array_de_palavras()[int(index)]

def array_de_palavras():
    arquivo = open('palavras.txt', 'r')
    palavras = []
    for palavra in arquivo:
        #palavra = palavra.strip
        palavras.append(palavra.strip())
    arquivo.close()
    return palavras

def recebe_chute(chutes_realizados):
    chute = input('Digite uma letra:\n')
    chute = chute.upper().strip()
    chutes_realizados.append(chute)
    print('letras chutadas: ', chutes_realizados)
    return chute

def marca_chute_correto(chute, letras_certas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_certas[index] = letra
            print(letras_certas)
        index += 1

    return letras_certas

def marca_chute_errado(tentativas, letras_certas):   
    print('\n❌ A letra escolhida não existe na palavra secreta. Você ainda possui {} tentativas.'.format(tentativas -1))
    tentativas -= 1
    print(letras_certas)
    if (tentativas == 0):
        print('\nSuas chances acabaram!! Você não descobriu a palavra secreta.')
        print(' ---------------------- FIM DE JOGO -------------------------')
    return letras_certas

def msg_vencedor():
    print('\nParabéns!!! Você descobriu a palavra secreta!!')
    print('---------------- FIM DE JOGO -----------------')

if __name__ == "__main__":
    jogar()

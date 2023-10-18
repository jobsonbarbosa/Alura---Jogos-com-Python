def jogar():
    print("********************************")
    print("Jobs Play - Jogo da Forca")
    print("********************************")

    palavra_secreta = "abacate"

    enforcou = False
    acertou = False
    #Enquanto não enforcou E não acertou
    while(not enforcou and not acertou):

        chute = input("Digite a letra: ")
        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                print("Letra {} encontrada da posição {}" .format(letra, index))
            index = index + 1
        print("jogando....")

    print("Fim do jogo")


if(__name__ == "__main__"):
    jogar()

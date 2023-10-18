def jogar():
    print("********************************")
    print("Jobs Play - Jogo da Forca")
    print("********************************")

    palavra_secreta = "abacate"
    letras_acertadas = ["_", "_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False
    print(letras_acertadas)
    #Enquanto não enforcou E não acertou
    while(not enforcou and not acertou):

        chute = input("Digite a letra: ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1
        print(letras_acertadas)

    print("Fim do jogo")


if(__name__ == "__main__"):
    jogar()

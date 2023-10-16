print("********************************")
print("Jobs Play - Jogo da Forca")
print("********************************")

palavra_secreta = "abacatee"
lista_letras = []

index = 0
for l in palavra_secreta:
    print(index)
    letra = input("Digita um letra: ")

    if l.upper() == letra.upper():

        lista_letras[index] = l
        print("contem")
        print(lista_letras[index])
    else:
        print("Não contem")
    index = index + 1
#print(lista_letras)

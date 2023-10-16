nome = "Jobson"
letra = input("letra: ")
for n in nome:
    print(letra)
    if letra.upper() == n.upper():
        print("Contem")
    else:
        print("não contem")
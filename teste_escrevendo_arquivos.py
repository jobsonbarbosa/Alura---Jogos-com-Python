
arquivo = open("palavra.txt", "w", encoding="utf-8")

arquivo.write("laranja\n")

arquivo.close()

arquivo = open("palavra.txt", "a")
arquivo.write("abacaxi\n")
arquivo.close()

arquivo = open("palavra.txt", "r", encoding="utf-8")
for linha in arquivo:
    print(linha)
arquivo.close()
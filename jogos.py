import adivinhacao
import forca

print("********************************")
print("Bem vindo ao Jobs Games")
print("********************************")


jogo = int(input("\nEscolha o jogo - (1)Adivinhação (2)Forca : "))

if(jogo == 1):
    print("Iniciando Jogo de Adivinhação")
    adivinhacao.jogar()
elif(jogo == 2):
    print("Iniciando Jogo da Forca")
    forca.jogar()
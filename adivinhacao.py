import random

print("********************************")
print("Jobs Play - Adivinhe o Numero")
print("********************************")

numero_aletorio = random.randrange(1, 101)
facil = 15
medio = 10
dificil = 5
tentativas = 0
rodadas = 1

print(numero_aletorio)

print("Escolha o Nivel")
print("(1)Difícil (2)Médio (3)Fácil:  ")
niveis = int(input("Digite o nível: \n"))

if niveis == 1:
    tentativas = dificil
elif niveis == 2:
    tentativas = medio
elif niveis == 3:
    tentativas = facil

while(niveis > 0):

    print("Voce esta {} de  {} tentativas" .format(rodadas, tentativas))

    numero_digitado = int(input("Digite um número: "))

    if(numero_digitado == numero_aletorio):
        print("você acertou")
        break
    elif (numero_digitado > numero_aletorio):
        print("O numero {} que voce digitou é maior que o numero secreto" .format(numero_digitado))
    elif(numero_digitado < numero_aletorio):
        print("O numero {} que voce digitou é menor que o numero secreto" .format(numero_digitado))
    else:
        print("Número invalido. Digite um numero ente 1 e 100")
    rodadas = rodadas + 1

    if(rodadas > tentativas):
        print("Voce perdeu! ")
        print("Não há mais tentativas.")
        break
print("Fim do jogo...")





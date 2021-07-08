import adivinhacao
import forca

def escolhe_jogo():
  print("*******************************")
  print("*******Escolha seu jogo********")
  print("*******************************")
  print("(1) Forca (2) Adivinhação")

  jogo = int(input("Qual jogo: "))
  jogos = [adivinhacao.jogar, forca.jogar]
  if(jogo > len(jogos) and jogo < 0):
    print("Valor errado")
  else:
    jogos[jogo -1]()

if(__name__ == '__main__'):
  escolhe_jogo()

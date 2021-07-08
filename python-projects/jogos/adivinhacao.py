import random

def jogar():
  print("*******************************")
  print("Bem vindo ao jogo de Advinhação")
  print("*******************************")

  numero_secreto = random.randrange(1,101);
  random.random()
  niveis = [20,10,5]
  pontos = 1000
  
  print("Qual a dificuldade? ")

  print("(1) Facil, (2) Médio, (3) Dificíl")

  nivel = int(input("Digite o nivel: "))

  total_tentativas = niveis[nivel - 1]

  for rodada in range(1,total_tentativas+1):
    print("Tentativa {} de {}".format(rodada,total_tentativas))
    
    chute_srt = input("Digite um numero entre 1 e 100: ")
    chute = int(chute_srt)
    print("Vc digitou",chute)
    if(chute < 1 or chute > 100):
      print("Numero invalido, o seu numero deve estar entre 1 e 100")
      continue

    if(numero_secreto == chute):
      print("Você acertou!!!")
      print("Sua pontuação foi de: {}".format(pontos))
      break
    else:
      if(numero_secreto < chute):
        print("Erouu, seu chute foi maior que o numero secreto")
      elif(numero_secreto > chute):
        print("Erouu, seu chute foi menor que o numero secreto")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos -= pontos_perdidos
  print('Fim do Jogo')

if(__name__ == '__main__'):
  jogar()

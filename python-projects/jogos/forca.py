from random import randrange



def jogar():

  mensagem_de_abertura()

  palavra_secreta = get_palavra_secreta()
  letras_acertadas = ["_"]*len(palavra_secreta)
  enforcou = False
  acertou = False
  erros = 0

  while(not enforcou and not acertou):
   
    chute = get_chute()
    
    if(chute in palavra_secreta):
        marca_letra_acertada(chute,letras_acertadas,palavra_secreta)
        
    else:
      desenha_forca(erros)
      erros += 1
  
    print(letras_acertadas)
    enforcou = erros ==6
    acertou = "_" not in letras_acertadas

  if(acertou):
    mensagem_ganhador(palavra_secreta)
  else:
    mensagem_perdedor(palavra_secreta)

def mensagem_de_abertura():
  print("*******************************")
  print("* Bem vindo ao jogo de forca *")
  print("*******************************")

def mensagem_ganhador(palavra_secreta = ""):
  print("Parabéns, você ganhou!")
  print("A palavra era {}".format(palavra_secreta))
  print("       ___________      ")
  print("      '._==_==_=_.'     ")
  print("      .-\::      /-.    ")
  print("     | (|:.     |) |    ")
  print("      '-|:.     |-'     ")
  print("        \::.    /      ")
  print("         '::. .'        ")
  print("           ) (          ")
  print("         _.' '._        ")
  print("        '-------'       ")

def mensagem_perdedor(palavra_secreta = ""):
  print("Puxa, você foi enforcado!")
  print("A palavra era {}".format(palavra_secreta))
  print("    _______________         ")
  print("   /               \       ")
  print("  /                 \      ")
  print("//                   \/\  ")
  print("\|   XXXX     XXXX   | /   ")
  print(" |   XXXX     XXXX   |/     ")
  print(" |   XXX       XXX   |      ")
  print(" |                   |      ")
  print(" \__      XXX      __/     ")
  print("   |\     XXX     /|       ")
  print("   | |           | |        ")
  print("   | I I I I I I I |        ")
  print("   |  I I I I I I  |        ")
  print("   \_             _/       ")
  print("     \_         _/         ")
  print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def get_palavra_secreta():
  arq = open("words.txt","r")
 
  palavras = []

  for line in arq:
    palavras.append(line.strip())

  arq.close()
  print(palavras)
  return palavras[randrange(0,len(palavras))].lower()

def get_chute():
  return input("Qual a letra: ").strip().lower()

def marca_letra_acertada(chute='',letras_acertadas=[],palavra_secreta=''):
  index = 0
  for letra in palavra_secreta:
    if(chute == letra):
      letras_acertadas[index] = letra
    index+=1

if(__name__ == '__main__'):
  jogar()
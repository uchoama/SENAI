import random
print("Bem vindo ao jogo de adivinhação!")
print("Tente adivinhar o numero que estou pensando entre 1 e 20")
print("Digite 'sair' para encerrar o jogo a qualquer momento.")
numero = random.randint(1,20)
while True:
    palpite= int(input ("Dê seu palpite:"))
    if palpite == numero:
        print ("#$#$ você acertou")
        break
    elif palpite > numero: 
        print("Você chutou alto")
    else:
        print ("você chutou baixo")

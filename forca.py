print("Jogo da Forca")
print("Desenvolvido por: Marcelo Uchoa")
print("Copywrite 2024")
print("Versão Beta")

palavraSecreta = input("Difite a palavra secreta: ")
linha = ""
for i in range(len(palavraSecreta)):
    linha = linha + "__ "

print(linha)

totalErros    = 0
totalAcertos = 0

print("\nPontuação")
print(f" - Toral de Erros : {totalErros}")
print(f"- Total de Acertos: {totalAcertos}")

letra = input("digite uma letra: ")

if letra in palavraSecreta:
    totalAcertos = totalAcertos + 1
    linha = ""
    for i in range(len(palavraSecreta)):
        if letra = palavraSecreta[1]:
print("Hello World")
#idade = int(input("qual é a sua idade? "))
#for contador in range(idade):
#    print(contador)
sair = "S"
while sair !=  "S":
    nome = input("Digite um nome: ")
    if nome == "":
        break
    for letra in nome:
        print(letra)
    print("************")
    sair = input("Sair do programa (S/N)?: ")

    
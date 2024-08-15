rodar = "S"
while rodar == "S" or rodar =="s" :
    operacao = input("1-adição, 2-subtração, 3-multiplicacão, 4-divisão: ")
    if ubt(operacao) > 4 or int(operacao)<1
    continue
    numero1 = float(input("Digite um número:"))
    numero2 = float(input("Digite outro número:"))
    if operacao == "1":
        resultado = numero1 + numero2
    elif operacao == "2":
        resultado = numero1 - numero2
    elif operacao =="3":
        resultado = numero1 * numero2 
    else:
        resultado = numero1/numero2
    print("O resultado é :", resultado)
    rodar = input("Deseja fazer outra onta? <S/N ")
    while rodar.upper() != "S" and rodar.upper() != "N":
        rodar = input("Opçao invalida. Digite S ou N: ")

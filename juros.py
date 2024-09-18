print("Sistema de Calculo de Juros")
print("Desenvolvido por Marcelo Uchoa")
print("Copywrite 2024")
print("Versão 1.0")
print("Digitar valor da conta")

while True:
    valorDaConta = float(input("Valor da conta: R$ "))
    diasDeAtraso = int(input("Quantos dias de atraso: "))
    jurosPorDia = float(input("Juros por dia: % "))

    valorCorrigido = valorDaConta + (valorDaConta * diasDeAtraso * (jurosPorDia/100))

    print(f"O valor corrigido é: R$ {valorCorrigido:.2f}")
    sair = input("Deseja corrigir outro valor? <S/N>")
    if sair.upper() == "N":
        break

print("Agradeço pela visita. Volte sempre. :-)")



aConta + (valorDaconta * diasDeAtraso * (jurosPorDia/100))


    

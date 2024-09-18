def adicao(numA, numB): 
    return numA+numB

def subtracao(numA, NumB):
    return numA- NumB


print("Escolha a opção:")
print("1 - Adição")
print("2 -Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
opcao = input("Digitea opção desejada: ")

if opcao == "1":
    numeroA = float(input("digite o primeiro número: "))
    numeroB = float(input("digite o segundo numero: :)"))
    resultado = numeroA + numeroB
elif opcao == "2":
    numeroA = float(input("digite o primeiro número: "))
    numeroB = float(input("digite o segundo número: "))
    resultado = numeroA - numeroB

    print (f"O resultado é{resultado: .2f}")


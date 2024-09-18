print("Sistema de Conversão do Dólar")
print("Desenvolvido por: Marcelo Uchoa")
print("Copywrite 2024")
print("versão 1.0")

while True: 
    valorEmDolar = float(input("Valor do produto em dólar: US$ "))
    cotacaoDolarHoje = float(input("Digite a cotação do dólar: R$ "))

    valorConvertido = valorEmDolar * cotacaoDolarHoje

    print(f"0 valor convertido de US$ {valorEmDolar} é: R$ {valorConvertido}")
    sair = input("deseja converter outro valor? <S/N> ")
    if sair.upper() == "N":
        Break
print("Agradeço pela visita. Volte sempre. :-)")

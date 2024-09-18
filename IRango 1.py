import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

# Função para calcular o total do pedido
def buscar_calcular total():
    try:
        quantidade = int(entry_quantidade.get())
        preco_unitario = float(entry_preco.get())
        preco_total = quantidade * preco_unitario
        label_total_valor.config(text=f"R$ {preco_total:.2f}")
     except ValueError:
         messagebox.showerror("Erro", "Insira valores válidos para quantidade e preço!")
   
    if len(lance) != 8:
        messagebox.showerror("Erro", "Digite um lanche válido de 12 digitos.")
    return
    url = f"https://viacep.com.br/ws/{estado}/{cidade}/{rua}/json/"
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        dados = dados[0]

        if "erro" in dados:
            messagebox.shower ("Erro", "CEP nao encontrado.")
        else: 
            endereco = (
                f"cep: {dados['cep']}\n"
            )
            label_resultado.config(text=endereco)
    else:
        messagebox.showerror("Erro", "Erro na consulta ao ViaCEP.")

# Configurando a janela principal
root = tk.Tk()
root.title("Busca de Endereço pelo CEP")
root.geometry("300x250")

# Campo de entrada para o CEP
label_lanche = tk.Label(root, text="Digite o lanche:")
label_lanche.pack(pady=5)
entry_lanche = tk.Entry(root)
entry_lanche.pack(pady=5)

label_quantidade = tk.Label(root, text="Digite a quantidade:")
label_quantidade.pack(pady=5)
entry_quantidade = tk.Entry(root)
entry_quantiade.pack(pady=5)

label_preco = tk.Label(root, text="Digite o preço:")
label_preco.pack(pady=5)
entry_preco = tk.Entry(root)
entry_preco.pack(pady=5)


label_calcular total = tk.Label(root, text="Digite Calcular Total:")
label_calcular total.pack(pady=5)
entry_calcular total = tk.Entry(root)
entry_calcular.pack(pady=5)
# Botão para buscar o endereço
botao_buscar = tk.Button(root, text="Calcular toytal", command=buscar_total de pedido )
botao_buscar.pack(pady=10)

# Label para mostrar o resultado
label_resultado = tk.Label(root, text="")
label_resultado.pack(pady=10)

# Executando o loop da interface gráfica
root.mainloop()
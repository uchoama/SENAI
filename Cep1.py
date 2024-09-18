import tkinter as tk
from tkinter import messagebox
import requests 

def buscar_endereco():
    estado = entry_estado.get().strip()
    cidade = entry_cidade.get().strip()
    rua = entry_rua.get().strip()

    if len(estado) != 2:
        messagebox.showerror("Erro", "Digite um CEP válido de 8 digitos.")
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
label_estado = tk.Label(root, text="Digite o Estado:")
label_estado.pack(pady=5)
entry_estado = tk.Entry(root)
entry_estado.pack(pady=5)

label_cidade = tk.Label(root, text="Digite a cidade:")
label_cidade.pack(pady=5)
entry_cidade = tk.Entry(root)
entry_cidade.pack(pady=5)

label_rua = tk.Label(root, text="Digite a rua:")
label_rua.pack(pady=5)
entry_rua = tk.Entry(root)
entry_rua.pack(pady=5)

# Botão para buscar o endereço
botao_buscar = tk.Button(root, text="Buscar Endereço", command=buscar_endereco)
botao_buscar.pack(pady=10)

# Label para mostrar o resultado
label_resultado = tk.Label(root, text="")
label_resultado.pack(pady=10)

# Executando o loop da interface gráfica
root.mainloop()
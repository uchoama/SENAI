import json
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import date

# Arquivo JSON para armazenar os chamados
ARQUIVO_CHAMADOS = 'chamados.json'

# Função para carregar os chamados existentes
def carregar_chamados():
    try:
        with open(ARQUIVO_CHAMADOS, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Função para salvar um novo chamado no arquivo JSON
def salvar_chamados(chamados):
    with open(ARQUIVO_CHAMADOS, 'w') as f:
        json.dump(chamados, f, indent=4)

# Função para gerar o próximo número de chamado
def gerar_numero_chamado():
    chamados = carregar_chamados()
    if chamados:
        ultimo_chamado = chamados[-1]['numero_chamado']
        return ultimo_chamado + 1
    return 1

# Função para salvar o chamado atual
def salvar_chamado():
    nome_cliente = entry_cliente.get()
    tipo_problema = combo_tipo_problema.get()
    descricao = text_descricao.get("1.0", tk.END).strip()
    prioridade = combo_prioridade.get()
    numero_chamado = label_numero_chamado['text']
    data_abertura = label_data_abertura['text']
    
    if not nome_cliente or not tipo_problema or not descricao or not prioridade:
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
        return

def mensagem():
    messagebox.showinfo("Teste",f"{entryNome.get()};\ntel:{entryTelefone.get()}")

janela = tk.Tk()
janela.title("Nome do Cliente")

# **** Cadastro do nome do cliente ****
labelNome = tk.Label(janela,text="Nome do Cliente",font=("Arial", 10), fg="black", bg="yellow")
labelNome.pack(padx=50, pady=5)

entryNome = tk.Entry(janela)
entryNome.pack(padx=50, pady=5)

# ****Cadastro tipo de problema
labelProblema = tk.Label(janela,text="Tipo de Problema")
labelProblema.pack(padx=50, pady=5)

entryProblema = tk.Entry(janela)
entryProblema.pack(padx=60, pady=6)

# **** Descrição do Problema ****
labelDescricao = tk.Label(janela,text="Descrição do Problema")
labelDescricao.pack(padx=60, pady=6)

entryTelefone = tk.Entry(janela)
entryTelefone.pack(padx=60, pady=6)

# **** Cadastro especie do pet ****
labelEmail = tk.Label(janela,text="Prioridade do Problema")
labelEmail.pack(padx=60, pady=6)

# Criando o Combobox
combobox = ttk.Combobox(janela, values=["Baixa", "Média", "Alta"])
combobox.pack(pady=20)

# **** Cadastro data de abertura ****
labelDatadeabertura = tk.Label(janela,text="Data da Abertura")
labelDatadeabertura.pack(padx=60, pady=6)

data_atual = date.today()
Datadeabertura = tk.Label(janela,text=data_atual.strftime("%d/%m/%Y"))
Datadeabertura.pack(padx=60, pady=6)

# **** Número do Chamado ****
labelnumerodochamado = tk.Label(janela,text="Numero do Chamado")
labelnumerodochamado.pack(padx=60, pady=6)

numerodochamado = tk.Label(janela,text=gerar_numero_chamado())
numerodochamado.pack(padx=60, pady=6)

buttonSalvar = tk.Button(janela, text="Salvar",command=mensagem)
buttonSalvar.pack(padx=60, pady=5)

janela.geometry("800x600")

janela.mainloop()
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def mensagem():
    messagebox.showinfo("Teste",f"{entryNome.get()};\ntel:{entryTelefone.get()}")

janela = tk.Tk()
janela.title("Nome do Tutor")

# **** Cadastro do nome do cliente ****
labelNome = tk.Label(janela,text="Nomen do Tutor",font=("Arial", 10), fg="black", bg="yellow")
labelNome.pack(padx=50, pady=5)

entryNome = tk.Entry(janela)
entryNome.pack(padx=50, pady=5)

# ****Cadastro do telefone do
labelTelefone = tk.Label(janela,text="Nome do Pet")
labelTelefone.pack(padx=50, pady=5)

entryTelefone = tk.Entry(janela)
entryTelefone.pack(padx=60, pady=6)

# **** Cadastro do e-mail do cliente ****
labelEmail = tk.Label(janela,text="Data do Nascimento do pet")
labelEmail.pack(padx=60, pady=6)

entryTelefone = tk.Entry(janela)
entryTelefone.pack(padx=60, pady=6)

# **** Cadastro especie do pet ****
labelEmail = tk.Label(janela,text="Especie do pet")
labelEmail.pack(padx=60, pady=6)

# Criando o Combobox
combobox = ttk.Combobox(janela, values=["Cachorro", "Gato", "Rato", "Vaca", "Cavalo"])
combobox.pack(pady=20)




# **** Cadastro raça do pet ****
labelEmail = tk.Label(janela,text="Raça")
labelEmail.pack(padx=60, pady=6)

entryEmail = tk.Entry(janela, text="Salvar")
entryEmail.pack(padx=60, pady=6)

buttonSalvar = tk.Button(janela, text="Salvar",command=mensagem)
buttonSalvar.pack(padx=60, pady=5)

janela.geometry("400x300")

janela.mainloop()
import tkinter as tk
from tkinter import messagebox
import string
import secrets

def gerar_senha():
    tamanho_str = entry_tamanho.get()

    # Verifica se o tamanho é um número
    if not tamanho_str.isdigit():
        messagebox.showerror("Erro", "Digite um tamanho válido (número).")
        return
    
    tamanho = int(tamanho_str)

    # Constrói o alfabeto baseado nas escolhas do usuário
    alfabeto = ""
    if var_minusculas.get():
        alfabeto += string.ascii_lowercase
    if var_maiusculas.get():
        alfabeto += string.ascii_uppercase
    if var_numeros.get():
        alfabeto += string.digits
    if var_simbolos.get():
        alfabeto += string.punctuation

    # Verifica se pelo menos uma opção foi escolhida
    if not alfabeto:
        messagebox.showerror("Erro", "Selecione pelo menos um tipo de caractere.")
        return

    # Gera a senha
    senha = ''.join(secrets.choice(alfabeto) for _ in range(tamanho))
    entry_resultado.config(state="normal")
    entry_resultado.delete(0, tk.END)
    entry_resultado.insert(0, senha)
    entry_resultado.config(state="readonly")

def copiar_para_area_de_transferencia():
    senha = entry_resultado.get()
    if not senha:
        messagebox.showwarning("Aviso", "Nenhuma senha para copiar.")
        return
    janela.clipboard_clear()
    janela.clipboard_append(senha)
    messagebox.showinfo("Copiado", "Senha copiada para a área de transferência!")

# ---------- JANELA PRINCIPAL ----------
janela = tk.Tk()
janela.title("Gerador de Senhas")
janela.geometry("380x360")
janela.resizable(False, False)

# ---------- CHECKBOXES ----------
tk.Label(janela, text="Selecione os tipos de caracteres:", font=("Arial", 11, "bold")).pack(pady=5)

var_minusculas = tk.BooleanVar(value=True)
var_maiusculas = tk.BooleanVar(value=True)
var_numeros = tk.BooleanVar(value=True)
var_simbolos = tk.BooleanVar(value=False)

tk.Checkbutton(janela, text="Letras minúsculas (a-z)", variable=var_minusculas).pack(anchor="w", padx=20)
tk.Checkbutton(janela, text="Letras maiúsculas (A-Z)", variable=var_maiusculas).pack(anchor="w", padx=20)
tk.Checkbutton(janela, text="Números (0-9)", variable=var_numeros).pack(anchor="w", padx=20)
tk.Checkbutton(janela, text="Símbolos (!@#$% etc)", variable=var_simbolos).pack(anchor="w", padx=20)

# ---------- TAMANHO ----------
frame_tamanho = tk.Frame(janela)
frame_tamanho.pack(pady=15)

tk.Label(frame_tamanho, text="Tamanho da senha:").pack(side="left", padx=5)
entry_tamanho = tk.Entry(frame_tamanho, width=5)
entry_tamanho.pack(side="left")
entry_tamanho.insert(0, "12")  # valor padrão

# ---------- BOTÃO GERAR ----------
btn_gerar = tk.Button(janela, text="Gerar Senha", command=gerar_senha, width=20, bg="#4CAF50", fg="white")
btn_gerar.pack(pady=10)

# ---------- RESULTADO ----------
tk.Label(janela, text="Senha gerada:", font=("Arial", 11, "bold")).pack()
entry_resultado = tk.Entry(janela, width=35, font=("Arial", 12), state="readonly")
entry_resultado.pack(pady=5)

# ---------- BOTÃO COPIAR ----------
btn_copiar = tk.Button(janela, text="Copiar", command=copiar_para_area_de_transferencia, width=15)
btn_copiar.pack(pady=5)

# ---------- LOOP ----------
janela.mainloop()

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

caminho_arquivo = filedialog.askopenfilename(title="Escolha um arquivo .docx")
print("Arquivo selecionado:", caminho_arquivo)

if caminho_arquivo.endswith(".docx"):
    print("Arquivo válido")
else:
    ("Por favor, selecione um arquivo válido(.docx)")
    
caminho_salvar = filedialog.asksaveasfilename(
    defaultextension=".pdf",
    filetypes=[("PDF files", "*.pdf")],
    title="Salvar como..."
)

print("Salvar em: ", caminho_salvar)

print(f"Convertendo '{caminho_arquivo}' em PDF...")
print(f"PDF será salvo em: {caminho_salvar}")
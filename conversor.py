import tkinter as tk
from tkinter import filedialog
from tqdm import tqdm
import time
from docx2pdf import convert
import os

root = tk.Tk()
root.withdraw()

arquivos = filedialog.askopenfilenames(filetypes=[("Documentos Word", "*.docx")])
pasta_destino = filedialog.askdirectory(title="Selecione a pasta para salvar os PDFs")

print("Arquivos selecionados:", arquivos)
print("*** Salvar em: ", pasta_destino + " ***")
print(f"Convertendo '{len(arquivos)}' arquivos em PDF...")

for arquivo in tqdm(arquivos):
    if arquivo.endswith(".docx"):
        nome_arquivo = os.path.basename(arquivo)
        nome_pdf = os.path.splitext(nome_arquivo)[0] + ".pdf"
        caminho_pdf = os.path.join(pasta_destino, nome_pdf)
        convert(arquivo, caminho_pdf)
    else:
        print(f"Arquivo inválido: {arquivo}")

print(f"*** PDF será salvo em: {pasta_destino} ***")

root.destroy()
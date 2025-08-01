import tkinter as tk
from tkinter import filedialog
from tqdm import tqdm
import time
from docx2pdf import convert
import os
from colorama import init, Fore, Style
init(autoreset=True)

root = tk.Tk()
root.withdraw()

arquivos = filedialog.askopenfilenames(filetypes=[("Documentos Word", "*.docx")])

pasta_destino = filedialog.askdirectory(title="Selecione a pasta para salvar os PDFs")


print("\n" + Fore.BLUE + Style.BRIGHT + "=" * 50)
print("CONVERSOR DE ARQUIVOS WORD PARA PDF".center(50))
print("=" * 50 + Style.RESET_ALL)


print(Fore.CYAN + "\n📄 Arquivos selecionados:")
for arq in arquivos:
    print(Fore.WHITE + f"  → {os.path.basename(arq)}")

print(Fore.CYAN + f"\n📁 Pasta destino: {pasta_destino}\n")

print(Fore.MAGENTA + "🚀 Iniciando conversão...\n" + Style.RESET_ALL)

for arquivo in tqdm(arquivos, desc=Fore.YELLOW + "Progresso" + Style.RESET_ALL, ncols=60):
    if arquivo.endswith(".docx"):
        nome_arquivo = os.path.basename(arquivo)
        nome_pdf = os.path.splitext(nome_arquivo)[0] + ".pdf"
        caminho_pdf = os.path.join(pasta_destino, nome_pdf)
        convert(arquivo, caminho_pdf)
        print(Fore.GREEN + f"✔ {nome_arquivo} convertido com sucesso.")
    else:
        print(Fore.RED + f"✖ Arquivo inválido: {arquivo}")


print("\n" + Fore.BLUE + Style.BRIGHT + "=" * 50)
print(Fore.GREEN + "Conversão finalizada!".center(50))
print(Fore.GREEN + f"PDFs salvos em: {pasta_destino}".center(50))
print("=" * 50 + Style.RESET_ALL)

root.destroy()

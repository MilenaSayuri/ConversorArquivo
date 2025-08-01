📝 Conversor de Word para PDF (.docx → .pdf)
Este é um projeto simples em Python que permite ao usuário converter arquivos .docx para PDF de forma prática, com uma interface gráfica básica para seleção de arquivos e pasta de destino. O terminal ainda oferece feedback visual com barra de progresso e cores para melhorar a experiência durante o uso.

✅ Funcionalidades
Seleciona múltiplos arquivos .docx com janela de arquivos.
Permite escolher a pasta de destino para os PDFs.
Converte automaticamente todos os arquivos para PDF usando a biblioteca docx2pdf.
Mostra o progresso da conversão com barra personalizada (tqdm).
Exibe mensagens coloridas no terminal para facilitar a leitura (colorama).
Exibe o nome de cada arquivo sendo convertido.
Mensagem de conclusão clara e organizada.

📦 Tecnologias e bibliotecas utilizadas
tkinter – para janelas de seleção de arquivos/pasta.
filedialog – para interação gráfica com o sistema de arquivos.
tqdm – barra de progresso amigável no terminal.
colorama – mensagens coloridas no terminal.
docx2pdf – conversão de .docx para .pdf.
os – manipulação de caminhos de arquivos e diretórios.

▶ Como usar
1. Clone este repositório ou copie o código.

2. Instale as dependências:
pip install docx2pdf tqdm colorama

3. Execute o script Python:
python conversor.py

5. Escolha os arquivos .docx que deseja converter.
6. Escolha a pasta onde deseja salvar os PDFs.
7. Acompanhe o progresso no terminal até a conversão estar concluída.

import os  # Importa o módulo para manipulação de arquivos e diretórios
from tkinter.filedialog import askdirectory  # Importa função para abrir uma janela de seleção de pasta

# Abre uma janela para o usuário selecionar uma pasta e armazena o caminho na variável 'caminho'
caminho = askdirectory(title="Selecione uma pasta")

# Lista todos os arquivos e pastas dentro do diretório selecionado
lista_arquivos = os.listdir(caminho)

# Dicionário que associa tipos de arquivos (categorias) às suas extensões
locais = {
    "imagens": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],  # Extensões de imagens
    "documentos": [".docx", ".txt", ".pptx"],  # Extensões de documentos
    "planilhas": [".xlsx", ".xls", ".csv"],  # Extensões de planilhas
    "videos": [".mp4", ".mkv", ".mov", ".avi"],  # Extensões de vídeos
    "audios": [".mp3", ".wav", ".aac", ".flac"],  # Extensões de áudios
    "pdfs": [".pdf"]  # Extensão de arquivos PDF
}

# Percorre cada arquivo na lista de arquivos do diretório
for arquivo in lista_arquivos:
    # Separa o nome do arquivo e sua extensão
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    
    # Verifica em qual categoria o arquivo se encaixa, com base na extensão
    for pasta in locais:
        if extensao in locais[pasta]:  # Se a extensão do arquivo está na lista de uma categoria
            # Verifica se a pasta correspondente à categoria já existe; se não, cria a pasta
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            
            # Move o arquivo para a pasta correspondente
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")
            break  # Sai do loop assim que o arquivo é movido

# Exibe uma mensagem indicando que a organização foi concluída
print("Arquivos organizados com sucesso!")
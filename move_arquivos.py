import os
import shutil

# Diretório onde estão os arquivos
diretorio_origem = 'C:/Users/ederson.domiciano/Downloads/'

# Pasta para os arquivos .xlsx, .csv e .xls
pasta_excel = 'C:/Users/ederson.domiciano/Downloads/EXCEL'

# Pasta para os arquivos .pdf
pasta_pdf = 'C:/Users/ederson.domiciano/Downloads/PDF'

# Pasta para os arquivos .png .jpeg .jpg .gif
pasta_img = 'C:/Users/ederson.domiciano/Downloads/IMG'

# Pasta para os arquivos .mp4
pasta_video = 'C:/Users/ederson.domiciano/Downloads/VIDEO'

# Pasta para os arquivos .exe .msi
pasta_programas = 'C:/Users/ederson.domiciano/Downloads/PROGRAMAS'

# Pasta para os arquivos .zip .rar .7zip
pasta_compactados = 'C:/Users/ederson.domiciano/Downloads/ZIP'

# Garante que as pastas de destino existam
os.makedirs(pasta_excel, exist_ok=True)
os.makedirs(pasta_pdf, exist_ok=True)
os.makedirs(pasta_img, exist_ok=True)
os.makedirs(pasta_video, exist_ok=True)
os.makedirs(pasta_programas, exist_ok=True)
os.makedirs(pasta_compactados, exist_ok=True)


# Loop pelos arquivos no diretório de origem
for arquivo in os.listdir(diretorio_origem):
    caminho_arquivo = os.path.join(diretorio_origem, arquivo)

    if arquivo.endswith(('.xlsx', '.csv', '.xls')):
        # Move arquivos .xlsx, .csv e .xls para a pasta EXCEL
        shutil.move(caminho_arquivo, os.path.join(pasta_excel, arquivo))
    elif arquivo.endswith('.pdf'):
        # Move arquivos .pdf para a pasta PDF
        shutil.move(caminho_arquivo, os.path.join(pasta_pdf, arquivo))
    elif arquivo.endswith(('.png', '.gif', '.jpg', '.jpeg')):
        # Move arquivos .pdf para a pasta PDF
        shutil.move(caminho_arquivo, os.path.join(pasta_img, arquivo))
    elif arquivo.endswith('.mp4'):
        # Move arquivos .pdf para a pasta VIDEO
        shutil.move(caminho_arquivo, os.path.join(pasta_video, arquivo))
    elif arquivo.endswith(('.exe', '.msi')):
        # Move arquivos .pdf para a pasta VIDEO
        shutil.move(caminho_arquivo, os.path.join(pasta_programas, arquivo))
    elif arquivo.endswith(('.zip', '.rar', '.zip')):
        # Move arquivos .pdf para a pasta VIDEO
        shutil.move(caminho_arquivo, os.path.join(pasta_compactados, arquivo))


import os
import cv2

# Variável path para a pasta Images
path = 'Images/'

# Lista para armazenar os nomes dos arquivos de imagem
Images = []

# Verificar cada arquivo da pasta
for file in os.listdir(path):
    # Separar o nome e a extensão do arquivo
    file_name, file_extension = os.path.splitext(file)
    
    # Verificar se a extensão do arquivo corresponde à extensão da imagem
    if file_extension == '.jpg' or file_extension == '.png':
        # Concatenar o caminho, nome do arquivo e extensão
        file_name = path + file_name + file_extension
        
        # Adicionar o arquivo à lista
        Images.append(file_name)

# Obter a contagem de imagens
count = len(Images)

# Ler a primeira imagem da lista
frame = cv2.imread(Images[0])

# Capturar a largura, altura e canais
height, width, channels = frame.shape

# Variável de tupla para armazenar as dimensões
size = (width, height)

# Criar um VideoWriter para escrever o vídeo
out = cv2.VideoWriter('Project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

# Adicionar as imagens ao VideoWriter
for i in range(0, count-1):
    # Ler a próxima imagem
    next_frame = cv2.imread(Images[i+1])
    
    # Adicionar a imagem ao vídeo
    out.write(next_frame)

# Imprimir mensagem de conclusão
print("Concluído")

# Fechar o VideoWriter
out.release()
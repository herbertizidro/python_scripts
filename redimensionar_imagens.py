import os
import glob
from PIL import Image

#redimensiona todas as imagens .png e .jpg de uma pasta 

larg_desejada = 960
for arq in os.listdir("./"):
    if arq in glob.glob("*.png") or arq in glob.glob("*.jpg"):
        img = Image.open(arq)     
        larg_percentual = float(larg_desejada) / float(img.size[1]) #altura da imagem    
        alt_desejada = int((img.size[1] * larg_percentual))        
        img = img.resize((larg_desejada, alt_desejada), Image.ANTIALIAS) #redimensiona
        print(str(img.size[0]) + "x" + str(img.size[1])) #altura x largura atuais
        img.save(arq)

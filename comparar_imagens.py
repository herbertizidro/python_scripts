import os
import cv2


def all_imgs(*dirs):
    aux = []
    for d in list(dirs):
        d = os.path.expanduser("~") + "\\" + d
        for caminho, pasta, arquivo in os.walk(d):
            for a in os.listdir(caminho):
                if a[-3::] == "jpg" or a[-3::] == "png":
                    aux.append(caminho + "\\" + a)
    return aux
                

def compare_imgs(path, dirs):
    if path in dirs:
        dirs.remove(path)
    img_orig = cv2.imread(path)
    for img in dirs:
        img_copia = cv2.imread(img)
        if img_orig.shape == img_copia.shape:
            diferenca = cv2.subtract(img_orig, img_copia)
            b, g, r = cv2.split(diferenca)
            if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
                print("\n >> Imagem em " + img + " corresponde!")

dirs = all_imgs("Documents", "Pictures") #quantos diretórios quiser
compare_imgs(<CAMINHO_DA_IMAGEM_ORIGINAL>, dirs)


#esse script procura imagens que sejam cópias de uma imagem "original" nos diretórios definidos
#imagens avulsas e dentro de pastas, todas são verificadas

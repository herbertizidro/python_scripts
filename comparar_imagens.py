import os
import cv2


def all_imgs(*dirs):
    aux = []
    for dir in list(dirs):
        dir = os.path.expanduser("~") + "\\" + dir
        for caminho, pasta, arquivo in os.walk(dir):
            print(' [+] verificando pasta "' + pasta '" de ' + dir + '\n')
            for img in os.listdir(caminho):
                if img[-3::] == "jpg" or img[-3::] == "png":
                    aux.append(caminho + "\\" + img)
    return aux
                

def compare_imgs(path, dirs):
    if path in dirs: #remove o caminho da imagem original
        dirs.remove(path)
    img_orig = cv2.imread(path)
    for img in dirs:
        img_copia = cv2.imread(img)
        if img_orig.shape == img_copia.shape:
            diferenca = cv2.subtract(img_orig, img_copia)
            b, g, r = cv2.split(diferenca)
            if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
                print("\n [!] Imagem em " + img + " corresponde!")

dirs = all_imgs("Documents", "Pictures") #quantos diretórios quiser
compare_imgs(<CAMINHO_DA_IMAGEM_ORIGINAL>, dirs)


#esse script procura imagens que sejam cópias de uma imagem "original" nos diretórios definidos
#imagens avulsas e dentro de pastas, todas são verificadas

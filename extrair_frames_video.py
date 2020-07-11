import os
import cv2
import numpy as np


#coleta frames de um vídeo .mp4

if __name__ == "__main__":
    video = "andy.mp4"
    diretorio = "./Andy"
    cap = cv2.VideoCapture(video)
    cont_frames = 0
    total_amostras = 50
    
    try:
        os.mkdir(diretorio)
    except OSError:
        local = os.listdir(diretorio)
        local_arquivos = []
        for arq in local:
            if arq[-3::] == "png":
                local_arquivos.append(arq)
        total_amostras += len(local_arquivos)
        cont_frames += len(local_arquivos)
        
    while cont_frames < total_amostras:
        ret, img = cap.read()
        if ret == False:
            cap.release()
        else:
            img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(diretorio + "\\" + str(cont_frames)+ ".png", img_cinza)
            cont_frames += 1
    cap.release()
    print(" [*] Concluído!")

import os
import cv2
import numpy as np

#use um vídeo que mostre somente a pessoa que você deseja extrair o rosto
#amostras de diferentes vídeos podem ser salvas na mesma pasta
#o nome das novas amostras seguem a ordem crescente das amostras já salvas


if __name__ == "__main__":
    video = "andy.mp4"
    diretorio = "./Andy"
    frontal_face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
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
            faces = frontal_face_cascade.detectMultiScale(img_cinza, 1.3, 5)
            if len(faces) == 0:
                continue
            for (x, y, w, h) in faces:
                coord_face = img_cinza[y:y+h, x:x+w] #ou coord_face = img[y:y+h, x:x+w]
                larg, alt = coord_face.shape

            if(larg * alt <= 20 * 20): #imagens muito pequenas são desconsideradas
                continue
            recortar_face = cv2.resize(coord_face, (255, 255))
            cv2.imwrite(diretorio + "\\" + str(cont_frames)+ ".png", coord_face)
            cont_frames += 1
    cap.release()
    print(" [*] Concluído!")

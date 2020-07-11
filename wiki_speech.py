import pyttsx3
import requests
from bs4 import BeautifulSoup
import speech_recognition as sr


def falar(texto):
    speak = pyttsx3.init('sapi5') 
    speak.say(texto)
    speak.runAndWait()


def busca_wiki(termo):
    requisicao = requests.get("https://pt.wikipedia.org/wiki/" + termo)
    soup = BeautifulSoup(requisicao.text, "html.parser")
    texto = []
    for s in soup.find_all("p"):
        texto.append(s.text)
    n_encontrado = "A Wikipédia não possui um artigo com este nome exato."
    if n_encontrado in texto[0]:
        falar(n_encontrado)      
    else:
        falar(texto[0])


while True:
    rec = sr.Recognizer()
    with sr.Microphone() as mic:
        frase = rec.listen(mic)
        busca_wiki(rec.recognize_google(frase, language = "pt-br"))
        

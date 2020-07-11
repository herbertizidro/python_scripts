import PyPDF2
from googletrans import Translator


def extrairTextoPDF(arq, traducao = False):
    pdf = open(arq, "rb")
    leitor = PyPDF2.PdfFileReader(pdf)
    texto_extraido = ""
    for i in range(leitor.numPages): #numPages = total de páginas
	 pagina = leitor.getPage(i) #getPage(i) = página 0
	 texto_extraido += pagina.extractText()
         pdf.close()
    if traducao:
        tradutor = Translator()
        detectar_idioma = tradutor.detect(texto_extraido)
        if "Detected" in str(detectar_idioma):
            traducao = tradutor.translate(texto_extraido, src = detectar_idioma.lang, dest = "pt")
            return traducao.text
    else:
        return texto_extraido

if __name__ == "__main__":
    pdf = extrairTextoPDF(<pdf>) #extrairTextoPDF(<pdf>, True) -> para extrair e traduzir
    print(pdf)

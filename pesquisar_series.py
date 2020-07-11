import requests
from bs4 import BeautifulSoup


def verificarTemporadas(serie):
    
    serie = serie.lower().replace(" ","-")
    
    url1 = requests.get("https://tuaserie.com/serie/assistir-serie-" + serie + ".html")
    url2 = requests.get("https://tuaserie.com/serie/assistir-" + serie + ".html")
    url3 = requests.get("https://tuaserie.com/serie/" + serie + ".html")
    
    resultado = [url1, url2, url3]
    aux = 0
    while aux < len(resultado):
        bs = BeautifulSoup(resultado[aux].text, "html.parser")
        h2 = [titulo for titulo in bs.find_all("h2")]
        if h2[0].text == "Error 404: Página não existe":
            aux += 1
        else:
            for i in range(0, len(h2)):
                print(h2[i].text)
            print()
            break


lista_series = ["the witcher",
                "the office",
                "good girls",
                "stranger things",
                "brooklyn nine nine",
                "la casa de papel"]
for serie in lista_series:
    print(serie.upper())
    verificarTemporadas(serie)


#pesquisa séries no site tuaserie.com
#informa as temporadas que o site exibe para cada série da lista

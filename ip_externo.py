import requests
import clipboard
from bs4 import BeautifulSoup

url = "https://www.meuip.com.br"
requisicao = requests.get(url)
soup = BeautifulSoup(requisicao.text, "html.parser")
ip_externo = soup.text[1454:]
clipboard.copy(ip_externo) #ip na área de transferência



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
# Configura o web
service = Service(ChromeDriverManager().install())
# Abre o Chrome e acessa a página
driver = webdriver.Chrome(service=service)
#ir para o site do ibge
driver.get("https://www.ibge.gov.br")
#seguindo pra barra de busca
#barra_de_busca = driver.find_element(By.ID, "mod-search-searchword")
#barra_de_busca = driver.find_element(By.NAME, "searchword")
#sleep(10)

# Insere o dado da pesquisa
#barra_de_busca.send_keys("Juiz de Fora")

#data_noticia = driver.find_element(By.CLASS_NAME,"home-noticia-data")

#data_noticia.text


#data_noticia = driver.find_elements(By.CLASS_NAME,'home-noticia-data')
#data_noticia

#for data_noticia in data_noticia:
# print(data_noticia.text)

tags = driver.find_elements(By.TAG_NAME,"a")

for tag in tags:
  print(tag.get_attribute("href"))
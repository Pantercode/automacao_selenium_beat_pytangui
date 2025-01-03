from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# Configura o web
service = Service(ChromeDriverManager().install())
# Abre o Chrome e acessa a página
driver = webdriver.Chrome(service=service)

driver.get("https://www.globo.com")

noticia = driver.find_elements(By.XPATH, '//*[@id="destaque"]/div/div/div[1]/div/div/a/h2')

print(noticia.text)

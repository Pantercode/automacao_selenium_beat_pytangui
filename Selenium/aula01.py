from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
# Configura o web
service = Service(ChromeDriverManager().install())

# Abre o Chrome e acessa a página
driver = webdriver.Chrome(service=service)
# Abre o Chrome na pagina da documentacao
driver.get('https://www.selenium.dev/documentation/')
# seleciona a caixa de texto
text_box = driver.find_element(by=By.NAME,value='my-text')
# Escreve dentro do box selenium
text_box.send_keys('Selenium')
submit_button = driver.find_element(by=By.CSS_SELECTOR,value='button')
submit_button.click()
sleep(30)
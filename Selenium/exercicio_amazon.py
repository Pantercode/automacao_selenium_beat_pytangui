from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
# Configura o web
service = Service(ChromeDriverManager().install())
# Abre o Chrome e acessa a página
driver = webdriver.Chrome(service=service)

driver.get("https://www.amazon.com.br")

clicar_no_botão = driver.find_element(By.CLASS_NAME, 'hm-icon-label')

clicar_no_botão.click()
sleep(5)
produtos_em_alta = driver.find_element(By.CLASS_NAME,'hmenu-item')
sleep(5)
produtos_em_alta.click()

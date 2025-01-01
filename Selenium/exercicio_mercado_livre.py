from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from time import sleep

# Configura o WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Acessa a página
driver.get('https://www.mercadolivre.com.br/ofertas#nav-header')

# Aguarda carregar os itens do carrossel
wait = WebDriverWait(driver, 10)

# Inicializa a lista para salvar os dados
ofertas = []

# Loop pelos itens do carrossel
filtros = driver.find_elements(By.CLASS_NAME, 'carousel__item')

for p in range(len(filtros)):
    filtros = driver.find_elements(By.CLASS_NAME, 'carousel__item')  # Recarrega os filtros
    filtro = filtros[p]
    
    # Verifica se o filtro está visível e clica
    if not filtro.is_displayed():
        proximo_filtro = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'andes-carousel-snapped__control--next'))
        )
        proximo_filtro.click()
        sleep(2)  # Dá tempo para os elementos carregarem
        filtros = driver.find_elements(By.CLASS_NAME, 'carousel__item')  # Atualiza os filtros
        filtro = filtros[p]

    filtro.click()
    sleep(3)  # Espera o carregamento dos resultados

    # Obtém as promoções
    promocoes = driver.find_elements(By.CLASS_NAME, 'poly-card__content')
    for promocao in promocoes:
        descricao = promocao.find_element(By.CLASS_NAME, 'promotion-item__description').text
        desconto = promocao.find_element(By.CLASS_NAME, 'andes-money-amount__discount').text
        ofertas.append({"Descrição": descricao, "Desconto": desconto})

# Salva os dados em um DataFrame
df_ofertas = pd.DataFrame(ofertas)
print(df_ofertas)

# Fecha o navegador
driver.quit()





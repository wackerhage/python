from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import json

driver = webdriver.Chrome()

driver.get("https://www.magazineluiza.com.br/console-nintendo-switch-oled-64gb-branco-com-joy-con-standard-hbgskaaa1/p/ab83e1cghh/ga/otga/")

try:
    title = driver.find_element(By.XPATH, '//h1[@data-testid="heading-product-title"]').text

    price_extract1 = driver.find_element(By.XPATH, '//p[@data-testid="installment"]').text
    price_extract2 = driver.find_element(By.XPATH, '//p[@data-testid="price-value"]').text
    price = f"{price_extract1} + {price_extract2} no pix."

    # Neste trecho utilizei o json para capturar as informacoes do script do magazine luiza que
    # contem informacoes sobre o estoque do produto:

    script = driver.find_element(By.XPATH, '//script[@type="application/ld+json" and @data-testid="jsonld-script"]')
    json_content = script.get_attribute('innerHTML')

    data = json.loads(json_content)

    availability = data["offers"]["availability"]

    # O magazineluiza faz uso de um script https://schema.org/InStock
    # Verifiquei que a variavel ItemAvailability ligada ao HTML do produto esta indicando InStock.
    # O mesmo poderia ter sido associado a SoldOut, caso nao houvesse estoque.
    # Entao utilizei a variavel availability para capturar este trecho, e se achar "InStock", entao ha estoque:

    if "InStock" in availability:
        stock_availability = "Disponibilidade: Em estoque."

finally:
    driver.quit()

dados = {
    "Título do produto": title,
    "Preco": 2033.15,
    "Disponibilidade": stock_availability,
}

with open("produto.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=3)
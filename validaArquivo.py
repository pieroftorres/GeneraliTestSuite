from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
import time

nome_arquivo = "DAYCOVAL_005465_22012024.txt"


with open(nome_arquivo, 'r') as arquivo:
    linhas = arquivo.readlines()


    chrome_options = Options()
    chrome_options.add_argument("user-data-dir=C:/Users/piero/AppData/Local/Google/Chrome/User Data")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(7)

    urlTia = driver.get('http://172.30.88.12:7202/tiaweb/faces/Login')


    usuarioTIA = driver.find_element(By.ID, value="r1:0:pt:s1:username::content")
    senhaTIA = driver.find_element(By.ID, value="r1:0:pt:s1:password::content")
    iniciarSessao = driver.find_element(By.XPATH, value='//span[contains(text(), "Iniciar Sessão")]')

    usuarioTIA.send_keys("PFAGUT")
    senhaTIA.send_keys("LOSA")
    iniciarSessao.click()

    
    # Processar linhas intermediárias
    for linha in linhas:
        if linha.startswith('1'):
            certificado = linha[41:59]
            print(f"Procurando {certificado}...")

            pesquisaRapida = driver.find_element(By.ID, value="pt:sf_t:searchTB:pt_it1::content")

            pesquisaRapida.clear()
            pesquisaRapida.send_keys(certificado)            

            sugestao = driver.find_element(By.XPATH, value="//li[contains(text(), 'Daycoval Prestamista')]")
            sugestao.click()
            pesquisaRapida.send_keys(Keys.ENTER)

            time.sleep(5)
            abaInformacoes = driver.find_element(By.XPATH, value="//label[contains(text(), 'Certificado do Parceiro')]/../../..//input")
            assert abaInformacoes.get_attribute('value') == certificado

            #fecharSeparador = driver.find_element(By.XPATH, value="//div[contains(@id, 'pt:sf_t:dynTabsPane:1:tabIndex::_afrEps')]/following-sibling::div/a")
        else:
            continue
    encerrarSessao = driver.quit()

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def despeja_json():
    import json
    from pathlib import Path
    lista_extrato = extrato.split('\n')
    print(lista_extrato)
    extrato_json = json.dumps(lista_extrato)
    Path('extrato-bpi.json').write_text(extrato_json)


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-PT', '--window-size=800,600', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,
        'excludeSwitches': ['enable-logging'],

    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    return driver


extrato = ''
flag = False

# Tela inicial
print('Buscador de Extrato e Manipulador de Dados')
entra = input('Deseja abrir navegador e buscar extrato? S/N: ')
entra = entra.upper()
if entra == "S":
    flag = True

if flag == True:

    # define o navegador padrão e abre o url
    navega = iniciar_driver()
    navega = webdriver.Chrome()
    navega.get("https://www.bpinet.pt/BPINET/Login.aspx#")

    time.sleep(2)
    navega.find_element(
        By.XPATH, '//*[@id="LT_BPINet_wtLT_Layout_Login_block_wtInputsLogin_CW_BPINet_Autenticacao_wt49_block_wtUserId"]').send_keys('855640021')
    navega.find_element(
        By.XPATH, '//*[@id="LT_BPINet_wtLT_Layout_Login_block_wtInputsLogin_CW_BPINet_Autenticacao_wt49_block_wtPassword"]').send_keys('08017')
    navega.find_element(
        By.XPATH, '//*[@id="LT_BPINet_wtLT_Layout_Login_block_wtInputsLogin_CW_BPINet_Autenticacao_wt49_block_wtBtnEntrar"]').click()
    time.sleep(2)
    # Clica Menu Vertical Consulta
    navega.find_element(
        By.XPATH, '//*[@id="LT_BPINet_wt10_block_wtMenu_CW_BPINet_Gerais_wt31_block_wtMnuPrincipal_ctl02_LT_BPI_Patterns_wt4_block_wtMenuItem_wt7_wt9"]').click()
    time.sleep(2)

    # Pega Texto do elemento extrato
    extrato = navega.find_element(
        By.XPATH, '//*[@id="LT_BPINet_wt38_block_wtMainContent_CW_Contas_wt12_block_wtListaMovimentos"]/tbody').text

    # Chama função para gravar extrato em formato json
    despeja_json()

    # Fecha navegador
    navega.quit()

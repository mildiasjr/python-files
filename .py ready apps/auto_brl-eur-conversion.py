
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

btcbrl = 0

# define o navegador padrão e abre o url
navega = webdriver.Chrome()
navega.get("http://br.advfn.com")

time.sleep(1)
## Clica no botao de aceita cookies do site
navega.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()

# Entra no Monitor
time.sleep(1)
btcbrl = navega.find_element(By.XPATH, '//*[@id="stocks-menu"]/ul/li[2]/span').click()

# Entra com os dados de login e avança
time.sleep(3)
navega.find_element(By.XPATH, '//*[@id="login_username"]').send_keys("mildiasjr")
time.sleep(1)
navega.find_element(By.XPATH, '//*[@id="login_password"]').send_keys("010875")
navega.find_element(By.XPATH, '//*[@id="login_submit"]').click()
time.sleep(1)

# Busca dados na tabela do Monitor
### Busca dados de BTCBRL
dados = {'BTCBRL':'','BTCUSD':'','BTCEUR':'','EURBRL':'','USDBRL':''}

dados['BTCBRL'] = navega.find_element(By.XPATH, '//*[@id="monitorApp_monGrid_grid_table"]/tbody/tr[21]/td[6]').text
dados['BTCEUR'] = navega.find_element(By.XPATH, '//*[@id="monitorApp_monGrid_grid_table"]/tbody/tr[22]/td[6]').text
dados['BTCUSD'] = navega.find_element(By.XPATH, '//*[@id="monitorApp_monGrid_grid_table"]/tbody/tr[23]/td[6]').text
dados['EURBRL'] = navega.find_element(By.XPATH, '//*[@id="monitorApp_monGrid_grid_table"]/tbody/tr[26]/td[6]').text
dados['USDBRL'] = navega.find_element(By.XPATH, '//*[@id="monitorApp_monGrid_grid_table"]/tbody/tr[28]/td[6]').text
navega.close()

for chave, valor in zip(dados.keys(), dados.values()):
    conteudo = dados[chave]
    conteudo = conteudo.replace('.','')
    conteudo = conteudo.replace(',','.')
    dados[chave] = float(conteudo)
    print(f'{chave}:{valor}')

ratiobe = dados['BTCBRL'] / dados['BTCEUR']
ratiobu = dados['BTCBRL'] / dados['BTCUSD'] 
print(f"Ratio BTCBRL e BTCEUR: {ratiobe}")
print(f"Ratio BTCBRL e BTCUSD: {ratiobu}")
if ratiobe <= dados['EURBRL']:
    print('Favorável para conversão BRL>EUR através do BTC')
else:
    print('Desfavorável para conversão BRL>EUR através do BTC')


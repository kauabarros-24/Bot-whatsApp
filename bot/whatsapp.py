
from selenium import webdrive
import time
from webdriver_manager.chrome import ChromeDriverManager

#NAVEGAR ATÉ O ZAP
driver = webdriver.Chrome(ChromeDriverManager.install())
driver.get('https://web.whatsapp.com/')
time.sleep(30)
#Definiar a mensagem a ser enviada:
contatos = ['Teste bot', 'Pai']
#Bibliotecas
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
#Ir para o zap
driver = webdriver.Chrome(ChromeDriverManager.install())
driver.get('https://web.whatsapp.com/')
time.sleep(30)
#Buscar contatos
contatos = ['Teste bot', 'Pai']
#Enviar mensagensd
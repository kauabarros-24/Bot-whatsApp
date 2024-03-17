#Bibliotecas
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
#Ir para o zap
driver = webdriver.Chrome(ChromeDriverManager.install())
driver.get('https://web.whatsapp.com/')
time.sleep(30)
#Buscar contatos
contatos = ['Teste bot', 'Pai']
#Enviar mensagens
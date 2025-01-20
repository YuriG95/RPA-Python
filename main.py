from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.chrome.service import Service
import time

#Configurar webdriver
driver_path = "chromedriver.exe"
service = Service(driver_path)

print("Seja bem vindo! ")
email = (input("Digite seu email:  "))
senha = (input("Digite sua senha:  "))

if email == "" or senha == "":
   print("Erro não e possivel passar os dados vazios")
else:
  try:
    # Inicializar o WebDriver do Chrome
    driver = webdriver.Chrome(service=service)

    #Acessar o site
    driver.get("https://us.account.battle.net/login/pt/") #Url passado do site batle net mas fica a escolha do usuario
    time.sleep(2)

    #preencher o formulario de login 
    username_field = driver.find_element(By.ID, "accountName")
    password_field = driver.find_element(By.ID, "password" )

    username_field.send_keys(email)
    password_field.send_keys(senha)
    password_field.send_keys(Keys.RETURN) #Apertar enter apos a senha
    time.sleep(3)

    #Coletar dados de uma pagina apos o login
    data_element =driver.find_element(By.ID,"app" )
    print("Dados coletados", data_element.text)

    #fechar navegador
    driver.quit()
  except Exception as e:
         print("Erro: " , e)
         driver.quit()

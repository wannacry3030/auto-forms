import time
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(options=options, service=servico)


#passo1
navegador.get("https://forms.office.com/Pages/ResponsePage.aspx?id=GUvwznZ3lEq4mzdcd6j5NqOa5rHBDstAhO363trnMtJUNlJKNFVEOVlUTUlTNkZLR0MzQjNDQlVROCQlQCN0PWcu&wdLOR=c3AADC4C4-C6DA-4993-90EC-8BE19D05F1B6")

time.sleep(1)

#1
navegador.find_element('xpath', '//*[@id="SelectId_0_placeholder"]').click()
#1.1
navegador.find_element('xpath', '/html/body/div/div/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div/div/div[3]/div/div/div[2]/div[2]').click()
#2
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div/input').send_keys("181766")
#3
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[3]/div/div[3]/div/div/input').send_keys("Horizonte Logistica")
#4
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[4]/div/div[3]/div/div/input').send_keys("lucas.oliveira@grupohorizonte.com.br")
#5
navegador.find_element('xpath', '//*[@id="SelectId_1_placeholder"]').click()
#5.1
navegador.find_element('xpath', '/html/body/div/div/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div[5]/div/div[3]/div/div/div[2]/div[1]').click()
#6
navegador.find_element('xpath', '//*[@id="SelectId_2_placeholder"]').click()
#6.1
navegador.find_element('xpath', '/html/body/div/div/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div[6]/div/div[3]/div/div/div[2]/div[11]').click()
#7
navegador.find_element('xpath', '/html/body/div/div/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div[7]/div/div[3]/div/div[2]/div/label/input').click()
#8
navegador.find_element('xpath', '/html/body/div/div/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div[8]/div/div[3]/div/div[2]/div/label/input').click()
#9
navegador.find_element('xpath', '//*[@id="SelectId_3_placeholder"]').click()
#9.1
navegador.find_element('xpath', '/html/body/div/div/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div[9]/div/div[3]/div/div/div[2]/div[3]').click()
#10
navegador.find_element('xpath', '//*[@id="SelectId_4_placeholder"]').click()
#10.1
navegador.find_element('xpath', '//*[@id="SelectId_4"]/div[2]/div[11]').click()
#11 NOME  
navegador.find_element('xpath', '/html/body/div/div/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div[11]/div/div[3]/div/div/input').send_keys('claudio de freitas alves')
#12 
navegador.find_element('xpath', '/html/body/div/div/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div[12]/div/div[3]/div/div/input').send_keys('distribuição')
#13
navegador.find_element('xpath', '/html/body/div/div/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div[13]/div/div[3]/div/div/textarea').send_keys('Uso correto do EPI.')
#14 CLICK FINAL
navegador.find_element('xpath', '//*[@id="cover-page-root"]/div[1]/div[2]/div[3]/div[1]/button').click()

time.sleep(2)

navegador.quit()
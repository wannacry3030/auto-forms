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
#passo2
navegador.find_element('xpath', '//*[@id="SelectId_0_placeholder"]').click()
navegador.find_element('xpath', '//*[@id="SelectId_0"]/div[2]/div[2]').click()
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div/input').send_keys("181766")
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[3]/div/div[3]/div/div/input').send_keys("Horizonte Logistica")
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[4]/div/div[3]/div/div/input').send_keys("lucas.oliveira@grupohorizonte.com.br")
navegador.find_element('xpath', '//*[@id="SelectId_1_placeholder"]/i').click()
navegador.find_element('xpath', '//*[@id="SelectId_1"]/div[2]/div[1]').click()
navegador.find_element('xpath', '//*[@id="SelectId_2_placeholder"]').click()
navegador.find_element('xpath', '//*[@id="SelectId_2"]/div[2]/div[11]').click()
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[7]/div/div[3]/div/div[2]/div/label/input').click()
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[8]/div/div[3]/div/div[2]/div/label/input').click()
navegador.find_element('xpath', '//*[@id="SelectId_3_placeholder"]').click()

navegador.find_element('xpath', '//*[@id="SelectId_3"]/div[2]/div[2]').click()
navegador.find_element('xpath', '//*[@id="SelectId_4_placeholder"]/i').click()
navegador.find_element('xpath', '//*[@id="SelectId_4"]/div[2]/div[11]').click()

navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[11]/div/div[3]/div/div/textarea').send_keys('Preenchimento do formulario')
time.sleep(1)
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[12]/div/div[3]/div/div/textarea').send_keys("Infesta????o de aedes aegypti (dengue), na sala ADM HORIZONTE..")

navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[3]/div[1]/button/div').click()





# Open a new tab
navegador.execute_script("window.open('https://forms.office.com/Pages/ResponsePage.aspx?id=GUvwznZ3lEq4mzdcd6j5NqOa5rHBDstAhO363trnMtJUNlJKNFVEOVlUTUlTNkZLR0MzQjNDQlVROCQlQCN0PWcu&wdLOR=c3AADC4C4-C6DA-4993-90EC-8BE19D05F1B6', '_blank');")

# Switch to the new tab
navegador.switch_to.window(navegador.window_handles[1])

time.sleep(1)
#passo2
navegador.find_element('xpath', '//*[@id="SelectId_0_placeholder"]').click()
navegador.find_element('xpath', '//*[@id="SelectId_0"]/div[2]/div[2]').click()
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div/input').send_keys("181766")
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[3]/div/div[3]/div/div/input').send_keys("Horizonte Logistica")
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[4]/div/div[3]/div/div/input').send_keys("lucas.oliveira@grupohorizonte.com.br")
navegador.find_element('xpath', '//*[@id="SelectId_1_placeholder"]/i').click()
navegador.find_element('xpath', '//*[@id="SelectId_1"]/div[2]/div[1]').click()
navegador.find_element('xpath', '//*[@id="SelectId_2_placeholder"]').click()
navegador.find_element('xpath', '//*[@id="SelectId_2"]/div[2]/div[11]').click()
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[7]/div/div[3]/div/div[2]/div/label/input').click()
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[8]/div/div[3]/div/div[2]/div/label/input').click()
navegador.find_element('xpath', '//*[@id="SelectId_3_placeholder"]').click()

navegador.find_element('xpath', '//*[@id="SelectId_3"]/div[2]/div[2]').click()
navegador.find_element('xpath', '//*[@id="SelectId_4_placeholder"]/i').click()
navegador.find_element('xpath', '//*[@id="SelectId_4"]/div[2]/div[11]').click()

navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[11]/div/div[3]/div/div/textarea').send_keys('Preenchimento do formulario')

navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[12]/div/div[3]/div/div/textarea').send_keys("Infesta????o de aedes aegypti (dengue), na sala ADM HORIZONTE --")

navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[3]/div[1]/button/div').click()



# Open a new tab
navegador.execute_script("window.open('https://forms.office.com/Pages/ResponsePage.aspx?id=GUvwznZ3lEq4mzdcd6j5NqOa5rHBDstAhO363trnMtJUNlJKNFVEOVlUTUlTNkZLR0MzQjNDQlVROCQlQCN0PWcu&wdLOR=c3AADC4C4-C6DA-4993-90EC-8BE19D05F1B6', '_blank');")

# Switch to the new tab
navegador.switch_to.window(navegador.window_handles[2])

time.sleep(1)
#passo2
navegador.find_element('xpath', '//*[@id="SelectId_0_placeholder"]').click()
navegador.find_element('xpath', '//*[@id="SelectId_0"]/div[2]/div[2]').click()
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div/input').send_keys("181766")
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[3]/div/div[3]/div/div/input').send_keys("Horizonte Logistica")
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[4]/div/div[3]/div/div/input').send_keys("lucas.oliveira@grupohorizonte.com.br")
navegador.find_element('xpath', '//*[@id="SelectId_1_placeholder"]/i').click()
navegador.find_element('xpath', '//*[@id="SelectId_1"]/div[2]/div[1]').click()
navegador.find_element('xpath', '//*[@id="SelectId_2_placeholder"]').click()
navegador.find_element('xpath', '//*[@id="SelectId_2"]/div[2]/div[11]').click()
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[7]/div/div[3]/div/div[2]/div/label/input').click()
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[8]/div/div[3]/div/div[2]/div/label/input').click()
navegador.find_element('xpath', '//*[@id="SelectId_3_placeholder"]').click()

navegador.find_element('xpath', '//*[@id="SelectId_3"]/div[2]/div[2]').click()
navegador.find_element('xpath', '//*[@id="SelectId_4_placeholder"]/i').click()
navegador.find_element('xpath', '//*[@id="SelectId_4"]/div[2]/div[11]').click()

navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[11]/div/div[3]/div/div/textarea').send_keys('Preenchimento do formulario')

navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[12]/div/div[3]/div/div/textarea').send_keys("Infesta????o de aedes aegypti (dengue), na sala ADM HORIZONTE --")

navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[3]/div[1]/button/div').click()



# Open a new tab
navegador.execute_script("window.open('https://forms.office.com/Pages/ResponsePage.aspx?id=GUvwznZ3lEq4mzdcd6j5NqOa5rHBDstAhO363trnMtJUNlJKNFVEOVlUTUlTNkZLR0MzQjNDQlVROCQlQCN0PWcu&wdLOR=c3AADC4C4-C6DA-4993-90EC-8BE19D05F1B6', '_blank');")

# Switch to the new tab
navegador.switch_to.window(navegador.window_handles[3])

time.sleep(1)
#passo2
navegador.find_element('xpath', '//*[@id="SelectId_0_placeholder"]').click()
navegador.find_element('xpath', '//*[@id="SelectId_0"]/div[2]/div[2]').click()
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div/input').send_keys("181766")
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[3]/div/div[3]/div/div/input').send_keys("Horizonte Logistica")
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[4]/div/div[3]/div/div/input').send_keys("lucas.oliveira@grupohorizonte.com.br")
navegador.find_element('xpath', '//*[@id="SelectId_1_placeholder"]/i').click()
navegador.find_element('xpath', '//*[@id="SelectId_1"]/div[2]/div[1]').click()
navegador.find_element('xpath', '//*[@id="SelectId_2_placeholder"]').click()
navegador.find_element('xpath', '//*[@id="SelectId_2"]/div[2]/div[11]').click()
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[7]/div/div[3]/div/div[2]/div/label/input').click()
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[8]/div/div[3]/div/div[2]/div/label/input').click()
navegador.find_element('xpath', '//*[@id="SelectId_3_placeholder"]').click()

navegador.find_element('xpath', '//*[@id="SelectId_3"]/div[2]/div[2]').click()
navegador.find_element('xpath', '//*[@id="SelectId_4_placeholder"]/i').click()
navegador.find_element('xpath', '//*[@id="SelectId_4"]/div[2]/div[11]').click()

navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[11]/div/div[3]/div/div/textarea').send_keys('Preenchimento do formulario')

navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[12]/div/div[3]/div/div/textarea').send_keys("Infesta????o de aedes aegypti (dengue), na sala ADM HORIZONTE --")

navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[3]/div[1]/button/div').click()



# Open a new tab
navegador.execute_script("window.open('https://forms.office.com/Pages/ResponsePage.aspx?id=GUvwznZ3lEq4mzdcd6j5NqOa5rHBDstAhO363trnMtJUNlJKNFVEOVlUTUlTNkZLR0MzQjNDQlVROCQlQCN0PWcu&wdLOR=c3AADC4C4-C6DA-4993-90EC-8BE19D05F1B6', '_blank');")

# Switch to the new tab
navegador.switch_to.window(navegador.window_handles[4])

time.sleep(1)
#passo2
navegador.find_element('xpath', '//*[@id="SelectId_0_placeholder"]').click()
navegador.find_element('xpath', '//*[@id="SelectId_0"]/div[2]/div[2]').click()
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div/input').send_keys("181766")
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[3]/div/div[3]/div/div/input').send_keys("Horizonte Logistica")
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[4]/div/div[3]/div/div/input').send_keys("lucas.oliveira@grupohorizonte.com.br")
navegador.find_element('xpath', '//*[@id="SelectId_1_placeholder"]/i').click()
navegador.find_element('xpath', '//*[@id="SelectId_1"]/div[2]/div[1]').click()
navegador.find_element('xpath', '//*[@id="SelectId_2_placeholder"]').click()
navegador.find_element('xpath', '//*[@id="SelectId_2"]/div[2]/div[11]').click()
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[7]/div/div[3]/div/div[2]/div/label/input').click()
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[8]/div/div[3]/div/div[2]/div/label/input').click()
navegador.find_element('xpath', '//*[@id="SelectId_3_placeholder"]').click()

navegador.find_element('xpath', '//*[@id="SelectId_3"]/div[2]/div[2]').click()
navegador.find_element('xpath', '//*[@id="SelectId_4_placeholder"]/i').click()
navegador.find_element('xpath', '//*[@id="SelectId_4"]/div[2]/div[11]').click()

navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[11]/div/div[3]/div/div/textarea').send_keys('Preenchimento do formulario')

navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[12]/div/div[3]/div/div/textarea').send_keys("Infesta????o de aedes aegypti (dengue), na sala ADM HORIZONTE --")

navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[3]/div[1]/button/div').click()



# Open a new tab
navegador.execute_script("window.open('https://forms.office.com/Pages/ResponsePage.aspx?id=GUvwznZ3lEq4mzdcd6j5NqOa5rHBDstAhO363trnMtJUNlJKNFVEOVlUTUlTNkZLR0MzQjNDQlVROCQlQCN0PWcu&wdLOR=c3AADC4C4-C6DA-4993-90EC-8BE19D05F1B6', '_blank');")

# Switch to the new tab
navegador.switch_to.window(navegador.window_handles[5])

time.sleep(1)
#passo2
navegador.find_element('xpath', '//*[@id="SelectId_0_placeholder"]').click()
navegador.find_element('xpath', '//*[@id="SelectId_0"]/div[2]/div[2]').click()
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div/input').send_keys("181766")
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[3]/div/div[3]/div/div/input').send_keys("Horizonte Logistica")
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[4]/div/div[3]/div/div/input').send_keys("lucas.oliveira@grupohorizonte.com.br")
navegador.find_element('xpath', '//*[@id="SelectId_1_placeholder"]/i').click()
navegador.find_element('xpath', '//*[@id="SelectId_1"]/div[2]/div[1]').click()
navegador.find_element('xpath', '//*[@id="SelectId_2_placeholder"]').click()
navegador.find_element('xpath', '//*[@id="SelectId_2"]/div[2]/div[11]').click()
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[7]/div/div[3]/div/div[2]/div/label/input').click()
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[8]/div/div[3]/div/div[2]/div/label/input').click()
navegador.find_element('xpath', '//*[@id="SelectId_3_placeholder"]').click()

navegador.find_element('xpath', '//*[@id="SelectId_3"]/div[2]/div[2]').click()
navegador.find_element('xpath', '//*[@id="SelectId_4_placeholder"]/i').click()
navegador.find_element('xpath', '//*[@id="SelectId_4"]/div[2]/div[11]').click()

navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[11]/div/div[3]/div/div/textarea').send_keys('Preenchimento do formulario')

navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[12]/div/div[3]/div/div/textarea').send_keys("Infesta????o de aedes aegypti (dengue), na sala ADM HORIZONTE --")

navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[3]/div[1]/button/div').click()



# Open a new tab
navegador.execute_script("window.open('https://forms.office.com/Pages/ResponsePage.aspx?id=GUvwznZ3lEq4mzdcd6j5NqOa5rHBDstAhO363trnMtJUNlJKNFVEOVlUTUlTNkZLR0MzQjNDQlVROCQlQCN0PWcu&wdLOR=c3AADC4C4-C6DA-4993-90EC-8BE19D05F1B6', '_blank');")

# Switch to the new tab
navegador.switch_to.window(navegador.window_handles[6])

time.sleep(1)
#passo2
navegador.find_element('xpath', '//*[@id="SelectId_0_placeholder"]').click()
navegador.find_element('xpath', '//*[@id="SelectId_0"]/div[2]/div[2]').click()
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div/input').send_keys("181766")
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[3]/div/div[3]/div/div/input').send_keys("Horizonte Logistica")
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[4]/div/div[3]/div/div/input').send_keys("lucas.oliveira@grupohorizonte.com.br")
navegador.find_element('xpath', '//*[@id="SelectId_1_placeholder"]/i').click()
navegador.find_element('xpath', '//*[@id="SelectId_1"]/div[2]/div[1]').click()
navegador.find_element('xpath', '//*[@id="SelectId_2_placeholder"]').click()
navegador.find_element('xpath', '//*[@id="SelectId_2"]/div[2]/div[11]').click()
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[7]/div/div[3]/div/div[2]/div/label/input').click()
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[8]/div/div[3]/div/div[2]/div/label/input').click()
navegador.find_element('xpath', '//*[@id="SelectId_3_placeholder"]').click()

navegador.find_element('xpath', '//*[@id="SelectId_3"]/div[2]/div[2]').click()
navegador.find_element('xpath', '//*[@id="SelectId_4_placeholder"]/i').click()
navegador.find_element('xpath', '//*[@id="SelectId_4"]/div[2]/div[11]').click()

navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[11]/div/div[3]/div/div/textarea').send_keys('Preenchimento do formulario')

navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[12]/div/div[3]/div/div/textarea').send_keys("Infesta????o de aedes aegypti (dengue), na sala ADM HORIZONTE --")

navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[3]/div[1]/button/div').click()



# Open a new tab
navegador.execute_script("window.open('https://forms.office.com/Pages/ResponsePage.aspx?id=GUvwznZ3lEq4mzdcd6j5NqOa5rHBDstAhO363trnMtJUNlJKNFVEOVlUTUlTNkZLR0MzQjNDQlVROCQlQCN0PWcu&wdLOR=c3AADC4C4-C6DA-4993-90EC-8BE19D05F1B6', '_blank');")

# Switch to the new tab
navegador.switch_to.window(navegador.window_handles[7])

time.sleep(1)
#passo2
navegador.find_element('xpath', '//*[@id="SelectId_0_placeholder"]').click()
navegador.find_element('xpath', '//*[@id="SelectId_0"]/div[2]/div[2]').click()
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div/input').send_keys("181766")
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[3]/div/div[3]/div/div/input').send_keys("Horizonte Logistica")
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[4]/div/div[3]/div/div/input').send_keys("lucas.oliveira@grupohorizonte.com.br")
navegador.find_element('xpath', '//*[@id="SelectId_1_placeholder"]/i').click()
navegador.find_element('xpath', '//*[@id="SelectId_1"]/div[2]/div[1]').click()
navegador.find_element('xpath', '//*[@id="SelectId_2_placeholder"]').click()
navegador.find_element('xpath', '//*[@id="SelectId_2"]/div[2]/div[11]').click()
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[7]/div/div[3]/div/div[2]/div/label/input').click()
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[8]/div/div[3]/div/div[2]/div/label/input').click()
navegador.find_element('xpath', '//*[@id="SelectId_3_placeholder"]').click()

navegador.find_element('xpath', '//*[@id="SelectId_3"]/div[2]/div[2]').click()
navegador.find_element('xpath', '//*[@id="SelectId_4_placeholder"]/i').click()
navegador.find_element('xpath', '//*[@id="SelectId_4"]/div[2]/div[11]').click()

navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[11]/div/div[3]/div/div/textarea').send_keys('Preenchimento do formulario')

navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[12]/div/div[3]/div/div/textarea').send_keys("Infesta????o de aedes aegypti (dengue), na sala ADM HORIZONTE --")

navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[3]/div[1]/button/div').click()



# Open a new tab
navegador.execute_script("window.open('https://forms.office.com/Pages/ResponsePage.aspx?id=GUvwznZ3lEq4mzdcd6j5NqOa5rHBDstAhO363trnMtJUNlJKNFVEOVlUTUlTNkZLR0MzQjNDQlVROCQlQCN0PWcu&wdLOR=c3AADC4C4-C6DA-4993-90EC-8BE19D05F1B6', '_blank');")

# Switch to the new tab
navegador.switch_to.window(navegador.window_handles[8])

time.sleep(1)
#passo2
navegador.find_element('xpath', '//*[@id="SelectId_0_placeholder"]').click()
navegador.find_element('xpath', '//*[@id="SelectId_0"]/div[2]/div[2]').click()
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div/input').send_keys("181766")
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[3]/div/div[3]/div/div/input').send_keys("Horizonte Logistica")
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[4]/div/div[3]/div/div/input').send_keys("lucas.oliveira@grupohorizonte.com.br")
navegador.find_element('xpath', '//*[@id="SelectId_1_placeholder"]/i').click()
navegador.find_element('xpath', '//*[@id="SelectId_1"]/div[2]/div[1]').click()
navegador.find_element('xpath', '//*[@id="SelectId_2_placeholder"]').click()
navegador.find_element('xpath', '//*[@id="SelectId_2"]/div[2]/div[11]').click()
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[7]/div/div[3]/div/div[2]/div/label/input').click()
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[8]/div/div[3]/div/div[2]/div/label/input').click()
navegador.find_element('xpath', '//*[@id="SelectId_3_placeholder"]').click()

navegador.find_element('xpath', '//*[@id="SelectId_3"]/div[2]/div[2]').click()
navegador.find_element('xpath', '//*[@id="SelectId_4_placeholder"]/i').click()
navegador.find_element('xpath', '//*[@id="SelectId_4"]/div[2]/div[11]').click()

navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[11]/div/div[3]/div/div/textarea').send_keys('Preenchimento do formulario')

navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[12]/div/div[3]/div/div/textarea').send_keys("Infesta????o de aedes aegypti (dengue), na sala ADM HORIZONTE --")

navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[3]/div[1]/button/div').click()




# Open a new tab
navegador.execute_script("window.open('https://forms.office.com/Pages/ResponsePage.aspx?id=GUvwznZ3lEq4mzdcd6j5NqOa5rHBDstAhO363trnMtJUNlJKNFVEOVlUTUlTNkZLR0MzQjNDQlVROCQlQCN0PWcu&wdLOR=c3AADC4C4-C6DA-4993-90EC-8BE19D05F1B6', '_blank');")

# Switch to the new tab
navegador.switch_to.window(navegador.window_handles[9])

time.sleep(1)
#passo2
navegador.find_element('xpath', '//*[@id="SelectId_0_placeholder"]').click()
navegador.find_element('xpath', '//*[@id="SelectId_0"]/div[2]/div[2]').click()
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div/input').send_keys("181766")
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[3]/div/div[3]/div/div/input').send_keys("Horizonte Logistica")
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[4]/div/div[3]/div/div/input').send_keys("lucas.oliveira@grupohorizonte.com.br")
navegador.find_element('xpath', '//*[@id="SelectId_1_placeholder"]/i').click()
navegador.find_element('xpath', '//*[@id="SelectId_1"]/div[2]/div[1]').click()
navegador.find_element('xpath', '//*[@id="SelectId_2_placeholder"]').click()
navegador.find_element('xpath', '//*[@id="SelectId_2"]/div[2]/div[11]').click()
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[7]/div/div[3]/div/div[2]/div/label/input').click()
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[8]/div/div[3]/div/div[2]/div/label/input').click()
navegador.find_element('xpath', '//*[@id="SelectId_3_placeholder"]').click()

navegador.find_element('xpath', '//*[@id="SelectId_3"]/div[2]/div[2]').click()
navegador.find_element('xpath', '//*[@id="SelectId_4_placeholder"]/i').click()
navegador.find_element('xpath', '//*[@id="SelectId_4"]/div[2]/div[11]').click()

navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[11]/div/div[3]/div/div/textarea').send_keys('Preenchimento do formulario')

navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[12]/div/div[3]/div/div/textarea').send_keys("Infesta????o de aedes aegypti (dengue), na sala ADM HORIZONTE --")

navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[3]/div[1]/button/div').click()



# Open a new tab
navegador.execute_script("window.open('https://forms.office.com/Pages/ResponsePage.aspx?id=GUvwznZ3lEq4mzdcd6j5NqOa5rHBDstAhO363trnMtJUNlJKNFVEOVlUTUlTNkZLR0MzQjNDQlVROCQlQCN0PWcu&wdLOR=c3AADC4C4-C6DA-4993-90EC-8BE19D05F1B6', '_blank');")

# Switch to the new tab
navegador.switch_to.window(navegador.window_handles[10])

time.sleep(1)
#passo2
navegador.find_element('xpath', '//*[@id="SelectId_0_placeholder"]').click()
navegador.find_element('xpath', '//*[@id="SelectId_0"]/div[2]/div[2]').click()
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div/input').send_keys("181766")
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[3]/div/div[3]/div/div/input').send_keys("Horizonte Logistica")
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[4]/div/div[3]/div/div/input').send_keys("lucas.oliveira@grupohorizonte.com.br")
navegador.find_element('xpath', '//*[@id="SelectId_1_placeholder"]/i').click()
navegador.find_element('xpath', '//*[@id="SelectId_1"]/div[2]/div[1]').click()
navegador.find_element('xpath', '//*[@id="SelectId_2_placeholder"]').click()
navegador.find_element('xpath', '//*[@id="SelectId_2"]/div[2]/div[11]').click()
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[7]/div/div[3]/div/div[2]/div/label/input').click()
navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[8]/div/div[3]/div/div[2]/div/label/input').click()
navegador.find_element('xpath', '//*[@id="SelectId_3_placeholder"]').click()

navegador.find_element('xpath', '//*[@id="SelectId_3"]/div[2]/div[2]').click()
navegador.find_element('xpath', '//*[@id="SelectId_4_placeholder"]/i').click()
navegador.find_element('xpath', '//*[@id="SelectId_4"]/div[2]/div[11]').click()

navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[11]/div/div[3]/div/div/textarea').send_keys('Preenchimento do formulario')

navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[12]/div/div[3]/div/div/textarea').send_keys("Infesta????o de aedes aegypti (dengue), na sala ADM HORIZONTE --")

navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[3]/div[1]/button/div').click()
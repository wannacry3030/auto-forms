from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(options=options, service=servico)
# Create a new ActionChains object
actions = ActionChains(navegador)

#passo1
navegador.get("https://forms.office.com/Pages/ResponsePage.aspx?id=GUvwznZ3lEq4mzdcd6j5NqOa5rHBDstAhO363trnMtJUNlJKNFVEOVlUTUlTNkZLR0MzQjNDQlVROCQlQCN0PWcu&wdLOR=c3AADC4C4-C6DA-4993-90EC-8BE19D05F1B6")

# Add actions to the ActionChains object
actions.click(navegador.find_element('xpath', '//*[@id="SelectId_0_placeholder"]'))
actions.click(navegador.find_element('xpath', '//*[@id="SelectId_0"]/div[2]/div[2]'))
actions.send_keys_to_element(navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div/input'), "181766")
actions.send_keys_to_element(navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[3]/div/div[3]/div/div/input'), "Horizonte Logistica")
actions.send_keys_to_element(navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[4]/div/div[3]/div/div/input'), "lucas.oliveira@grupohorizonte.com.br")
actions.click(navegador.find_element('xpath', '//*[@id="SelectId_1_placeholder"]/i'))
actions.click(navegador.find_element('xpath', '//*[@id="SelectId_1"]/div[2]/div[1]'))
actions.click(navegador.find_element('xpath', '//*[@id="SelectId_2_placeholder"]'))
actions.click(navegador.find_element('xpath', '//*[@id="SelectId_2"]/div[2]/div[11]'))
actions.click(navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[7]/div/div[3]/div/div[2]/div/label/input'))
actions.click(navegador.find_element('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[8]/div/div[3]/div/div[2]/div/label/input'))
actions.click(navegador.find_element('xpath', '//*[@id="SelectId_3_placeholder"]'))
actions.click(navegador.find_element('xpath', '//*[@id="SelectId_3"]/div[2]/div[3]'))
actions.click(navegador.find_element('xpath', '//*[@id="SelectId_4_placeholder"]'))
actions.click(navegador.find_element('xpath', '//*[@id="SelectId_4"]/div[2]/div[11]'))

# Perform all of the actions in the ActionChains object
actions.perform()


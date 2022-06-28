from wsgiref import headers

import pd as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep
import pandas as pd

options = Options()
#options.add_argument('--headless')  # não mostrar o navegador
options.add_argument('window-size=400,800')
options.add_experimental_option("detach", True)

s = Service('C:/Users/marco/Downloads/chromedriver.exe')
navegador = webdriver.Chrome(service=s, options=options)
navegador.get('https://marcosruizmrf.github.io/front-pgf/')
sleep(2)

button_stay = navegador.find_element_by_css_selector('button > span')
# TODO: clicar no segundo botao
nextButton = navegador.find_elements_by_tag_name('button')[-4]
button_stay.click()

sleep(2)

page_content = navegador.page_source
site = BeautifulSoup(page_content, 'html.parser')
#print(site.prettify())
sleep(2)
'''
noticia = site.findAll("mat-card-header")
for header in noticia:
   header.get('class'), print(header.find('mat-card-title').text[0:20])'''
dados_contents = []

contents = site.findAll('div', attrs={'class': 'content'})
for content in contents:
    title = site.findAll('mat-card-title', attrs={'class': 'mat-card-title'})[-1].text
    print('Título:', title)

    description = site.findAll('mat-card-subtitle', attrs={'class': 'mat-card-subtitle'})[0].text
    print('Descrição:', description)

    orderOfService = site.findAll('mat-card-subtitle', attrs={'class': 'mat-card-subtitle'})[-1].text
    print('Ordem de serviço:', orderOfService)

    #print()

    dados_contents.append([title, description, orderOfService])


dados = pd.DataFrame(dados_contents, columns=['Titulo', 'Descricao', 'Ordem de Servico'])

finalDados = dados.to_csv('contents2.csv', index=False, encoding='utf-8-sig')



'''title = [detalhe.text for detalhe in title]
print(title)'''

'''titulo = site.findAll("mat-card-header")
for header in titulo:
   header.get('class'), print(header.find('mat-card-subtitle').text)'''

'''divoContent = site.findAll("div")
for content in divoContent:
   content.get('class'), print(content.find('mat-card').text)'''

'''container = site.findAll('div', attrs={'class': 'content'})
container = [detalhe.text for detalhe in container]
container.append(container.count(container))
print(container)'''

'''
input_place = navegador.find_element_by_tag_name('input')
input_place.send_keys('São Paulo')
input_place.submit()
'''

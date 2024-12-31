from bs4 import BeautifulSoup 
# faz a leitura do html
with open('C:\\Users\\marcell.oliveira\\Desktop\\webScraping\\automacao_selenium_beat_pytangui\\asimov.html', 'r') as file:
  html_content = file.read()
#
ex = BeautifulSoup(html_content,'lxml')

# acessando o 1 paragrafo
#print(ex.find('p'))
#todos o paragrafos
#print(ex.find_all('p'))
#lendo o corpo do html
#print(ex.find_all('body'))

tags = ex.find_all(class_='paragrafos')

for tag in tags:
  print(tag.text)
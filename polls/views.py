from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

url_patio = "https://www.patiosavassi.com/lazer/cinema/"
url_bh = "https://www.bhshopping.com.br/lazer/cinema/"
url_diamond = "https://www.diamondmall.com.br/lazer/cinema"

# https://www.patiosavassi.com/lazer/cinema/pequena-sereia?d=2023-06-26
# eles tem a query “d” pra falar a data
# tb tem isso: #datasFilmes, mas não é obrigatório


def index(request):
    nomes_filmes = obterFilmes(url_diamond)
    template = loader.get_template("polls/index.html")
    context = {
        "nomes_filmes": nomes_filmes,
    }
    return HttpResponse(template.render(context, request))


def obterFilmes(url):
    driver = webdriver.Chrome()
    h5_class_nome = "text-uppercase.font-oswald"

    try:
        driver.get(url)

        nomes_filmes_elems = driver.find_elements(By.CLASS_NAME, h5_class_nome)
        nomes_filmes = filtrar_nomes(nomes_filmes_elems)  
        return nomes_filmes

    except Exception as ex:
        print(ex)
            
    driver.close()

def filtrar_nomes(nomes_filmes_elems: list[WebElement]):
        nome_class_filme = "text-uppercase font-oswald"
        nomes_filmes: list[str] = []
        for nome_filme_elem in nomes_filmes_elems:  
            nome_classe = nome_filme_elem.get_attribute("class")
            if(nome_class_filme == nome_classe):
                nomes_filmes.append(nome_filme_elem.text)
        return nomes_filmes
   

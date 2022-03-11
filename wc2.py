from bs4 import BeautifulSoup

from collections import Counter

import operator



import requests

def inicio(url):

    lista_palavras = []

    codigo_fonte = requests.get(url).text

    soup = BeautifulSoup(codigo_fonte,'html.parser')

    for palavra in soup.find_all('div', {'class' : 'entry-content'}):
        content = palavra.text

        words = content.lower().split()

        for word in words:
            lista_palavras.append(word)
        remove_caractere(lista_palavras)

def remove_caractere(palavras):

    simbols = '!@#$%¨&*()_+-,^~[({})].\;/"<>:'

    lista_limpa = []

    for word in palavras:
        for i in range(0, len(simbols)):
            word = word.replace(simbols[i], '')
        if len(word) > 0:
            lista_limpa.append(word)

    cria_dicionario(lista_limpa)


def cria_dicionario(lista_limpa):
    dicionario_de_palavras = {}

    for word in lista_limpa:
        if word in dicionario_de_palavras:
            dicionario_de_palavras[word] +=1
        else:
            dicionario_de_palavras[word] = 1

    for key, value in sorted(dicionario_de_palavras.items(),
                            key=operator.itemgetter(1)):
        print("% s : % s " % (key, value))

    c = Counter(dicionario_de_palavras)

    top = c.most_common(10)

    print(top)

inicio('https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar')


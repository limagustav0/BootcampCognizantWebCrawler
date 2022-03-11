from collections import Counter
from bs4 import BeautifulSoup
import operator
import requests


url = 'https://www.climatempo.com.br/'


def start(url):

    wordlist = []

    source_code = requests.get(url).text

    soup = BeautifulSoup(source_code,'html.parser')

    for each_text in soup.findAll('div',{'class' : 'entry-content'}):
        content = each_text .text

        words = content.lower().split()

        for each_word in words:
            wordlist.append(each_word)
        clear_wordlist(wordlist)


def clear_wordlist(wordlist):
    clean_list = []

    for word in wordlist:
        simbols = '!@#$%¨&*()_+-,.\;/"<>:'

        for i in range(0, len(simbols)):
            word = word.replace(simbols[i],'')

        if len(word) > 0:
            clean_list.append(word)

    create_dictionary(clean_list)

def create_dictionary(clean_list):
    word_count = {}

    for word in clean_list:
        if word in word_count:
            word_count[word] +=1
        else:
            word_count[word] = 1

    for key, value in sorted(word_count.items(),
                            key=operator.itemgetter(1)):
        print("% s : % s " % (key, value))

    c = Counter(word_count)

    top = c.most_common(10)

    print(top)

start('https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar')
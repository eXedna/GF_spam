
from ShG_rand import perem

import random

import requests
from bs4 import BeautifulSoup

def random_names(*args):
    resp = requests.get("https://kakzovut.ru/man.html").text
    _soup = BeautifulSoup(resp, "lxml")

    res = list()

    for i in _soup.find_all("div", {
        "class" : "nameslist"
    }):
        _st = str(i).find('.html">')
        _end = str(i).find('</a>')
        
        res.append(str(i)[_st + 7:_end])
        
    resp = requests.get("https://imena-znachenie.ru/imena/polskie/").text
    _soup = BeautifulSoup(resp, "lxml")
    
    
        
    if len(args) == 0:
        
        return res
    
    else:
        
        return random.choice(res)
        
def random_surnames(*args):
    resp = requests.get("http://imja.name/familii/pyatsot-chastykh-familij.shtml").text
    _soup = BeautifulSoup(resp, "lxml")
    
    res = list()
    
    for i in _soup.find_all("td",
                        {
                            "class" : "topin1"
                        }):
        _st = str(i).find('">')
        _end = str(i).find("</td>")
        
        res.append(str(i)[_st + 2: _end])
          
    res.sort(key = lambda x: x[0])
    res.remove(res[0]) 
    
    if len(args) == 0:
        return res
    else:
        
        return random.choice(res)
        
def random_patronymic():
    resp = requests.get("https://surnameonline.ru/patronymic-male.html").text
    _soup = BeautifulSoup(resp, "lxml")
    
    res = list()

    for i in _soup.find_all("li"):
        _st = str(i).find('html">')
        _end = str(i).find('</a>')
        
        
        res.append(str(i)[_st + 6: _end])
        
    return res

def FIO():
    fio = random.choice(random_surnames()) + " "\
        + random.choice(random_names()) + " "\
        + random.choice(random_patronymic())

    return fio

def AnimeNames():
    res = random.choice(perem.anime_list)
    
    return res

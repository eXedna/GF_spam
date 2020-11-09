try:
    from ShG_rand import perem
except:
    import perem

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
        
def random_patronymic(*args):
    resp = requests.get("https://surnameonline.ru/patronymic-male.html").text
    _soup = BeautifulSoup(resp, "lxml")
    
    res = list()

    for i in _soup.find_all("li"):
        _st = str(i).find('html">')
        _end = str(i).find('</a>')
        
        
        res.append(str(i)[_st + 6: _end])
        
    if len(args) == 0:
        return res
    else:
        return random.choice(res)

def FIO():
    fio = random_surnames("...") + " "\
        + random_names("...") + " "\
        + random_patronymic("...")

    return fio

def AnimeNames(*args):
    res = perem.anime_list
    
    if len(args) != 0:
        return random.choice(res)
    else:  
        return res

def Genders(*args):
    res = perem.genders
    
    if len(args) != 0:
        return random.choice(res)
    else:  
        return res

def RandomStations(*args):
    resp = requests.get("http://www.metro.ru/stations/codes/").text
    
    _soup = BeautifulSoup(resp, "lxml")
    
    _text, res = _soup.find_all("td"), list()
    
    for i in range(len(_text)):
        if (i + 1) % 3 != 0:
            res.append(str(_text[i]).replace("<td>", "").replace("</td>", ""))
        
    if len(args) != 0:
        return random.choice(res)
    else:
        return res                                              
    
def RandomWords(*args):
    url = "https://klavogonki.ru/vocs/203/"

    spl1 = "<div class=words>"
    spl2 = "</table>"
    spl3 = "<table cellspacing=0 cellpadding=0>"
    c = requests.post(url)
    text = c.text
    list_ = []
    text = text.split(spl1)[1]
    text = text.split(spl2)[0]
    text = text.split(spl3)[1]

    for i in text.split("\n"):
        if len(i) < 3:
            continue
        elif "тумбочка" in i:
            break

        list_.append(i.strip().split(">")[2].split("<")[0] )          
        
    if len(args) != 0:
        return random.choice(list_)
    else:
        return list_         
    
def RandomRes(qan = 5):
    gl_list = list()
    
    for i in AnimeNames():
        gl_list.append(i)
        
    for k in Genders():
        gl_list.append(k)

    for l in RandomStations():
        gl_list.append(l)

    for j in RandomWords():
        gl_list.append(j)
    
    res = str()
    
    if qan == 0:
        for i in range(random.randint(4, 70)):
            res += random.choice(gl_list)
            res += ' '
    else:    
        for i in range(qan):
            res += random.choice(gl_list)
            res += ' '
    
    return res

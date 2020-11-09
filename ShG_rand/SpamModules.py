from ShG_rand import perem
from bs4 import BeautifulSoup
import requests
import random
from ShG_rand import Identities

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
    
    for i in Identities.AnimeNames():
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
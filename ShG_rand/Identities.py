import requests
from bs4 import BeautifulSoup

def random_names():
    resp = requests.get("https://kakzovut.ru/man.html").text
    _soup = BeautifulSoup(resp, "lxml")

    res = list()

    for i in _soup.find_all("div", {
        "class" : "nameslist"
    }):
        _st = str(i).find('.html">')
        _end = str(i).find('</a>')
        
        res.append(str(i)[_st + 7:_end])
        
    return res
        
def random_surnames():
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
                    
    return res
        
def random_patronymic():
    resp = requests.get("https://surnameonline.ru/patronymic-male.html").text
    _soup = BeautifulSoup(resp, "lxml")
    
    res = list()

    for i in _soup.find_all("li"):
        _st = str(i).find('html">')
        _end = str(i).find('</a>')
        
        
        res.append(str(i)[_st + 6: _end])
        
    return res

def jojo():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4240.80 Safari/537.36 Edg/84.0.622.43'
    }

    for i in range(100):
        r = requests.post("https://forms.gle/tcx52iAwShSWFfE36", 
                            data = {
                                    "entry.1508740013": "pidor",
                                    "entry.297670832": "al;kvn;kslvn;ksldvnldsk;",
                                    "entry.234969710": "гениально просто гениально",
                                    "entry.347858582": "Да",
                                    "entry.347858582_sentinel": "",
                                    "fvv": "1",
                                    "draftResponse": '[null,null,"-798133708033948623"]',
                                    "pageHistory": "0",
                                    "fbzx": "-798133708033948623  "                          
                            },
                            headers = headers)

        print(";LKDNV;KLAVLK;DS;KLVNDSFK;N'LKNDF'LKNDLNDAF;NDFL;LDLVNA;LKVKNFDD;LVNAF;VKLNAVL;KNFLNV")

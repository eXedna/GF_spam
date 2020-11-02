# -*- coding: utf-8 -*-

import requests
import random
from LogPython import LogManager
import requests
LogManager = LogManager()
import threading
import click

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 Edg/86.0.622.43'
}

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

_first_answer_ = 'Зачем задавать такой вопрос, если проблема в индивидуальном расписании? - при индивидуальном расписании пропадали уроки, на каждом третьем уроке учеников больше чем посадочных мест, по большей мере хаотичное распределение по группам, например, информатика, физика и русский (когда распределение по уровню было). Даже непонятно, было ли распределение по уровню знаний по некоторым предметам. Отсутствие возможности перейти в другую группу, несмотря на то, что обещали, что это не будет проблемой. По словам преподавателей, чтобы перейти в группу с якобы более высоким уровнем преподавания, нужно решать дополнительное задание, которое будет (момент времени, когда оно должно там появиться естественно не оговаривается) в гугл классе этой группы. К слову, задания в гугл классе нет и, как я думаю, не будет. Так же интересует вопрос с окнами посреди школьного дня, пустые промежутки между седьмым и восьмым уроком, вовремя которых нужно заниматься непонятно чем. Из-за этих бесполезных промежутков ученики возвращаются домой минимум на два часа позже, когда могли вернуться домой и спокойно заняться своими делами, вместо этого они вынуждены находиться в школе и буквально "убивать время". Не говоря о том, что в некоторых случаях на уроке было только половина учеников, а вторая половина шла не по расписанию и из-за этого фактически пропадали уроки, можно сказать о том, что такой урок как физкультура полностью пропал из расписания и его по факту не существует как предмета уже месяц. Недавно поднялся вопрос о том, что группа Регины Рашидовны по геометрии не может написать акр просто потому, что для него нужно два подряд идущих урока, которые у нас есть только заочно. Казалось бы, Аветис Грачевич, как классный руководитель и директор, мог отпустить  учеников с одного, максимум с двух уроков, чтобы они без проблем написали акр. Я бы не писал(а) об этом инциденте, если бы все произошло так, как я предполагал(а), но акр эта группа так и не написала, поэтому пришлось высказать это. Короче говоря, в пуме царит хаос и беспорядок, противоположно словам директора в этой школе полнейшее отсутствие дисциплины и порядка. Не буду затрагивать тему некой иерархии в пуме, которая сформировалась еще в прошлом году и не распалась до сих пор. В некоторый момент времени возникло такое ощущение, что в пуме все делается в последний момент и на скорую руку. Никакой речи о планировании идти не может.'
   
_second_answer_ = 'Например, заранее планировать его, распределить количество учеников в каждой группе и сформировать расписание, а потом только вписывать фамилии учеников. В пум изначально должно было прийти фиксированное количество учеников или же набирали всех, кто захотел, лишь бы набрались классы? - если судить по новому набору учеников, экзамены были по общеобразовательной программе и не выходили за рамки обыкновенной школы. Изначально нужно было формировать расписание, а не доделывать его по десять раз. Если что-то стабильно не работает и исправить это не получается 2 месяца подряд, лучше перейти к тому, что с самого начала работало исправно. Кстати говоря, я не понимаю цели создания индивидуального расписания - разделение по группам были и в прошлом году, при чем достаточно удобное, а индивидуальное расписание только добавляет дополнительные каверзы и неудобства в и так сомнительный в последнее время учебный процесс.'

_third_answer_ = 'Если вы дочитали до этого момента, то я даже опущу момент о том, что подростки приходят в пум со знаниями, а если смогут выйти, то ни с чем. Осталось всего два вопрос, которые я бы хотел(а) обсудить. Первый из них - это огромное количество учеников, которые не только употребляют никотин, но и распространяют идею о его использовании. Казалось бы, пум должен быть кристально прозрачным - школе всего год и два месяца, но такое чувство, что ей уже десятилетие и всей администрации уже совершенно наплевать на происходящее внутри школьных стен. И наконец последний и более насущный вопрос - это выставление оценок новым зам. директором Кристиной Петровной. Оценки не только запаздывают, но иногда не соответствуют тому, что озвучили на уроке. Насколько я понял(а), расписание тоже составляла она, как я писал(а) ранее , расписанием я тоже категорически недоволен(а). Выводы делайте сами'

random_num = [1, 5]

jojo = random.choice(random_num)
 
def raid(a, b, c, d, e:int):
    while True:
        r = requests.post("https://docs.google.com/forms/u/0/d/e/1FAIpQLSfSA182h4jGDBIOcfyMgxeorPUokkb26QS4KZtMpB5H6O3ZcA/formResponse",
                        data={
                            "entry.447101162": "9",
                            "entry.1043893031": a,
                            "entry.806414291": b,
                            "entry.1293916860": c,
                            "entry.635193400": d,
                            "entry.1625556646": d,
                            "entry.24742125": d, 
                            "entry.731997419": d,
                            "entry.877852689": d,
                            "entry.325369499": d,
                            "entry.1508918824": d,
                            "entry.1003945292": "5",
                            "entry.635193400_sentinel": "",
                            "entry.1625556646_sentinel": "",
                            "entry.24742125_sentinel": "",
                            "entry.731997419_sentinel": "",
                            "entry.877852689_sentinel": "",
                            "entry.325369499_sentinel": "",
                            "entry.1508918824_sentinel": "",
                            "entry.1003945292_sentinel": "",
                            "fvv": "1",
                            "draftResponse": '[null,null,"-1322386903815409528"]',
                            "pageHistory": "0",
                            "fbzx": "-1322386903815409528"
                        },

                        headers=headers)
        
        if r.status_code == 200:
            status = "OK"
        elif r.status_code == 429:
            status ="TooManyRequests"
        elif r.status_code == 405:
            status = "MethodNotAllowed"
        else:
            status = "Undefined"

        thr = threading.enumerate()[len(threading.enumerate()) - 1]

        # print("==============================================\n\n\n")
        LogManager.info(f"{thr} === {r} === {e + 1} === {status}")
        # print("\n\n\n==============================================\n\n\n")

@click.command()
def start(): 

    i = 0
    while True:
        threading.Thread(target = raid, args = (_first_answer_, _second_answer_, _third_answer_, jojo, i)).start()
        i += 1
      
if __name__ == "__main__":  
    start()

# 'proxies = {
# "https" : "https://159.8.114.34:8123"
# }'


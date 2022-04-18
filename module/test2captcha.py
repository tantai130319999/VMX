import requests
from time import sleep, time
import string
import random

def ramdompass():
    chars_fixed = string.ascii_letters + string.digits
    password = "".join(random.choice(chars_fixed) for x in range(10))
    return password
start_time = time()
def gettoken(apikey,ggskey,urlpage):
    # send credentials to the service to solve captcha
    # returns service's captcha_id of captcha to be solved
    service_key = apikey # 2captcha service key
    google_site_key = ggskey
    pageurl = urlpage
    url = "http://2captcha.com/in.php?key=" + service_key + "&method=userrecaptcha&googlekey=" + google_site_key + "&pageurl=" + pageurl
    resp = requests.get(url)
    if resp.text[0:2] != 'OK':
        quit('Error. Captcha is not received')
    captcha_id = resp.text[3:]

    # fetch ready 'g-recaptcha-response' token for captcha_id  
    fetch_url = "http://2captcha.com/res.php?key=" + service_key + "&action=get&id=" + captcha_id
    for i in range(1, 100):
        sleep(5) # wait 5 sec.
        resp = requests.get(fetch_url)
        if resp.text[0:2] == 'OK':
            break
    return resp.text[3:]
def getapicodever(keyapi,userm,passm):
    for a in range(0, 10):
        url = 'https://fbvip.org/api/ordercode.php?apiKey='+ keyapi +'&type=1&user=' + userm + '&pass=' + passm
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        result = requests.get(url, headers=headers)
        json = result.content.decode()
        json = json[json.find('http://'):json.find('}') - 1]
        print(json)
        sleep(5)
        result2 = requests.get(json, headers=headers)
        json2 = result2.content.decode()
        print(json2[json2.find('message') + 10:])
        if json2[json2.find('message') + 10:] == 'Thành công"}':
            break
    if json2[json2.find('message') + 10:] == 'Thành công"}':
        codever = json2[json2.find('code') + 7:json2.find('code') + 13]
        print(codever)
    return codever
def getsdtsim(keyapi):
    for a in range(0, 10):
        url = 'https://chothuesimcode.com/api?act=number&apik=' + keyapi + '&appId=1030'
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        result = requests.get(url, headers=headers)
        json = result.content.decode()
        print(json)
        sleep(5)
        print(json[json.find('Msg') + 6:json.find('Msg') + 8])
        if json[json.find('Msg') + 6:json.find('Msg') + 8] == 'OK':
            break
    if json[json.find('Msg') + 6:json.find('Msg') + 8] == 'OK':
        codever = []
        codever.append(json[json.find('Number') + 9:json.find('Number') + 18])
        codever.append(json[json.find('Id') + 4:json.find('Number') - 2])
        print(codever)
    return codever
def getcodesim(keyapi,idsim):
    for a in range(0, 30):
        url = 'https://chothuesimcode.com/api?act=code&apik=' + keyapi + '&id=' + idsim
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        result = requests.get(url, headers=headers)
        json = result.content.decode()
        print(json)
        sleep(5)
        print(json[json.find('Msg') + 6:json.find('Msg') + 8])
        if json[json.find('Msg') + 6:json.find('Msg') + 8] == 'Đã':
            break
    if json[json.find('Msg') + 6:json.find('Msg') + 8] == 'Đã':
        codever=json[json.find('Code') + 7:json.find('Cost') - 2]
        print(codever)
    return codever    
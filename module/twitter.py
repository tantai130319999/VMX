from logging import error
import time
import names
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import json
import pyclip
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import messagebox 
from tkinter.filedialog import askopenfilename
import glob, os, os.path
from tkinter.ttk import Progressbar
from collections import OrderedDict
import zipfile
import random
import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from threading import Thread
import threading
from module import test2captcha
def xulyfile(file):
    listmail = []
    with open(file, encoding = 'utf-8') as file:
        listdata = file.readlines()
    for a in listdata:
        text = a
        timx = text.find('\n')
        if timx != -1:
            listmail.append(text[:timx])
        else:
            listmail.append(text)
    return listmail
def xulyfile2(file):
    listmail = []
    with open(file, encoding = 'latin-1') as file:
        listdata = file.readlines()
    for a in listdata:
        text = a
        timx = text.find('\n')
        if timx != -1:
            listmail.append(text[:timx])
        else:
            listmail.append(text)
    return listmail
def auto(ip,port,up,pp,file,file2):
    def getPlugin(proxy_host, proxy_port, proxy_user, proxy_pass):
        manifest_json = """
        {
            "version": "1.0.0",
            "manifest_version": 2,
            "name": "Chrome Proxy",
            "permissions": [
                "proxy",
                "tabs",
                "unlimitedStorage",
                "storage",
                "<all_urls>",
                "webRequest",
                "webRequestBlocking"
            ],
            "background": {
                "scripts": ["background.js"]
            },
            "minimum_chrome_version":"22.0.0"
        }
        """

        background_js = """
        var config = {
                mode: "fixed_servers",
                rules: {
                singleProxy: {
                    scheme: "http",
                    host: "%s",
                    port: parseInt(%s)
                },
                bypassList: ["localhost"]
                }
            };

        chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

        function callbackFn(details) {
            return {
                authCredentials: {
                    username: "%s",
                    password: "%s"
                }
            };
        }

        chrome.webRequest.onAuthRequired.addListener(
                    callbackFn,
                    {urls: ["<all_urls>"]},
                    ['blocking']
        );
        """ % (proxy_host, proxy_port, proxy_user, proxy_pass)
        pluginfile = 'proxy_auth_plugin.zip'

        with zipfile.ZipFile(pluginfile, 'w') as zp:
            zp.writestr("manifest.json", manifest_json)
            zp.writestr("background.js", background_js)
        
        return pluginfile
    def run(ip,port,up,pp):
        proxyArgsList = [
                            {
                                'proxy_host': '196.242.245.23',
                                'proxy_port': '11112',
                                'proxy_user': 'midi9x',
                                'proxy_pass': 'JNX0R1IECLADXNVC98EPRGQW',
                            },
                            {
                                'proxy_host': '196.242.245.33',
                                'proxy_port': '11112',
                                'proxy_user': 'midi9x',
                                'proxy_pass': 'JNX0R1IECLADXNVC98EPRGQW',
                            },
                            {
                                'proxy_host': '196.242.245.100',
                                'proxy_port': '11112',
                                'proxy_user': 'midi9x',
                                'proxy_pass': 'JNX0R1IECLADXNVC98EPRGQW',
                            },
                            {
                                'proxy_host': '196.242.245.199',
                                'proxy_port': '11112',
                                'proxy_user': 'midi9x',
                                'proxy_pass': 'JNX0R1IECLADXNVC98EPRGQW',
                            }
                            
                        ]
        if ip != "":
            chromeOptions = webdriver.ChromeOptions()
            chromeOptions.add_extension(getPlugin(ip,port,up,pp))
            name = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=chromeOptions)
        else:
            name = webdriver.Chrome(executable_path="chromedriver.exe")
        name.execute_script("window.open('{}');".format('https://outlook.live.com/'))
        def waite(el):
            waite = name.find_elements_by_name(el)
            while len(waite) == 0:
                waite = name.find_elements_by_name(el)
            return waite
        def waites(el):
            waites = name.find_elements_by_xpath(el)
            while len(waites) == 0:
                waites = name.find_elements_by_xpath(el)
            return waites
        def changeacc(file,file2):
            listacc = file
            listmail = file2
            for acc in listacc:
                try:
                    userlog = acc[:acc.find('|')]
                    passlog = acc[acc.find('|') + 1:]
                    def printacc(getusername,getnamtao,getquocgia,follow):
                        with open('output/twitter.txt','a+', encoding = 'utf-8') as luufile:
                            luufile.write(userlog +'|' + 'tantai1303' + '|' + getusername + '|' + getnamtao + '|' + getquocgia + '|' + follow + '\n')
                    window1 = name.window_handles[0]
                    name.switch_to_window(window1)
                    name.get('https://twitter.com/login')
                    user = waite('session[username_or_email]')
                    user[0].send_keys(userlog)
                    passw = waite('session[password]')
                    passw[0].send_keys(passlog)
                    login = name.find_element_by_xpath('//span[text()="Log in"]')
                    login.click()
                    time.sleep(3)
                    try:
                        error = name.find_element_by_xpath('//div[@role="alert"]')
                        txt1.insert(INSERT,"TK:       " + userlog + "      không thể login")
                        window.update()
                    except:
                        name.get('https://twitter.com/settings/password')
                        passcu = waite('current_password')
                        passcu[0].send_keys(passlog)
                        newpass = waite('new_password')
                        newpass[0].send_keys('tantai130319')
                        confixpass = waite('password_confirmation')
                        confixpass[0].send_keys('tantai130319')
                        savepass = name.find_element_by_xpath('//span[text()="Save"]')
                        savepass.click()
                        time.sleep(3)
                        name.get('https://twitter.com/settings/your_twitter_data/account')
                        currpass = waite('current_password')
                        currpass[0].send_keys('tantai130319')
                        confirm = name.find_element_by_xpath('//span[text()="Confirm"]')
                        confirm.click()
                        time.sleep(1)
                        name.get('https://twitter.com/settings/email')
                        time.sleep(3)
                        try:
                            Addmail = name.find_element_by_xpath('//span[text()="Add email address"]')
                            Addmail.click()
                        except:
                            updatemail = name.find_element_by_xpath('//span[text()="Update email address"]')
                            updatemail.click()
                        nhappass = waite('password')
                        nhappass[0].send_keys('tantai130319')
                        Nextp = name.find_element_by_xpath('//span[text()="Next"]')
                        Nextp.click()
                        for mail in listmail:
                            try:
                                hotmail = mail[:mail.find('|')]
                                passmail = mail[mail.find('|') + 1:]
                                Mailadd = waite('email')
                                Mailadd[0].send_keys(hotmail)
                                time.sleep(3)
                                Nextm = waites('//span[text()="Next"]')
                                Nextm[0].click()
                                window2 = name.window_handles[1]
                                name.switch_to_window(window2)
                                loginhotmail = waites('//a[text()="Sign in"]')
                                loginhotmail[0].click()
                                addhotmail = waite('loginfmt')
                                addhotmail[0].send_keys(hotmail)
                                vaomail = name.find_element_by_id('idSIButton9')
                                vaomail.click()
                                addpassmail = waite('passwd')
                                addpassmail[0].send_keys(passmail)
                                time.sleep(1)
                                vaomail2 = waites('//input[@id="idSIButton9"]//..')
                                try:
                                    vaomail2[0].click()
                                except:
                                    time.sleep(2)
                                    vaomail2[0].click()
                                getcode = waites('//span[contains(text(),"is your Twitter ver")]')
                                code = getcode[0].text
                                findcode = code[:code.find(' ')]
                                window1 = name.window_handles[0]
                                name.switch_to_window(window1)
                                vercode = waite('verfication_code')
                                vercode[0].send_keys(findcode)
                                Nextv = name.find_element_by_xpath('//span[text()="Verify"]')
                                Nextv.click()
                                time.sleep(1)
                                name.get('https://twitter.com/settings/phone')
                                time.sleep(3)
                                try:
                                    delephone = name.find_element_by_xpath('//span[text()="Delete phone number"]')
                                    delephone.click()
                                    time.sleep(1)
                                except:
                                    pass
                                name.get('https://twitter.com/settings/your_twitter_data/account')
                                getusername = waites('//div//span[text()="Username"]//..//..//div[2]//span').text
                                getnamtao = waites('//div//span[text()="Account creation"]//..//..//div[2]//span').text
                                getquocgia = waites('//div//span[text()="Country"]//..//..//div[2]//span').text
                                name.get('https://twitter.com/sidemeninsecure')
                                follow = waites('//div//span[text()="Followers"]//..//..//span[1]//span').text
                                printacc(getusername,getnamtao,getquocgia,follow) 
                            except:
                                pass 
                except:
                    pass
        changeacc(file,file2)
    run(ip,port,up,pp)
# p = ['midi9x1','midi9x2','midi9x3']
# a = threading.Thread(target=auto, args=(0,))
# a.start()
# b = threading.Thread(target=auto, args=(1,))
# b.start()
# c = threading.Thread(target=auto, args=(2,))
# c.start()
# file = xulyfile("")
# file2 = xulyfile2("")
# auto("","","","",file,file2)
# towcaptcha = test2captcha.gettoken('abc','abc','abc')

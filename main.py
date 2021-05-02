import os, pathlib, time, pyicloud, base64, hashlib, webbrowser, pip
from Crypto.Cipher import AES
from Crypto import Random
from pathlib import Path
from datetime import datetime
import os.path
from os import system, name, path
from pkg_resources import WorkingSet , DistributionNotFound
import sys as s
import defines
from defines import *
from pyicloud import PyiCloudService
from pyicloud.exceptions import *


#find downloads folder
if os.name == 'nt':
    downloads_path = str(Path.home() / "Downloads")
else:
    downloads_path = str(os.path.join(Path.home(), "Downloads"))

#find core files
core_files = downloads_path + '/Apple-Device-Controller'
login_files = core_files + '/Sensitive_content'
eula_check = core_files +'/EULA'
log_files = core_files + '/Logs'

bbb = False

#Core files check
core_text = core_files + '/check.txt'
eula_text = eula_check + '/check.txt'
Log_text = log_files + '/check.txt'
login_text = login_files + '/check.txt'
#Eula check and core file check

loading(2)

try:
    try:
        a = open(core_text, 'x')
        a.writelines('TRUE')
        a.close
    except FileExistsError:
        a = open(core_text, 'r')
        b = a.readlines()
        for word in b:
            if word == 'TRUE':
                ac = 'Check successful'
            else:
                clear()
                print('Error please check github!')
                exit()
    print('ac')            
    time.sleep(1)
    clear()
    print(f'Check of {core_files} is done')
except:
    print('Error, Please check github page.')
    time.sleep(.1)
    print('If nothing found make a push request.')
    exit()
loading(1)
clear()

try:
    try:
        a = open(login_text, 'x')
        a.writelines('TRUE')
        a.close
    except FileExistsError:
        a = open(login_text, 'r')
        b = a.readlines()
        for word in b:
            if word == 'TRUE':
                ac = 'Check successful'
            else:
                clear()
                print('Error please check github!')
                exit()
    print('ac')            
    time.sleep(1)
    clear()
    print(f'Check of {login_files} is done')
except:
    print('Error, Please check github page.')
    time.sleep(.1)
    print('If nothing found make a push request.')
    exit()
loading(1)
clear()

try:
    try:
        a = open(eula_text, 'x')
        a.writelines('TRUE')
        a.close
    except FileExistsError:
        a = open(eula_text, 'r')
        b = a.readlines()
        for word in b:
            if word == 'TRUE':
                ac = 'Check successful'
            else:
                clear()
                print('Error please check github!')
                exit()
    print('ac')            
    time.sleep(1)
    clear()
    print(f'Check of {eula_check} is done')
except:
    print('Error, Please check github page.')
    time.sleep(.1)
    print('If nothing found make a push request.')
    exit()
loading(1)
clear()

try:
    try:
        a = open(Log_text, 'x')
        a.writelines('TRUE')
        a.close
    except FileExistsError:
        a = open(Log_text, 'r')
        b = a.readlines()
        for word in b:
            if word == 'TRUE':
                ac = 'Check successful'
            else:
                clear()
                print('Error please check github!')
                exit()
    print('ac')            
    time.sleep(1)
    clear()
    print(f'Check of {log_files} is done')
except:
    print('Error, Please check github page.')
    time.sleep(.1)
    print('If nothing found make a push request.')
    exit()
loading(1)
clear()

EULA_check()
f = open(login_files+'/email.txt', 'r')
b = f.readlines()
for word in b:
    if word == 'NA':
        print('You have never logged in before!')
        time.sleep(.5)
        print('Please login now')
        elogin = 'a'
    else:
        print('You have logged in before.')
        loading(2)
        clear()
        print('Logging in...')
        elogin = 'b'
f.close()

f = open(login_files+'/password.txt', 'r')
b = f.readlines()
for word in b:
    if word == 'NA':
        print('You have never logged in before!')
        time.sleep(.5)
        print('Please login now')
        plogin = 'a'
    else:
        print('You have logged in before.')
        loading(2)
        clear()
        print('Logging in...')
        plogin = 'b'
f.close()
while bbb == False:
    if elogin and plogin == 'a':
        print('Logging in now!')
        time.sleep(1)
        print('Your data is stored in the downloads folder ')
        time.sleep(1)
        print('This uses Icloud')
        email = input('Email: ')
        f = open(login_files+'/email.txt', 'w')
        f.writelines(email)
        f.close()
        password = input('Password: ')
        f = open(login_files+'/password.txt', 'w')
        f.writelines(password)
        f.close()
    elif elogin and plogin == 'b':
        print('Logging in now!')
        time.sleep(1)
        print('Your data has been stored in the downloads folder')
        f = open(login_files+'/email.txt', 'r')
        b = f.readline(1)
        emaillogin = b
        f.close()
        f = open(login_files+'/password.txt', 'r')
        b = f.readline(1)
        passwordlogin = b
        f.close()
        loading(1)
        clear()
        print('Loaded data from data files')
        time.sleep(1)

    encryption_check()
    if defines.ecrypt == True:
        print('This is currently disabled!')
    elif defines.ecrypt == False:
        try:
            api = PyiCloudService(emaillogin, passwordlogin)
            bbb = True
        except PyiCloudFailedLoginException:
            clear()
            print('Please Check your email and password!')
            time.sleep(1)
            print('And try again')



print('Welcome')




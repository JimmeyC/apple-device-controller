import os, pathlib, time, pyicloud, base64, hashlib, webbrowser, pip
from Crypto.Cipher import AES
from Crypto import Random
from pathlib import Path
from datetime import datetime
import os.path
from os import system, name, path
from pkg_resources import WorkingSet , DistributionNotFound
import sys as s

if os.name == 'nt':
    downloads_path = str(Path.home() / "Downloads")
else:
    downloads_path = str(os.path.join(Path.home(), "Downloads"))

core_files = downloads_path + '/Apple-Device-Controller'
login_files = core_files + '/Sensitive_content'
eula_check = core_files +'/EULA'
log_files = core_files + '/Logs'
Eula_text = eula_check + '/eula.txt'

ecrypt = ''
elogin = False
plogin = False

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def continu():
    l = input('Press enter to continue!')

def loading(times):
    for _ in range(times):
        time.sleep(.5)
        clear()
        print('Loading    |')
        time.sleep(.5)
        clear()
        print('Loading.   /')
        time.sleep(.5)
        clear()
        print('Loading..  -')
        time.sleep(.5)
        clear()
        print('Loading... \\')

def dir_check(path):
    a = Path.exists(path)
    if a == False:
        print(f'{path} does not exist')
        time.sleep(1)
        clear()
        print('Will continue to check the rest before stopping!')
        time.sleep(1)
        print('Please Run Setup to rebuild the folder/file!')
    elif a == True:
        clear()
        print(f'{path} has been found!')
        time.sleep(1)
        print('Continuing check')
    else:
        print('Error with checking path!')
        time.sleep(1)
        print('Please refer to the github page for more info!')
        exit()

def EULA_check():
    f = open(Eula_text)
    b = f.readlines()
    for word in b:
        if word == 'FALSE':
            print('You have not accepted the EULA!')
            time.sleep(1)
            print('Run Setup to accept the EULA then open the Apple Device controller.app again!')
            exit()
        elif word == 'TRUE':
            print('EULA has been checked and shown true!')
            time.sleep(1)
            clear()
            print('Returning to program!')
            loading(2)
            clear()
        else:
            clear()
            print('Error with checking EULA!')
            time.sleep(1)
            print('Check with github page!')
            exit()
    f.close()

def encryption_check():
    try:
        f = open(login_files + '/encryption.txt','r')
        b = f.readlines()
        for word in b:
            if word == 'DISABLED':
                clear()
                print('Encryption has been disabled.')
                time.sleep(.5)
                print('If you want to turn it back on please run Setup.')
                ecrypt = False
            elif word == 'ENABLED':
                clear()
                print('Encryption has been enabled but It will not work at the moment!')
                time.sleep(.5)
                print('Please disable it untill a new update comes out as you will get locked out!')
                ecrypt = True
        f.close()

    except FileNotFoundError:
        print('Encryption file does not exist!')
        time.sleep(1)
        print('Please run Setup to restore the encryption.txt file!')
        exit()
    
def check_not_login():
    f = open(login_files+'/email.txt', 'r')
    b = f.readlines()
    for word in b:
        if word == 'NA':
            print('You have never logged in before!')
            time.sleep(.5)
            print('Please login now')
            elogin = False
        else:
            print('You have logged in before.')
            loading(2)
            clear()
            print('Logging in...')
            elogin = True
    f.close()

    f = open(login_files+'/password.txt', 'r')
    b = f.readlines()
    for word in b:
        if word == 'NA':
            print('You have never logged in before!')
            time.sleep(.5)
            print('Please login now')
            plogin = False
        else:
            print('You have logged in before.')
            loading(2)
            clear()
            print('Logging in...')
            plogin = True
    f.close()

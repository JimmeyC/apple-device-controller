#######################################################################
# This Setup is to only be used if your in a IDLE                     #
#######################################################################

import os, pathlib, time, pyicloud, base64, hashlib, webbrowser, pip
from Crypto.Cipher import AES
from Crypto import Random
from pathlib import Path
from datetime import datetime
from os import system, name
from pkg_resources import WorkingSet , DistributionNotFound
import sys as s
import defines
from defines import *
l = ''

if os.name == 'nt':
    downloads_path = str(Path.home() / "Downloads")
else:
    downloads_path = str(os.path.join(Path.home(), "Downloads"))

pdir = downloads_path
directory = 'Apple-Device-Controller'
verfication_folder = os.path.join(pdir,directory)
creation_of_main = os.path.join(pdir,directory)
working_set = WorkingSet()


try:
    print('Creating Core folder!')
    time.sleep(.2)
    os.mkdir(creation_of_main)
    print(f'Folder created at {creation_of_main}')
except FileExistsError:
    print('Setup directory already exists.')
    time.sleep(.1)
    print('Continuing on with setup')

time.sleep(1)

core_fl = creation_of_main
lAl = os.path.join(core_fl, "Logs")
try:
    print(f'Creating {lAl} folders and files!')
    time.sleep(.2)
    os.mkdir(lAl)
except FileExistsError:
    print(f'{lAl} already exists!')

time.sleep(1)

#Log
Pathl = lAl + '/setup_log.txt'
try:
    time.sleep(.2)
    f = open(Pathl, "x")
    exact_t = datetime.now()
    f.write(f'[{exact_t}] {Pathl} has been created! \n')
    f.close()
except FileExistsError:
    f = open(Pathl, "w")
    exact_t = datetime.now()
    f.write(f'[{exact_t}] {Pathl} Already Exists! \n')
    f.close()
    print(f'{Pathl} already exists!')

time.sleep(1)

core_fl = creation_of_main
lAl = os.path.join(core_fl, "EULA")
try:
    print(f'Creating {lAl} folders and files!')
    time.sleep(.2)
    os.mkdir(lAl)
    f = open(Pathl, "x")
    exact_t = datetime.now()
    f.write(f'[{exact_t}] {lAl} has been created! \n')
    f.close()
except FileExistsError:
    f = open(Pathl, "w")
    exact_t = datetime.now()
    f.write(f'[{exact_t}] {lAl} Already Exists! \n')
    f.close()
    print(f'{lAl} already exists!')

time.sleep(1)

elsei = lAl + '/eula.txt'
try:
    time.sleep(.2)
    a = open(elsei, "x")
    a.write("FALSE")
    a.close()
    f = open(Pathl, "w")
    exact_t = datetime.now()
    f.write(f'[{exact_t}] {elsei} has been created! \n')
    f.close()
except FileExistsError:
    f = open(Pathl, "w")
    exact_t = datetime.now()
    f.write(f'[{exact_t}] {elsei} Already Exists! \n')
    f.close()
    print(f'{elsei} already exists!')

time.sleep(1)

core_fl = creation_of_main
lAl = os.path.join(core_fl, "Sensitive_content")
try:
    print(f'Creating {lAl} folders and files!')
    time.sleep(.2)
    os.mkdir(lAl)
    f = open(Pathl, "x")
    exact_t = datetime.now()
    f.write(f'[{exact_t}] {lAl} has been created! \n')
    f.close()
except FileExistsError:
    f = open(Pathl, "w")
    exact_t = datetime.now()
    f.write(f'[{exact_t}] {lAl} Already Exists! \n')
    f.close()
    print(f'{lAl} already exists!')

time.sleep(1)

elsei = lAl + '/password.txt'
try:
    time.sleep(.2)
    a = open(elsei, "x")
    a.writelines('NA')
    a.close()
    f = open(Pathl, "w")
    exact_t = datetime.now()
    f.write(f'[{exact_t}] {elsei} has been created! \n')
    f.close()
except FileExistsError:
    f = open(Pathl, "w")
    exact_t = datetime.now()
    f.write(f'[{exact_t}] {elsei} Already Exists! \n')
    f.close()
    print(f'{elsei} already exists!')

time.sleep(1)

elsei = lAl + '/email.txt'
try:
    time.sleep(.2)
    a = open(elsei, "x")
    a.writelines('NA')
    a.close()
    f = open(Pathl, "w")
    exact_t = datetime.now()
    f.write(f'[{exact_t}] {elsei} has been created! \n')
    f.close()
except FileExistsError:
    f = open(Pathl, "w")
    exact_t = datetime.now()
    f.write(f'[{exact_t}] {elsei} Already Exists! \n')
    f.close()
    print(f'{elsei} already exists!')

time.sleep(1)
encryptt = True
while encryptt == True:
    clear()
    print('Would you like to enable encryption (Recomended)')
    encrypt = input('Y/N ')
    if encrypt.upper() == 'Y':
        elsei = lAl + '/encryption.txt'
        try:
            time.sleep(.2)
            a = open(elsei, "x")
            a.write('ENABLED')
            a.close()
            f = open(Pathl, "w")
            exact_t = datetime.now()
            f.write(f'[{exact_t}] {elsei} has been created! \n')
            f.close()
            encryptt = False
        except FileExistsError:
            f = open(Pathl, "w")
            exact_t = datetime.now()
            f.write(f'[{exact_t}] {elsei} Already Exists! \n')
            f.close()
            print(f'{elsei} already exists!')
            encryptt = False
    elif encrypt.upper() == 'N':
        elsei = lAl + '/encryption.txt'
        try:
            time.sleep(.2)
            a = open(elsei, "x")
            a.write('DISABLED')
            a.close()
            f = open(Pathl, "w")
            exact_t = datetime.now()
            f.write(f'[{exact_t}] {elsei} has been created! \n')
            f.close()
            encryptt = False
        except FileExistsError:
            f = open(Pathl, "w")
            exact_t = datetime.now()
            f.write(f'[{exact_t}] {elsei} Already Exists! \n')
            f.close()
            print(f'{elsei} already exists!')
            encryptt = False
    else:
        clear()
        time.sleep(1)
        print('Select a valid option')
        
        loading(3)

time.sleep(1)
clear()
eula = os.path.join(core_fl, "EULA")
eula = eula + "/eula.txt"
a = open(eula,'r')
b = a.readlines()
for Fa in b:
    if Fa == 'FALSE':
        bb = True
        webbrowser.open_new_tab(url="https://github.com/poggers1337/POGGERS-LICENSE-AGREEMENT")
        while bb == True:
            clear() 
            print('Do you accept the licence agreement and EULA!')
            eula_accept = input('READ/YES/NO ')
            if eula_accept.upper() == 'YES':
                loading(2)
                time.sleep(1)
                clear()
                print('EULA ACCEPTED')
                time.sleep(1)
                clear()
                a.close()
                a = open(eula, "w")
                a.write('TRUE')
                a.close()
                print('RETURNING TO SETUP')
                bb = False
            elif eula_accept.upper() == 'NO':
                time.sleep(1)
                clear()
                print('EXITTING SETUP')
                exit()
            elif eula_accept.upper() == 'READ':
                webbrowser.open_new_tab(url="")

loading(2)
clear()
print('Are you running this script on python IDLE/terminal?')
ru_python = input('Y/N ')
ru_pythonn = True
while ru_pythonn == True:
    if ru_python.upper() == 'Y':
        print('Installing packages...')
        time.sleep(1)
        loading(2)
        clear()
        print('###########################################################################')
        print('# All Packages that are installed are shown below this                    #')
        print('###########################################################################')
        print (s.modules.keys())
        print('###########################################################################')
        print('# All Packages that are installed are shown above this                    #')
        print('###########################################################################')
        continu()
        ru_pythonn = False
        try:
            dep = working_set.require('pyicloud')
        except DistributionNotFound:
            from setuptools.command.easy_install import main as install
            install(['pyicloud'])
            pass
        time.sleep(1)
        clear()
        print('RETURNING TO SETUP')
        time.sleep(1)
    elif ru_pythonn.upper() == 'N':
        clear()
        print('Returning to setup!')
        time.sleep(1)
        ru_pythonn = False
    else:
        clear()
        print('Choose a valid option')
        time.sleep(1)

loading(1)
clear()

time.sleep(1)
print('Setup completed!')
time.sleep(1)
for _ in range(4):
    time.sleep(1)

    print('#################################################')
    print('# DO NOT RUN AGAIN UNLESS YOU DELETE CORE FILES #')
    print('#################################################')
    time.sleep(1)
    clear()
print('#################################################')
print('# DO NOT RUN AGAIN UNLESS YOU DELETE CORE FILES #')
print('#################################################')
exit()
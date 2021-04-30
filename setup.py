#######################################################################
# This code is intended for macosx users, It will not work on windows #
#######################################################################

import os, pathlib, time
from pathlib import Path
from datetime import datetime
from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

if os.name == 'nt':
    downloads_path = str(Path.home() / "Downloads")
else:
    downloads_path = str(os.path.join(Path.home(), "Downloads"))

pdir = downloads_path
directory = 'Apple-Device-Controller'
verfication_folder = os.path.join(pdir,directory)
creation_of_main = os.path.join(pdir,directory)

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
    print(f'{Pathl} already exists!')

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
    print(f'{Pathl} already exists!')

time.sleep(1)

elsei = lAl + '/email.txt'
try:
    time.sleep(.2)
    a = open(elsei, "x")
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
    print(f'{Pathl} already exists!')

time.sleep(1)




import yaml
import AutoRouter.Commands as Commands
import keyboard
from AutoRouter.Exceptions import *
import os
from time import sleep



req_keys = ['host', 'username', 'kind']

def readYml(file_name):
    try:
        file = open(file_name, 'r')
        Commands.data = yaml.safe_load(file)
        file.close()
        return checkYml(file_name)
    except Exception:
        FileError(file_name)
    return 0


def checkYml(file_name):
    for i in req_keys:
        if i not in Commands.data.keys():
            YmlMissingCamp(file_name, i)
            return 1
    if 'port' not in Commands.data.keys():
        Commands.data['port'] = 22
    if 'password' not in Commands.data.keys():
        Commands.data['password'] = ''
    return 0


def position_up():
    print('Hola\n\n')



def selectFile():
    position = 0
    path = 'YML_Files'
    max_len = 20
    files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
    print('\033[1mSelect File:\033[0m\n')
    for file in files:
        if len(file) > max_len:
            max_len = len(file)
        print(file)
    print(f'\033[{len(files)}A\033[46m{files[position]}'+' '*(max_len-len(files[position]))+'\033[0m', end='')
    print()
    keyboard.on_press_key("up arrow", lambda: print('Hola'))
    while True:
        continue



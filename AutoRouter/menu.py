import keyboard
import time
import os


path = 'YML_Files'
max_len = 40


def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def position_up(files, position):
    if position == 0:
        return 0
    else:
        print(f'{files.index(files[position])+1}. {files[position]}'+' '*(max_len-len(files[position])))
        position -= 1
        print(f'\033[2A\033[47m{files.index(files[position])+1}. {files[position]}'+' '*(max_len-len(files[position]))+'\033[0m\033[1A')
        return position
    

def position_down(files, position):
    if position == len(files) - 1:
        return position
    else:
        print(f'{files.index(files[position])+1}. {files[position]}'+' '*(max_len-len(files[position])))
        position += 1
        print(f'\033[47m{files.index(files[position])+1}. {files[position]}'+' '*(max_len-len(files[position]))+'\033[0m\033[1A')
        return position
    

def selectFile():
    global max_len
    position = 0
    files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
    print('\033[1mSelect File:\033[0m\n')
    for file in files:
        if len(file) > max_len:
            max_len = len(file)
        print(f'{files.index(file)+1}. {file}')
    print(f'\033[{len(files)}A\033[47m{files.index(files[position])+1}. {files[position]}'+' '*(max_len-len(files[position]))+'\033[0m\033[1A')
    while True:
        if keyboard.is_pressed('down'):
            position = position_down(files, position)
        elif keyboard.is_pressed('up'):
            position = position_up(files, position)
        elif keyboard.is_pressed('enter'):
            break
        time.sleep(0.15)
    clear()
    return os.path.abspath(os.path.join(path, files[position]))

import yaml
import AutoRouter.Commands as Commands
from AutoRouter.Exceptions import *
import os


key_pressed = ''
req_keys = ['host', 'username', 'kind']

def readYml(file_path):
    try:
        file = open(file_path, 'r')
        Commands.data = yaml.safe_load(file)
        file.close()
        if os.stat(file_path).st_size == 0:
            raise EmptyFileException
        return checkYml(file_path)
    except EmptyFileException:
        EmptyFileError(os.path.basename(file_path))
    except Exception:
        FileError(os.path.basename(file_path))
    return 1


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

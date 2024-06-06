import yaml
import Commands
from Exceptions import *


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

INFO = '\033[1:32mINFO: \033[0m'

def ConnectionSuccessful(host):
    print(INFO+f'SHH Connection with {host} successful.')


def SSHDisconection():
    print(INFO+f'SHH Connection closed successfully.')


def CommandExecution(command):
    print(INFO+f'The command [{command}] has been executed successfully')

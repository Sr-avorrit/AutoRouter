import AutoRouter.Commands as Commands
import paramiko
from AutoRouter.Exceptions import *
from AutoRouter.Information import *

def getConnectionData():
    connectionInfo = {}
    hosts = list(Commands.data['host'])
    for host in hosts:
        connectionInfo[host] = {}
    for param in ['port', 'username', 'password', 'kind']:
        tmp = Commands.data[param]
        if type(tmp) != type([]):
            aux = tmp
            tmp = [aux]
        if len(tmp) == 1:
            for host in hosts:
                connectionInfo[host][param] = tmp[0]
        elif len(tmp) == len(hosts):
            for i in range(len(hosts)):
                connectionInfo[hosts[i]][param] = tmp[i]
        else:
            ParameterMismatch(param, len(hosts), len(tmp))
            return 1
    return connectionInfo


def connect(host, data):
    try:
        connection = paramiko.SSHClient()
        connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        router = data.copy()
        router['hostname'] = host
        router.pop('kind')
        connection.connect(**router)
        ConnectionSuccessful(host)
        return connection
    except Exception:
        SSHConnectionError(host, data['port'])


def executeCommand(connection, command):
    stdin, stdout, stderr = connection.exec_command(command)
    CommandExecution(command)


def disconnect(connection):
    connection.close()
    SSHDisconection()

import AutoRouter.files as files
import AutoRouter.connector as connector
import AutoRouter.Commands as Commands
from AutoRouter.menu import selectFile


def start():
    print('\033[1:34mWelcome to AutoRouter v0.0pa1\033[0m\n')
    file = selectFile()
    if files.readYml(file) == 0:
        connections = connector.getConnectionData()
        if connections != 1:
            for connection in connections:
                router = connector.connect(connection, connections[connection])
                for i in Commands.data:
                    if i not in ['host', 'port', 'username', 'password', 'kind']:
                        if type(Commands.data[i]) != type({}):
                            command = Commands.getCommand(connections[connection]['kind'], i)
                            if command != 1:
                                connector.executeCommand(router, command)
                connector.disconnect(router)

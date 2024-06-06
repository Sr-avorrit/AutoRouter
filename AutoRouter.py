import files, connector, Commands


def start():
    print('\033[1:34mWelcome to AutoRouter v0.0a1\033[0m\n')
    if files.readYml('R1.yml') == 0:
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

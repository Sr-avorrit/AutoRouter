ERROR = '\033[1:31mERROR: \033[0m'
WARNING = '\033[1:33mWARNING: \033[0m'


class EmptyFileException(Exception):
    pass


def FileError(file_name):
    print(ERROR+f'Something went wrong wile trying to open the file {file_name}.')


def YmlMissingCamp(file_name, camp):
    print(ERROR+f'At lest a {camp} is missing in the file {file_name}')


def ParameterMismatch(param, expected, got):
    print(ERROR+f'Length mismatch at {param} expected {expected} occurrences and got {got}')


def SSHConnectionError(host, port):
    print(ERROR+f'Unable to connect to {host}  using port {port}')


def UnexpectedAttribute():
    print(WARNING+f'Unexpected parameter recited, no actions taken.')


def NotProgramed():
    print(WARNING + f'The command you are trying to execute is not available in this version of AutoRouter.')


def EmptyFileError(file_name):
    print(ERROR+f'The file {file_name} is empty.')

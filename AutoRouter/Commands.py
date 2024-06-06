import Exceptions

data = {}
commands = {
    'hostname': 'kind+"Hostname()"',
    'domain-lookup': 'kind+"DomainLookup()"',
}


def getCommand(kind, command):
    return eval(eval(commands[command]))


######################
#   CISCO Commands   #
######################
def ciscoHostname():
    return f'hostname {data["hostname"]}'


def ciscoDomainLookup():
    if str(data['domain-lookup']).lower() in ['no', 'false']:
        return 'no ip domain-lookup'
    elif str(data['domain-lookup']).lower() in ['yes', 'true', 'si']:
        return 'ip domain-lookup'
    else:
        Exceptions.UnexpectedAttribute()
        return 1


#######################
#  MikroTik Commands  #
#######################
def mktHostname():
    return f'/system identity set name={data["hostname"]}'


def mktDomainLookup():
    Exceptions.NotProgramed()
    return 1

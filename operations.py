import config
import sshrunner


def is_argument_missing(value: str, message: str) -> bool:
    if not value:
        print('{} is missing!'.format(message))
        return True
    
    return False


def add_new_host(alias: str, host: str, key_path: str, login: str):
    if is_argument_missing(alias, 'alias'):
        return

    if is_argument_missing(host, 'host'):
        return
    
    if is_argument_missing(login, 'login'):
        return
    
    config.create()
    conf = config.load()

    conf[alias] = {'host': host, 'key_path': key_path, 'login': login}
    print('Added new config for {}'.format(alias))
    print(conf[alias])

    config.save(conf)


def list_saved_hosts():
    config.create()
    conf = config.load()

    aliases = [alias for alias in conf]
    aliases.sort()
    for alias in aliases:
        print(alias)


def show(alias: str):
    config.create()
    conf = config.load()

    if not conf[alias]:
        print('{} hasn\'t been found'.format(alias))
        return
    
    print(conf[alias])


def run_ssh(alias: str):
    config.create()
    conf = config.load()

    if not conf[alias]:
        print('{} hasn\'t been found'.format(alias))
        return
    
    sshrunner.run(conf[alias])

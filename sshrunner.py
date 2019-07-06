import subprocess


def run(conf: dict):
    command = ['ssh']

    if conf['key_path']:
        command.extend(['-i', conf['key_path']])
    
    command.append('{}@{}'.format(conf['login'], conf['host']))
    print('pyremote: {}'.format(' '.join(command)), flush=True)

    subprocess.run(command)

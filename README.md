# pyremote

# Requirements
* Python 3

# Installation
1. Add folder with pyremote.py to the PATH or create symlink ```ln -s _path_/pyremote.py pyremote```
2. To enable autocompletion add to ```~/.bashrc``` command ```source _path_/pyremote-completion.bash```

# Usage
Configuration is stored in ```~/.pyremote/config.yaml```


To change configuration for specified alias just run ```-add``` command again with the same alias.

```bash
$ pyremote -add --host-alias test --host test.dc0 --key-path /c/repo/pub_key --login urazoth
Added new config for test
{'host': 'test.dc0', 'key_path': 'C:/repo/pub_key', 'login': 'urazoth'}

$ pyremote -list
test

$ pyremote -show test
{'host': 'test.dc0', 'key_path': 'C:/repo/pub_key', 'login': 'urazoth'}

$ pyremote test
pyremote: ssh -i C:/repo/pub_key urazoth@test.dc0
Enter passphrase for key 'C:/repo/pub_key':
Last login: Sat Jul  6 18:20:09 2019 from 10.122.185.137
[urazoth@test.dc0 ~]$
```
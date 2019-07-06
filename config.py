import os
import yaml

CONFIG_DIR = os.path.sep.join([os.getenv('HOME'), '.pyremote'])
CONFIG_FILE = os.path.sep + 'config.yaml'
CONFIG_FULL_PATH = CONFIG_DIR + CONFIG_FILE


def create():
    if os.path.exists(CONFIG_DIR + CONFIG_FILE):
        return

    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR)

    with open(CONFIG_FULL_PATH, 'w') as f:
        yaml.dump({'config':''}, f)


def load():
    conf = None

    with open(CONFIG_FULL_PATH, 'r') as f:
        conf = yaml.safe_load(f)
    
    if conf is None:
        conf = {}
    
    return conf


def save(config):
    with open(CONFIG_FULL_PATH, 'w') as f:
        yaml.dump(config, f, default_flow_style=False)

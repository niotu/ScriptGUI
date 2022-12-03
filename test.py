from const.CONSTANTS import *

for name in NAMES_TO_SCRIPTS.values():
    name = name.replace('\n', '')
    with open(f'logs/{name}_logs.log', 'w') as fh:
        fh.write('')
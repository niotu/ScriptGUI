from const.CONSTANTS import *


for name in NAMES_TO_SCRIPTS.values():
    script = (f"from const.CONSTANTS import *\n\nwith open(OUTPUT_DIR + \'{name}\' + '.txt', 'w') as f:\n\tf.write(\'{name}\')")
    with open('scripts' + '\\' + name + '.py', 'w') as f:
        f.write(script)

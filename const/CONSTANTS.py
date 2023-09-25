import io

from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal

SCRIPT_NAMES = \
    [
        'агата', 'арго', 'эталина',
        'фиорита', 'гинда', 'жанели',
        'джети', 'куртки', 'лкрафт',
        'сумки\nстиль', 'босса\nнова',
        "синий\nлен", 'клевер\nмедиа', 'раш',
        "ЭЙС", "Фанси\nмода"
    ]

COMMON_STYLE = (
    """
    QPushButton{
        position: absolute;
        width: 168px;
        height: 168px;
        top: 75px;
        
        border-radius: 15px;
        font-family: 'Inter';
        font-style: normal;
        font-weight: 400;
        font-size: 20px
    }
    QPushButton[state='common']{
        background: rgba(195, 253, 31, 1.0);
    }
    
    QPushButton:hover{
        background: rgba(195, 253, 31, 0.7)
    }
    QPushButton:pressed{
        border: 3px solid #373E43;
    }         
    QPushButton[state='loading']{
        background: #EAC713;
    }
    QPushButton[state='error']{
        background: #FF440A;
    }
    """)

ALL_START_STYLE = ('''
QPushButton
{
    position: absolute;
    width: 168px;
    height: 168px;
    top: 75px;
    
    background: #1387F1;
    border-radius: 15px;
    font-family: 'Inter';
    font-style: normal;
    font-weight: 400;
    font-size: 20px;
}
 
QPushButton:hover
{
    background: #0E5597;
}
QPushButton:pressed{
    border: 3px solid #373E43;
}         
''')

NAMES_TO_SCRIPTS = \
    {
        'агата': 'agata', 'арго': 'argo', 'эталина': 'etalina',
        'фиорита': 'fiorita', 'гинда': 'guinda', 'жанели': 'janelli',
        'джети': 'jetty', 'куртки': 'kurtki', 'лкрафт': 'lcraft',
        'сумкистиль': 'sumki-style', 'боссанова': 'triko',
        "синийлен": '/home/vint/workspace/siniylen.ru/siniylen.py',
        'клевермедиа': '/home/vint/workspace/clever-media/clever-media.py',
        'раш': '/home/vint/workspace/rash.su/rashParser.py',
        'эйс': '/home/vint/workspace2/ScriptGUI/difficult/do_ace.sh',
        'фансимода': '/home/vint/workspace2/ScriptGUI/difficult/fancy.sh'
    }

SPECIAL = {'агата': 'agata', 'арго': 'argo', 'эталина': 'etalina',
           'фиорита': 'fiorita', 'гинда': 'guinda', 'жанели': 'janelli',
           'джети': 'jetty', 'куртки': 'kurtki', 'лкрафт': 'lcraft',
           'сумкистиль': 'sumki-style', 'боссанова': 'triko',
           "синийлен": 'siniylen',
           'клевермедиа': 'clever-media',
           'раш': 'rash', 'эйс': 'ace', 'фансимода': 'fancymoda'}

OUTPUT_DIR = 'output/'

MENU_STYLE = (
    'QMenu{'
    'position: absolute;'
    'width: 168px;'
    'height: 70px;'

    'background: #DAF296;'

    'border-radius: 15px;'
    # 'border: 3px solid #000000;'
    'font-family: "Inter";'
    'font-style: normal;'
    'font-weight: 400;'
    'font-size: 14px;'
    '}'
    'QMenu::item{'
    'padding-left: 25px;'

    'width: 140px;'
    'height: 30px;'

    'border: 2px solid #000000;'
    'border-radius: 15px;'
    'background: #C3FD1F;'
    '}'
    'QMenu::item:hover{'
    'background: #86B405;'
    '}'
)


class Logger:
    def __init__(self):
        pass

    def write(self, name, info):
        mode = 'ab'
        if name == 'errors_QT':
            mode = 'a'
            info += '\n'
        filepath = f'logs/{name}_logs.log'
        with open(filepath, mode) as f:
            f.write(info)

    def read(self, name):
        filepath = f'logs/{name}_logs.log'
        with open(filepath, 'r') as f:
            try:
                lines = f.readlines()
            except io.UnsupportedOperation:
                lines = f.readlines()
        return lines


logger = Logger()

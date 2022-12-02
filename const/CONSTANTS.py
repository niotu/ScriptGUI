import logging

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtGui

SCRIPT_NAMES = \
    [
        'агата', 'арго', 'эталина',
        'фиорита', 'гинда', 'жанели',
        'джети', 'куртки', 'лкрафт',
        'сумки\nстиль', 'босса\nнова',
        "синий\nлен", 'клевер\nмедиа', 'раш'
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
        'фиорита': 'fiorita', 'гинда': 'guinda', 'жанели': 'janeli',
        'джети': 'jetty', 'куртки': 'kurtki', 'лкрафт': 'lcraft',
        'сумкистиль': 'sumkistyle', 'боссанова': 'bossanova',
        "синийлен": 'siniylen', 'клевермедиа': 'clevermedia', 'раш': 'rash'
    }

OUTPUT_DIR = 'C:\\Users\\noitu\\work\\PycharmProjects\\ScriptGUI\\output\\'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename="logs/logs.log")
logger = logging.getLogger(__name__)

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

class Pic(QtWidgets.QLabel):
    click = pyqtSignal()

    def __init__(self, parent):
        super().__init__(parent)

    def mousePressEvent(self, ev: QtGui.QMouseEvent) -> None:
        super().mousePressEvent(ev)
        self.click.emit()

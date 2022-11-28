PREFIX = 'C:/Users/noitu/work/PycharmProjects/Parser/'

SCRIPT_NAMES = \
    [
        'агата', 'арго', 'эталина',
        'фиорита', 'гинда', 'жанели',
        'джети', 'куртки', 'лкрафт',
        'сумкистиль', 'боссанова',
        "синий лен", 'клевер-\nмедиа', 'раш'
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
        "синий лен": 'siniylen', 'клевер-\nмедиа': 'clevermedia', 'раш': 'rash'
    }

SCRIPT_NAMES = ['агата', 'арго', 'эталина',
                'фиорита', 'гинда', 'жанели',
                'джети', 'куртки', 'лкрафт',
                'сумкистиль', 'боссанова',
                "синий лен", 'клевер-\nмедиа', 'раш']

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
    background: #C3FD1F;
}

QPushButton:hover{
    opacity: 0.8;
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



ERROR_STYLE = ''

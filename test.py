from PyQt5.QtCore import QProcess

pth = "python C:/Users/ni0tu/work/PycharmProjects/Parser/xlsxParser/allabuena.py C:/Users/ni0tu/work/PycharmProjects/Parser/xlsxParser/inp_files/inp.xlsx"

process = QProcess()
process.start(pth)
process.waitForFinished()
print(process.errorString())

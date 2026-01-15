import sys 
from PySide6.Qtwidgets import QApplication ,QWidget


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        


app = QApplication(sys.argv)
QWidget().show()
app.exec()
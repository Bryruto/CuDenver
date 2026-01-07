from PyQt6 import QtWidgets
from PyQt6.QtCore import QTimer, QTime, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()
        self.setGeometry(200,200,300,300)
        self.setWindowTitle("name")
    
    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("clock")
        self.label.move(50,50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Start")
        self.b1.clicked.connect(self.start)

        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("Stop")
        self.b2.clicked.connect(self.stop)
        self.b2.move(100, 0)

    def stop(self):
        self.label.setText(QTime.currentTime().toString("HH:mm:ss"))

    def start(self):
        self.label.setText(QTime.currentTime().toString("HH:mm:ss"))





def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec())

def main():
    window()

main()
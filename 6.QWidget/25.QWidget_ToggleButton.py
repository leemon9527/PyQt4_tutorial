# -*- coding: utf-8 -*-
__author__ = 'leemon'

import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        self.col = QtGui.QColor(0,0,0)

        redbtn = QtGui.QPushButton('Red',self)
        redbtn.setCheckable(True)
        redbtn.move(10,10)
        redbtn.clicked[bool].connect(self.setColor)

        greenbtn = QtGui.QPushButton('Green',self)
        greenbtn.setCheckable(True)
        greenbtn.move(10,60)
        greenbtn.clicked[bool].connect(self.setColor)

        bluebtn = QtGui.QPushButton('Bkue',self)
        bluebtn.setCheckable(True)
        bluebtn.move(10,110)
        bluebtn.clicked[bool].connect(self.setColor)

        self.square = QtGui.QFrame(self)
        self.square.setGeometry(150,20,100,100)
        self.square.setStyleSheet("QWidget { background-color: %s}" % self.col.name())

        self.setGeometry(300, 300, 800, 600)
        self.setWindowIcon(QtGui.QIcon('..\\img\\tool.ico'))
        self.setWindowTitle('Toggle Button')
        self.show()
    def setColor(self,pressed):
        source = self.sender()

        if pressed:
            val = 255
        else: val = 0

        if source.text() == "Red":
            self.col.setRed(val)
        elif source.text() == "Green":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)

        self.square.setStyleSheet("QWidget { background-color: %s}" % self.col.name())



def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
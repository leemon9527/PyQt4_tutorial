# -*- coding: utf-8 -*-
__author__ = 'leemon'

import  sys
from PyQt4 import QtGui,QtCore

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        qbtn = QtGui.QPushButton('Quit',self)
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(150,150)

        self.setGeometry(300,300,800,600)
        self.setWindowTitle('QuitButton')
        self.show()
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
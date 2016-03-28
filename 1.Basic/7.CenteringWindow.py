# -*- coding: utf-8 -*-
__author__ = 'leemon'

import sys
from PyQt4 import QtGui,QtCore

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        #self.resize(250,160)
        #self.center()
        # create a button to Center the windows by clicked it
        cbtn = QtGui.QPushButton('CenterWindow',self)
        cbtn.clicked.connect(self.center)
        cbtn.resize(cbtn.sizeHint())
        cbtn.move(150,150)

        self.setGeometry(100,100,800,600)
        self.setWindowTitle('Centering Window')
        self.show()
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
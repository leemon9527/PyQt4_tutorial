# -*- coding: utf-8 -*-
__author__ = 'leemon'
import sys
from PyQt4 import QtGui


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        lbl1 = QtGui.QLabel('Leemon',self)
        lbl1.move(15,10)

        lbl2 = QtGui.QLabel('Yaqin',self)
        lbl2.move(35,40)

        lbl3 = QtGui.QLabel('Ourhome',self)
        lbl3.move(55,70)

        self.setGeometry(300,300,800,600)
        self.setWindowIcon(QtGui.QIcon('tool.ico'))
        self.setWindowTitle('AbsPosition')
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
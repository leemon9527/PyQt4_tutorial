# -*- coding: utf-8 -*-
__author__ = 'leemon'

import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        self.lb1 = QtGui.QLabel(self)
        qle = QtGui.QLineEdit(self)

        qle.move(60,100)
        self.lb1.move(60,40)

        qle.textChanged[str].connect(self.onChanged)


        self.setGeometry(300, 300, 800, 600)
        self.setWindowIcon(QtGui.QIcon('..\\img\\tool.ico'))
        self.setWindowTitle('QtGui.QLineEdit')
        self.show()

    def onChanged(self,text):
        self.lb1.setText(text)
        self.lb1.adjustSize()



def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
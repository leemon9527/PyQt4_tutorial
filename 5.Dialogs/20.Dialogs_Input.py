# -*- coding: utf-8 -*-
__author__ = 'leemon'
import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        self.btn = QtGui.QPushButton('Dialog',self)
        self.btn.move(20,20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QtGui.QLineEdit(self)
        self.le.move(130,20)
        self.le.setDisabled(True)


        self.setGeometry(300, 300, 800, 600)
        self.setWindowIcon(QtGui.QIcon('..\\img\\tool.ico'))
        self.setWindowTitle('Input Dialog')
        self.show()
    def showDialog(self):
        text,ok =QtGui.QInputDialog.getText(self,'Input Dialog','Enter your name')
        if ok:
            self.le.setText(str(text))


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
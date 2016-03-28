# -*- coding: utf-8 -*-
__author__ = 'leemon'

import sys
from PyQt4 import QtGui, QtCore

class Button(QtGui.QPushButton):
    def __init__(self,title,parent):
        super(Button,self).__init__(title,parent)
        self.setAcceptDrops(True)
        self.adjustSize()

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()
    def dropEvent(self, e):
        self.setText(e.mimeData().text())
        self.adjustSize()

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        edit = QtGui.QLineEdit('',self)
        edit.setDragEnabled(True)
        edit.move(30,65)

        button = Button('Button',self)
        button.move(190,65)



        self.setGeometry(300, 300, 800, 600)
        self.setWindowIcon(QtGui.QIcon('..\\img\\tool.ico'))
        self.setWindowTitle('Simple drag & drop')



def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
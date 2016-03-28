# -*- coding: utf-8 -*-
__author__ = 'leemon'
import sys
from PyQt4 import QtGui, QtCore

class Communicate(QtCore.QObject):
    closeApp = QtCore.pyqtSignal()

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        #self.lb1 = QtGui.QLabel('tEST',self)
        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        self.setGeometry(300, 300, 800, 600)
        self.setWindowIcon(QtGui.QIcon('tool.ico'))
        self.setWindowTitle('Emit Signal')
        self.show()
    def mousePressEvent(self, QMouseEvent):
        self.c.closeApp.emit()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
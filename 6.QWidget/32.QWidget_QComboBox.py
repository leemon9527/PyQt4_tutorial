# -*- coding: utf-8 -*-
__author__ = 'leemon'

import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        self.lb1 = QtGui.QLabel('Windows',self)

        combo = QtGui.QComboBox(self)
        combo.addItem("Ubuntu")
        combo.addItem("Windows")
        combo.addItem("CentOS")
        combo.addItem("Redhat")
        combo.addItem("Gentoo")

        combo.move(50,50)
        self.lb1.move(50,150)

        combo.activated[str].connect(self.onActivated)

        self.setGeometry(300, 300, 800, 600)
        self.setWindowIcon(QtGui.QIcon('..\\img\\tool.ico'))
        self.setWindowTitle('QtGui.QComboBox')
        self.show()
    def onActivated(self,text):
        self.lb1.setText(text)
        self.lb1.adjustSize()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
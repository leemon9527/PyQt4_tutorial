# -*- coding: utf-8 -*-
__author__ = 'leemon'
import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        vbox = QtGui.QVBoxLayout()

        btn = QtGui.QPushButton("Dialog",self)
        btn.setSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Fixed)
        btn.move(20,20)

        vbox.addWidget(btn)

        btn.clicked.connect(self.showDialog)

        self.lb1 = QtGui.QLabel("KnowLedge only matters",self)
        self.lb1.move(130,20)

        vbox.addWidget(self.lb1)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 800, 600)
        self.setWindowIcon(QtGui.QIcon('..\\img\\tool.ico'))
        self.setWindowTitle('Font Dialog')
        self.show()
    def showDialog(self):
        font,ok =QtGui.QFontDialog.getFont()
        if ok:
            self.lb1.setFont(font)

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
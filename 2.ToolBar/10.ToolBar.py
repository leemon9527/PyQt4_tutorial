# -*- coding: utf-8 -*-
__author__ = 'leemon'
import sys
from PyQt4 import QtGui


class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        exitAction = QtGui.QAction(QtGui.QIcon('exit64.ico'),'Exit',self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(QtGui.qApp.quit)

        self.toorbar = self.addToolBar('Exit')
        self.toorbar.addAction(exitAction)

        self.setGeometry(300,300,800,600)
        self.setWindowIcon(QtGui.QIcon('tool.ico'))
        self.setWindowTitle('ToolBar')
        self.show()
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
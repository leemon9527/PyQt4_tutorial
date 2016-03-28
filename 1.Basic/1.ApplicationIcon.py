# -*- coding: utf-8 -*-
__author__ = 'leemon'

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example,self).__init__()
        self.initUI()
    def initUI(self):

        self.setGeometry(300,300,800,600)
        self.setWindowTitle('Jscntech Deploy Tool')
        self.setWindowIcon(QtGui.QIcon('tool.ico'))

        self.show()

def main():

        app = QtGui.QApplication(sys.argv)
        ex = Example()
        sys.exit(app.exec_())
if __name__ == '__main__':
    main()
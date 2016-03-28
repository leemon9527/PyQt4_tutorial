# -*- coding: utf-8 -*-
__author__ = 'leemon'

import sys
from PyQt4 import QtGui

def main():
    app = QtGui.QApplication(sys.argv)

    w = QtGui.QWidget()
    w.resize(800,600)
    w.move(300,300)
    w.setWindowTitle("Jscntech Deploy Tool")
    w.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
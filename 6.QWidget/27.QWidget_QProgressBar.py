# -*- coding: utf-8 -*-
__author__ = 'leemon'
import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        self.pbar = QtGui.QProgressBar(self)
        self.pbar.setGeometry(30,40,200,25)

        self.btn = QtGui.QPushButton('Start',self)
        self.btn.move(40,80)
        self.btn.clicked.connect(self.doAction)

        self.timer = QtCore.QBasicTimer()
        self.step = 0


        self.setGeometry(300, 300, 800, 600)
        self.setWindowIcon(QtGui.QIcon('..\\img\\tool.ico'))
        self.setWindowTitle('QtGui.QProgressBar')
        self.show()
    def timerEvent(self,e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Restart')
            return
        self.step = self.step + 1
        self.pbar.setValue(self.step)
    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        elif self.btn.text() == 'Restart'and not self.timer.isActive():
            self.step = 0
            self.timer.start(100,self)
            self.btn.setText('Stop')
        else:
            self.timer.start(100,self)
            self.btn.setText('Stop')

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
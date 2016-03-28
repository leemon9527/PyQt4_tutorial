__author__ = 'leemon'
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        cal = QtGui.QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(20,20)
        cal.clicked[QtCore.QDate].connect(self.showDate)

        self.lb1 = QtGui.QLabel(self)
        date = cal.selectedDate()
        self.lb1.setText(date.toString())
        self.lb1.move(130,260)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowIcon(QtGui.QIcon('..\\img\\tool.ico'))
        self.setWindowTitle('Calendar')
        self.show()
    def showDate(self,date):
        self.lb1.setText(date.toString())


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
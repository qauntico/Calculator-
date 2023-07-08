from PyQt6.QtWidgets import QApplication, QMainWindow
from calculator import Ui_MainWindow
import sys
import re

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.totalvalues = ''
        self.currentvalues = ''
        self.pushButton_4.clicked.connect(self.one)
        self.pushButton_5.clicked.connect( self.two )
        self.pushButton_6.clicked.connect( self.three )
        self.pushButton_8.clicked.connect( self.four )
        self.pushButton_9.clicked.connect( self.five )
        self.pushButton_10.clicked.connect( self.six )
        self.pushButton_12.clicked.connect( self.seven )
        self.pushButton_13.clicked.connect( self.eight )
        self.pushButton_14.clicked.connect( self.nine )
        self.pushButton_17.clicked.connect( self.zero )
        self.pushButton_16.clicked.connect( self.decimal )
        self.pushButton_3.clicked.connect(self.add)
        self.pushButton_11.clicked.connect(self.subtract)
        self.pushButton_15.clicked.connect(self.multiply)
        self.pushButton_19.clicked.connect(self.division)
        self.pushButton_7.clicked.connect(self.clear)


    def one(self):
        if '+' in self.currentvalues or '÷' in self.currentvalues or '-' in self.currentvalues or '×' in self.currentvalues:
            self.currentvalues = ''
            if len(self.totalvalues) != 8:
                self.label.setText(self.totalvalues+'1')
                self.totalvalues += '1'
                self.currentvalues += '1'
            else:
                return
        else:
            if len(self.totalvalues) != 8:
                self.label.setText(self.totalvalues+'1')
                self.totalvalues += '1'
                self.currentvalues += '1'
            else:
                return
    def two(self):
        if '+' in self.currentvalues or '÷' in self.currentvalues or '-' in self.currentvalues or '×' in self.currentvalues:
            self.currentvalues = ''
            if len(self.totalvalues) != 8:
                self.label.setText(self.totalvalues+'2')
                self.totalvalues += '2'
            else:
                return
        else:
            if len(self.totalvalues) != 8:
                self.label.setText(self.totalvalues+'2')
                self.totalvalues += '2'
            else:
                return
    def three(self):
        if '+' in self.currentvalues or '÷' in self.currentvalues or '-' in self.currentvalues or '×' in self.currentvalues:
            self.currentvalues = ''
            if len(self.totalvalues) != 8:
                self.label.setText(self.totalvalues+'3')
                self.totalvalues += '3'
            else:
                return
        else:
            if len(self.totalvalues) != 8:
                self.label.setText(self.totalvalues+'3')
                self.totalvalues += '3'
            else:
                return
    def four(self):
        if '+' in self.currentvalues or '÷' in self.currentvalues or '-' in self.currentvalues or '×' in self.currentvalues:
            self.currentvalues = ''
            if len(self.totalvalues) != 8:
                self.label.setText(self.totalvalues+'4')
                self.totalvalues += '4'
            else:
                return
        else:
            if len( self.totalvalues ) != 8:
                self.label.setText( self.totalvalues + '4' )
                self.totalvalues += '4'
            else:
                return
    def five(self):
        if '+' in self.currentvalues or '÷' in self.currentvalues or '-' in self.currentvalues or '×' in self.currentvalues:
            self.currentvalues = ''
            if len(self.totalvalues) != 8:
                self.label.setText(self.totalvalues+'5')
                self.totalvalues += '5'
                self.currentvalues += '5'
            else:
                return
        else:
            if len( self.totalvalues ) != 8:
                self.label.setText( self.totalvalues + '5' )
                self.totalvalues += '5'
                self.currentvalues += '5'
            else:
                return
    def six(self):
        if '+' in self.currentvalues or '÷' in self.currentvalues or '-' in self.currentvalues or '×' in self.currentvalues:
            self.currentvalues = ''
            if len(self.totalvalues) != 8:
                self.label.setText(self.totalvalues+'6')
                self.totalvalues += '6'
                self.currentvalues += '6'
            else:
                return
        else:
            if len( self.totalvalues ) != 8:
                self.label.setText( self.totalvalues + '6' )
                self.totalvalues += '6'
                self.currentvalues += '6'
            else:
                return
    def seven(self):
        if '+' in self.currentvalues or '÷' in self.currentvalues or '-' in self.currentvalues or '×' in self.currentvalues:
            self.currentvalues = ''
            if len(self.totalvalues) != 8:
                self.label.setText(self.totalvalues+'7')
                self.totalvalues += '7'
                self.currentvalues += '7'
            else:
                return
        else:
            if len( self.totalvalues ) != 8:
                self.label.setText( self.totalvalues + '7' )
                self.totalvalues += '7'
                self.currentvalues += '7'
            else:
                return
    def eight(self):
        if '+' in self.currentvalues or '÷' in self.currentvalues or '-' in self.currentvalues or '×' in self.currentvalues:
            self.currentvalues = ''
            if len(self.totalvalues) != 8:
                self.label.setText(self.totalvalues+'8')
                self.totalvalues += '8'
                self.currentvalues += '8'
            else:
                return
        else:
            if len(self.totalvalues) != 8:
                self.label.setText(self.totalvalues+'8')
                self.totalvalues += '8'
                self.currentvalues += '8'
            else:
                return
    def nine(self):
        if '+' in self.currentvalues or '÷' in self.currentvalues or '-' in self.currentvalues or '×' in self.currentvalues:
            self.currentvalues = ''
            if len(self.totalvalues) != 8:
                self.label.setText(self.totalvalues+'9')
                self.totalvalues += '9'
                self.currentvalues += '9'
            else:
                return
        else:
            if len(self.totalvalues) != 8:
                self.label.setText(self.totalvalues+'9')
                self.totalvalues += '9'
                self.currentvalues += '9'
            else:
                return
    def zero(self):
        if '+' in self.currentvalues or '÷' in self.currentvalues or '-' in self.currentvalues or '×' in self.currentvalues:
            self.currentvalues = ''
            if len(self.totalvalues) != 8:
                self.label.setText(self.totalvalues+'0')
                self.totalvalues += '0'
                self.currentvalues += '0'
            else:
                return
        else:
            if len( self.totalvalues ) != 8:
                self.label.setText( self.totalvalues + '0' )
                self.totalvalues += '0'
                self.currentvalues += '0'
            else:
                return
    def decimal(self):
        if '.' in self.currentvalues:
             return
        else:
            self.label.setText(self.totalvalues+'.')
            self.totalvalues += '.'
            self.currentvalues += '.'
    def add(self):
        if '+' in self.currentvalues:
            return
        else:
            self.label.setText(self.totalvalues+'+')
            self.totalvalues += '+'
            self.currentvalues += '+'
    def multiply(self):
        if '×' in self.currentvalues:
            return
        else:
            self.label.setText(self.totalvalues+'×')
            self.totalvalues += '×'
            self.currentvalues += '×'
    def division(self):
        if '÷' in self.currentvalues:
            return
        else:
            self.label.setText(self.totalvalues+'÷')
            self.totalvalues += '÷'
            self.currentvalues += '÷'
    def subtract(self):
        if '-' in self.currentvalues:
            return
        else:
            self.label.setText(self.totalvalues+'-')
            self.totalvalues += '-'
            self.currentvalues += '-'
    def clear(self):
        self.totalvalues = ''
        self.currentvalues = ''
        self.label.setText('0')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())
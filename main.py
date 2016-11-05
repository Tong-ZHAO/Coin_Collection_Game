#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: tong
# date  : 04/11/2016

import sys
from PyQt4 import QtGui
from menu import Ui_MenuWindow
from my_window import MyWindow

"""
  The main function to start game. Please use the following command: 

  $python main.py

"""


if __name__ == "__main__":
    
    app = QtGui.QApplication(sys.argv)  # create an application 
    MainWindow = MyWindow()             
    ui = Ui_MenuWindow()
    ui.setupUi(MainWindow)              # set up UI
    MainWindow.show()                   # show Window
    MainWindow.raise_()
    sys.exit(app.exec_())
    

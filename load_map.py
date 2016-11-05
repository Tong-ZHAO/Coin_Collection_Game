# -*- coding: utf-8 -*-
#!/usr/bin/env python
# author: tong
# date  : 04/11/2016

from PyQt4 import QtCore, QtGui
from game_window import Ui_GameWindow
import os, sys
 
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_LoadMapWindow(object):

    """ 
    This UI class of load map window. You can choose to initialized a random map or load an existing map from a csv file 
    
    :function enableButton(self)              : After choosing whether to load a map from csv file, according button will be enabled
    :function findFile(self, LoadMapWindow)   : A widget to find files in PC
    :function startGame(self, LoadMapWindow)  : Initialize game state 
    :function gameInitial(self, LoadMapWindow): Show game window
    """

    def setupUi(self, LoadMapWindow):
        LoadMapWindow.setObjectName(_fromUtf8("LoadMapWindow"))
        LoadMapWindow.setEnabled(True)
        LoadMapWindow.resize(600, 400)
        self.centralwidget = QtGui.QWidget(LoadMapWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem = QtGui.QSpacerItem(20, 14, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(178, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.WelcomeTitle = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WelcomeTitle.sizePolicy().hasHeightForWidth())
        self.WelcomeTitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.WelcomeTitle.setFont(font)
        self.WelcomeTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.WelcomeTitle.setObjectName(_fromUtf8("WelcomeTitle"))
        self.verticalLayout.addWidget(self.WelcomeTitle)
        self.GameTitle = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.GameTitle.setFont(font)
        self.GameTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.GameTitle.setObjectName(_fromUtf8("GameTitle"))
        self.verticalLayout.addWidget(self.GameTitle)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem2 = QtGui.QSpacerItem(188, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem3 = QtGui.QSpacerItem(20, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_2.addWidget(self.line)
        spacerItem4 = QtGui.QSpacerItem(20, 14, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem5 = QtGui.QSpacerItem(13, 106, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(20, 5, 20, 5)
        self.gridLayout_2.setHorizontalSpacing(100)
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.chooseLabel = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chooseLabel.sizePolicy().hasHeightForWidth())
        self.chooseLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.chooseLabel.setFont(font)
        self.chooseLabel.setObjectName(_fromUtf8("chooseLabel"))
        self.gridLayout_2.addWidget(self.chooseLabel, 0, 0, 1, 1)
        self.csvFlag = QtGui.QComboBox(self.centralwidget)
        self.csvFlag.setObjectName(_fromUtf8("csvFlag"))
        self.csvFlag.addItem(_fromUtf8(""))
        self.csvFlag.setItemText(0, _fromUtf8(""))
        self.csvFlag.addItem(_fromUtf8(""))
        self.csvFlag.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.csvFlag, 0, 1, 1, 1)
        self.csvLabel = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.csvLabel.sizePolicy().hasHeightForWidth())
        self.csvLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.csvLabel.setFont(font)
        self.csvLabel.setObjectName(_fromUtf8("csvLabel"))
        self.gridLayout_2.addWidget(self.csvLabel, 1, 0, 1, 1)
        self.sizeInput = QtGui.QLineEdit(self.centralwidget)
        self.sizeInput.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizeInput.sizePolicy().hasHeightForWidth())
        self.sizeInput.setSizePolicy(sizePolicy)
        self.sizeInput.setObjectName(_fromUtf8("sizeInput"))
        intValidator = QtGui.QIntValidator(0,99)
        self.sizeInput.setValidator(intValidator)
        self.gridLayout_2.addWidget(self.sizeInput, 2, 1, 1, 1)
        self.sizeLabel = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizeLabel.sizePolicy().hasHeightForWidth())
        self.sizeLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.sizeLabel.setFont(font)
        self.sizeLabel.setObjectName(_fromUtf8("sizeLabel"))
        self.gridLayout_2.addWidget(self.sizeLabel, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.fileName = QtGui.QLineEdit(self.centralwidget)
        self.fileName.setEnabled(False)
        self.fileName.setObjectName(_fromUtf8("fileName"))
        self.horizontalLayout_4.addWidget(self.fileName)
        self.selectFile = QtGui.QToolButton(self.centralwidget)
        self.selectFile.setEnabled(False)
        self.selectFile.setObjectName(_fromUtf8("selectFile"))
        self.horizontalLayout_4.addWidget(self.selectFile)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        spacerItem6 = QtGui.QSpacerItem(13, 106, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem7 = QtGui.QSpacerItem(20, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem7)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem8 = QtGui.QSpacerItem(238, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.startButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy)
        self.startButton.setMinimumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.startButton.setFont(font)
        self.startButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.startButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.startButton.setAutoRepeatInterval(100)
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.horizontalLayout_3.addWidget(self.startButton)
        spacerItem9 = QtGui.QSpacerItem(238, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem10 = QtGui.QSpacerItem(20, 14, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem10)
        self.line.raise_()
        self.selectFile.raise_()
        self.fileName.raise_()
        LoadMapWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(LoadMapWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        LoadMapWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoadMapWindow)
        QtCore.QObject.connect(self.csvFlag, QtCore.SIGNAL(_fromUtf8("activated(int)")), lambda: self.enableButton())
        QtCore.QObject.connect(self.startButton, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda: self.startGame(LoadMapWindow))
        QtCore.QObject.connect(self.selectFile, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda: self.findFile(LoadMapWindow))
        QtCore.QMetaObject.connectSlotsByName(LoadMapWindow)

    def retranslateUi(self, LoadMapWindow):
        LoadMapWindow.setWindowTitle(_translate("LoadMapWindow", "Coin Collection Game", None))
        self.WelcomeTitle.setText(_translate("LoadMapWindow", "Welcome To", None))
        self.GameTitle.setText(_translate("LoadMapWindow", "Coin Collection Game", None))
        self.chooseLabel.setText(_translate("LoadMapWindow", "Load a map from .csv ?", None))
        self.csvFlag.setItemText(1, _translate("LoadMapWindow", "Yes", None))
        self.csvFlag.setItemText(2, _translate("LoadMapWindow", "No", None))
        self.csvLabel.setText(_translate("LoadMapWindow", "Choose a csv file", None))
        self.sizeLabel.setText(_translate("LoadMapWindow", "Choose a map size  ( A positive odd integer )", None))
        self.selectFile.setText(_translate("LoadMapWindow", "...", None))
        self.startButton.setText(_translate("LoadMapWindow", "Start", None))

    def enableButton(self):
        index = self.csvFlag.currentIndex()
        if index == 0:
            self.fileName.setEnabled(False)
            self.selectFile.setEnabled(False)
            self.sizeInput.setEnabled(False)
        elif index == 1:
            self.fileName.setEnabled(True)
            self.selectFile.setEnabled(True)
            self.sizeInput.setEnabled(False)
        else:
            self.fileName.setEnabled(False)
            self.selectFile.setEnabled(False)
            self.sizeInput.setEnabled(True)

    def findFile(self, LoadMapWindow):
        # open a window to choose files in PC
        fname = QtGui.QFileDialog.getOpenFileName(LoadMapWindow, 'Open file', '/home', '*.csv')
        self.fileName.setText(fname)  

    def startGame(self, LoadMapWindow):
        # initialize game state
        index = self.csvFlag.currentIndex()
        if index == 0:  
            QtGui.QMessageBox.about(LoadMapWindow, "Invalid Input", "Please choose a method of initialization")
        elif index == 1:
            fname = self.fileName.text()
            if not os.path.isfile(fname) or fname.split('.')[-1] != 'csv':
                self.fileName.clear()
                QtGui.QMessageBox.about(LoadMapWindow, "Invalid Input", "Please choose a valid csv file")
            else:
                LoadMapWindow.csv_flag = True
                LoadMapWindow.csv_file = fname
                self.gameInitial(LoadMapWindow)
        else:
            size = self.sizeInput.text()
            if size == '':
                QtGui.QMessageBox.about(LoadMapWindow, "Invalid Input", "Please choose a map size")
            elif int(size) % 2 == 0:
                QtGui.QMessageBox.about(LoadMapWindow, "Invalid Input", "Please choose an odd integer")
            else:
                LoadMapWindow.csv_flag = False
                LoadMapWindow.map_size = int(size)
                self.gameInitial(LoadMapWindow)
        

    def gameInitial(self, LoadMapWindow):
        # show game window
        LoadMapWindow.create_game()
        ui = Ui_GameWindow()
        ui.setupUi(LoadMapWindow)
        LoadMapWindow.show()


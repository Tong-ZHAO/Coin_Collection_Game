# -*- coding: utf-8 -*-
#!/usr/bin/env python
# author: tong
# date  : 04/11/2016

from PyQt4 import QtCore, QtGui
from one_player import Ui_SinglePlayerWindow
from two_player import Ui_TwoPlayerWindow
from load_map import Ui_LoadMapWindow
from rule import Ui_RuleWindow 

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

class Ui_MenuWindow(object):

    
    """ 
    This UI class of menu window.

    :function toSingleMode(self, MenuWindow) : called by "Single Mode" button
    :function toTwoMode(self, MenuWindow)    : called by "Two Player Mode" button
    :function toRule(self, MenuWindow)       : called by "Rule" button
    """

    def setupUi(self, MenuWindow):
        MenuWindow.setObjectName(_fromUtf8("MenuWindow"))
        MenuWindow.resize(600, 400)
        self.centralwidget = QtGui.QWidget(MenuWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem = QtGui.QSpacerItem(20, 7, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
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
        spacerItem3 = QtGui.QSpacerItem(20, 7, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_2.addWidget(self.line)
        spacerItem4 = QtGui.QSpacerItem(20, 7, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem5 = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setMargin(20)
        self.gridLayout_2.setHorizontalSpacing(100)
        self.gridLayout_2.setVerticalSpacing(50)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.singlePlayerButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.singlePlayerButton.sizePolicy().hasHeightForWidth())
        self.singlePlayerButton.setSizePolicy(sizePolicy)
        self.singlePlayerButton.setMinimumSize(QtCore.QSize(160, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.singlePlayerButton.setFont(font)
        self.singlePlayerButton.setObjectName(_fromUtf8("singlePlayerButton"))
        self.gridLayout_2.addWidget(self.singlePlayerButton, 0, 0, 1, 1)
        self.twoPlayersButton = QtGui.QPushButton(self.centralwidget)
        self.twoPlayersButton.setMinimumSize(QtCore.QSize(160, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.twoPlayersButton.setFont(font)
        self.twoPlayersButton.setObjectName(_fromUtf8("twoPlayersButton"))
        self.gridLayout_2.addWidget(self.twoPlayersButton, 0, 1, 1, 1)
        self.ruleButton = QtGui.QPushButton(self.centralwidget)
        self.ruleButton.setMinimumSize(QtCore.QSize(160, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ruleButton.setFont(font)
        self.ruleButton.setObjectName(_fromUtf8("ruleButton"))
        self.gridLayout_2.addWidget(self.ruleButton, 1, 0, 1, 1)
        self.exitButton = QtGui.QPushButton(self.centralwidget)
        self.exitButton.setMinimumSize(QtCore.QSize(160, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.exitButton.setFont(font)
        self.exitButton.setObjectName(_fromUtf8("exitButton"))
        self.gridLayout_2.addWidget(self.exitButton, 1, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        spacerItem6 = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem7 = QtGui.QSpacerItem(20, 7, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem7)
        MenuWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MenuWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MenuWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MenuWindow)

        # define action
        QtCore.QObject.connect(self.singlePlayerButton, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda: self.toSingleMode(MenuWindow))
        QtCore.QObject.connect(self.twoPlayersButton, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda: self.toTwoMode(MenuWindow))
        QtCore.QObject.connect(self.ruleButton, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda: self.showRule(MenuWindow))
        QtCore.QObject.connect(self.exitButton, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda: MenuWindow.close())
        QtCore.QMetaObject.connectSlotsByName(MenuWindow)

    def retranslateUi(self, MenuWindow):
        MenuWindow.setWindowTitle(_translate("MenuWindow", "Coin Collection Game", None))
        self.WelcomeTitle.setText(_translate("MenuWindow", "Welcome To", None))
        self.GameTitle.setText(_translate("MenuWindow", "Coin Collection Game", None))
        self.singlePlayerButton.setText(_translate("MenuWindow", "Single Player", None))
        self.twoPlayersButton.setText(_translate("MenuWindow", "Two Players", None))
        self.ruleButton.setText(_translate("MenuWindow", "Game Rule", None))
        self.exitButton.setText(_translate("MenuWindow", "Quit", None))

    def toSingleMode(self, MenuWindow):
        # change to next UI
        MenuWindow.mode = 1
        MenuWindow.player_index = 1   # in single player mode, the player begins at first 
        ui = Ui_SinglePlayerWindow()
        ui.setupUi(MenuWindow)
        MenuWindow.show()

    def toTwoMode(self, MenuWindow):
        # change to next UI
        MenuWindow.mode = 2
        ui = Ui_TwoPlayerWindow()
        ui.setupUi(MenuWindow)
        MenuWindow.show()

    def showRule(self, MenuWindow):
        # show rules
        ui = Ui_RuleWindow()
        ui.setupUi(MenuWindow)
        MenuWindow.show()

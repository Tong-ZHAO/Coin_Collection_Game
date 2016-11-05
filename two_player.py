# -*- coding: utf-8 -*-
#!/usr/bin/env python
# author: tong
# date  : 04/11/2016

from PyQt4 import QtCore, QtGui
from load_map import Ui_LoadMapWindow

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

class Ui_TwoPlayerWindow(object):

    """ 
    This UI class of two player window. You can go to the next window only if the players' name are not same.
    
    :function toChooseMap(self, TwoPlayerWindow): called by "Next" button
    """

    def setupUi(self, TwoPlayerWindow):
        TwoPlayerWindow.setObjectName(_fromUtf8("TwoPlayerWindow"))
        TwoPlayerWindow.resize(600, 400)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TwoPlayerWindow.sizePolicy().hasHeightForWidth())
        TwoPlayerWindow.setSizePolicy(sizePolicy)
        TwoPlayerWindow.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtGui.QWidget(TwoPlayerWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem = QtGui.QSpacerItem(20, 8, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
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
        spacerItem4 = QtGui.QSpacerItem(20, 8, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem5 = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(20, 10, 20, 20)
        self.gridLayout_2.setHorizontalSpacing(100)
        self.gridLayout_2.setVerticalSpacing(55)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.firstPlayerName = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.firstPlayerName.sizePolicy().hasHeightForWidth())
        self.firstPlayerName.setSizePolicy(sizePolicy)
        self.firstPlayerName.setObjectName(_fromUtf8("firstPlayerName"))
        self.gridLayout_2.addWidget(self.firstPlayerName, 0, 1, 1, 1)
        self.firstPlayerLabel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.firstPlayerLabel.setFont(font)
        self.firstPlayerLabel.setObjectName(_fromUtf8("firstPlayerLabel"))
        self.gridLayout_2.addWidget(self.firstPlayerLabel, 0, 0, 1, 1)
        self.secondPlayerName = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.secondPlayerName.sizePolicy().hasHeightForWidth())
        self.secondPlayerName.setSizePolicy(sizePolicy)
        self.secondPlayerName.setObjectName(_fromUtf8("secondPlayerName"))
        self.gridLayout_2.addWidget(self.secondPlayerName, 1, 1, 1, 1)
        self.secondPlayerLabel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.secondPlayerLabel.setFont(font)
        self.secondPlayerLabel.setObjectName(_fromUtf8("secondPlayerLabel"))
        self.gridLayout_2.addWidget(self.secondPlayerLabel, 1, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        spacerItem6 = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem7 = QtGui.QSpacerItem(20, 8, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem7)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem8 = QtGui.QSpacerItem(238, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.nextButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.nextButton.sizePolicy().hasHeightForWidth())
        self.nextButton.setSizePolicy(sizePolicy)
        self.nextButton.setMinimumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.nextButton.setFont(font)
        self.nextButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.nextButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nextButton.setAutoRepeatInterval(100)
        self.nextButton.setObjectName(_fromUtf8("nextButton"))
        self.horizontalLayout_3.addWidget(self.nextButton)
        spacerItem9 = QtGui.QSpacerItem(238, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem10 = QtGui.QSpacerItem(20, 8, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem10)
        TwoPlayerWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(TwoPlayerWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        TwoPlayerWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TwoPlayerWindow)
        QtCore.QObject.connect(self.nextButton, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda: self.toChooseMap(TwoPlayerWindow))
        QtCore.QMetaObject.connectSlotsByName(TwoPlayerWindow)

    def retranslateUi(self, TwoPlayerWindow):
        TwoPlayerWindow.setWindowTitle(_translate("TwoPlayerWindow", "Coin Collection Game", None))
        self.WelcomeTitle.setText(_translate("TwoPlayerWindow", "Welcome To", None))
        self.GameTitle.setText(_translate("TwoPlayerWindow", "Coin Collection Game", None))
        self.firstPlayerLabel.setText(_translate("TwoPlayerWindow", "Player 1 :  Name", None))
        self.secondPlayerLabel.setText(_translate("TwoPlayerWindow", "Player 2 :  Name", None))
        self.nextButton.setText(_translate("TwoPlayerWindow", "Next", None))

    def toChooseMap(self, TwoPlayerWindow):
        name_one = self.firstPlayerName.text()
        name_two = self.secondPlayerName.text()

        if name_one == '' or name_two == '':
            QtGui.QMessageBox.about(TwoPlayerWindow, "Invalid Input", "The players' names could not be blank!")
        elif name_one == name_two:
            QtGui.QMessageBox.about(TwoPlayerWindow, "Invalid Input", "The players' names could not be same")
            self.firstPlayerName.clear()
            self.secondPlayerName.clear()
        else:
            TwoPlayerWindow.player_name.append(name_one)
            TwoPlayerWindow.player_name.append(name_two)
            ui = Ui_LoadMapWindow()
            ui.setupUi(TwoPlayerWindow)
            TwoPlayerWindow.show()

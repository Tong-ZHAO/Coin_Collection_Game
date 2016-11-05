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

class Ui_SinglePlayerWindow(object):


    """ 
    This UI class of single player window. You can go to the next window only if the player's name is not blank.
    
    :function toChooseMap(self, SinglePlayerWindow): called by "Next" button
    """

    def setupUi(self, SinglePlayerWindow):
        SinglePlayerWindow.setObjectName(_fromUtf8("SinglePlayerWindow"))
        SinglePlayerWindow.resize(600, 400)
        self.centralwidget = QtGui.QWidget(SinglePlayerWindow)
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
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.selectDiffBox = QtGui.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.selectDiffBox.setFont(font)
        self.selectDiffBox.setObjectName(_fromUtf8("selectDiffBox"))
        self.selectDiffBox.addItem(_fromUtf8(""))
        self.selectDiffBox.addItem(_fromUtf8(""))
        self.selectDiffBox.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.selectDiffBox, 1, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        spacerItem6 = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem7 = QtGui.QSpacerItem(20, 6, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
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
        self.nextButton.setFont(font)
        self.nextButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.nextButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nextButton.setAutoRepeatInterval(100)
        self.nextButton.setObjectName(_fromUtf8("nextButton"))
        self.horizontalLayout_3.addWidget(self.nextButton)
        spacerItem9 = QtGui.QSpacerItem(238, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem10 = QtGui.QSpacerItem(20, 7, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem10)
        SinglePlayerWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(SinglePlayerWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        SinglePlayerWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SinglePlayerWindow)
        QtCore.QObject.connect(self.nextButton, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda: self.toChooseMap(SinglePlayerWindow))
        QtCore.QMetaObject.connectSlotsByName(SinglePlayerWindow)

    def retranslateUi(self, SinglePlayerWindow):
        SinglePlayerWindow.setWindowTitle(_translate("SinglePlayerWindow", "Coin Collection Game", None))
        self.WelcomeTitle.setText(_translate("SinglePlayerWindow", "Welcome To", None))
        self.GameTitle.setText(_translate("SinglePlayerWindow", "Coin Collection Game", None))
        self.label.setText(_translate("SinglePlayerWindow", "Player \'s  Name", None))
        self.label_2.setText(_translate("SinglePlayerWindow", "Game Difficulty", None))
        self.selectDiffBox.setItemText(0, _translate("SinglePlayerWindow", "Easy", None))
        self.selectDiffBox.setItemText(1, _translate("SinglePlayerWindow", "Middle", None))
        self.selectDiffBox.setItemText(2, _translate("SinglePlayerWindow", "Hard", None))
        self.nextButton.setText(_translate("SinglePlayerWindow", "Next", None))

    def toChooseMap(self, SinglePlayerWindow):
        name = self.lineEdit.text()
        if name == '' or name == "PC":        
            self.lineEdit.clear()
            QtGui.QMessageBox.about(SinglePlayerWindow, "Invalid Input", "The player's name could not be blank or 'PC'")
        else:
            SinglePlayerWindow.player_name.append("PC")    
            SinglePlayerWindow.player_name.append(name)
            SinglePlayerWindow.choose_diff = self.selectDiffBox.currentIndex()
            ui = Ui_LoadMapWindow()
            ui.setupUi(SinglePlayerWindow)
            SinglePlayerWindow.show() 

# -*- coding: utf-8 -*-
#!/usr/bin/env python
# author: tong
# date  : 04/11/2016

from PyQt4 import QtCore, QtGui
import menu

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

class Ui_RuleWindow(object):

    """ 
    This UI class of rule window.
    
    :function toMenu(self, RuleWindow): called by "Back" button
    """

    def setupUi(self, RuleWindow):
        RuleWindow.setObjectName(_fromUtf8("RuleWindow"))
        RuleWindow.resize(600, 400)
        self.centralwidget = QtGui.QWidget(RuleWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem = QtGui.QSpacerItem(20, 23, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
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
        spacerItem3 = QtGui.QSpacerItem(20, 22, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_2.addWidget(self.line)
        spacerItem4 = QtGui.QSpacerItem(20, 23, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem5 = QtGui.QSpacerItem(228, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.rule_label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.rule_label.setFont(font)
        self.rule_label.setAlignment(QtCore.Qt.AlignCenter)
        self.rule_label.setObjectName(_fromUtf8("rule_label"))
        self.horizontalLayout_3.addWidget(self.rule_label)
        spacerItem6 = QtGui.QSpacerItem(218, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.rule_text = QtGui.QTextBrowser(self.centralwidget)
        self.rule_text.setObjectName(_fromUtf8("rule_text"))
        self.verticalLayout_2.addWidget(self.rule_text)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem7 = QtGui.QSpacerItem(218, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.backButton = QtGui.QPushButton(self.centralwidget)
        self.backButton.setObjectName(_fromUtf8("backButton"))
        self.horizontalLayout_2.addWidget(self.backButton)
        spacerItem8 = QtGui.QSpacerItem(218, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem9 = QtGui.QSpacerItem(20, 22, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem9)
        RuleWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(RuleWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        RuleWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(RuleWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        RuleWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RuleWindow)
        QtCore.QObject.connect(self.backButton, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda: self.toMenu(RuleWindow))
        QtCore.QMetaObject.connectSlotsByName(RuleWindow)

    def retranslateUi(self, RuleWindow):
        RuleWindow.setWindowTitle(_translate("RuleWindow", "Coin Collection Game", None))
        self.WelcomeTitle.setText(_translate("RuleWindow", "Welcome To", None))
        self.GameTitle.setText(_translate("RuleWindow", "Coin Collection Game", None))
        self.rule_label.setText(_translate("RuleWindow", "Game Rule", None))
        self.rule_text.setHtml(_translate("RuleWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">We have two players and a n*n map. At each point of the map, there is a coin with a random values (5, 10, 20, 50 ,100, 200). (You can choose to load the map from a csv file)</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> At the beginning, the king stands in the center of the map. Then you take turns to move it in the map. But make sure to follow the two restraints below.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(1) The king cannot go out the map</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(2) The king can only move to nearby points with coins.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Each player collects coins in his bag after the king arriving on a new point. Game is over when the king cannot move and the player having higher value of coins win.</p></body></html>", None))
        self.backButton.setText(_translate("RuleWindow", "Back", None))

    def toMenu(self, RuleWindow):
        ui = menu.Ui_MenuWindow()
        ui.setupUi(RuleWindow)
        RuleWindow.show()

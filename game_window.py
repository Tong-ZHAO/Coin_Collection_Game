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

class Ui_GameWindow(object):

    """ 
    This UI class of this game. 
    
    :function record(self, GameWindow)          : to be sure that the player could only choose one direction
    :function first_confirm(self, GameWindow)   : the 1st player confirms his/her choice
    :function second_confirm(self, GameWindow)  : the 2nd player confirms his/her choice
    :function game_finish(self, GameWindow)     : if game is over, this function will be called
    """

    def setupUi(self, GameWindow):
        GameWindow.setObjectName(_fromUtf8("GameWindow"))
        GameWindow.resize(600, 400)
        font = QtGui.QFont()
        font.setPointSize(10)
        GameWindow.setFont(font)
        self.centralwidget = QtGui.QWidget(GameWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        spacerItem = QtGui.QSpacerItem(20, 6, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(178, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.GameTitle = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.GameTitle.setFont(font)
        self.GameTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.GameTitle.setObjectName(_fromUtf8("GameTitle"))
        self.horizontalLayout.addWidget(self.GameTitle)
        spacerItem2 = QtGui.QSpacerItem(188, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        spacerItem3 = QtGui.QSpacerItem(20, 4, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_5.addWidget(self.line)
        spacerItem4 = QtGui.QSpacerItem(20, 6, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem5 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.table_layout = QtGui.QGridLayout()
        self.table_layout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.table_layout.setObjectName(_fromUtf8("table_layout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
    
        # To set gridLayout according to the game map
        self.table_size = GameWindow.my_game.my_grid.size
        positions = [(i,j) for i in range(self.table_size) for j in range(self.table_size)]
        names = [GameWindow.my_game.my_grid.grid[i][j] for i in range(self.table_size) for j in range(self.table_size)]
        names[pow(self.table_size, 2) // 2] = names[pow(self.table_size, 2) // 2][:0] + '###'
        for position, name in zip(positions, names):
            button = QtGui.QPushButton(name)
            button.setFixedWidth(50)
            button.setCheckable(True)      # let the button can be hold
            QtCore.QObject.connect(button, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda: self.record(GameWindow))
            if [position[0], position[1]] not in GameWindow.enable_button:
                button.setEnabled(False)   # if this position cannot be reach, set to be false
            self.gridLayout.addWidget(button, *position)

        self.table_layout.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.confirm_button_1 = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.confirm_button_1.setFont(font)
        self.confirm_button_1.setObjectName(_fromUtf8("confirm_button_1"))
        self.horizontalLayout_2.addWidget(self.confirm_button_1)
        self.confirm_button_2 = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.confirm_button_2.setFont(font)
        self.confirm_button_2.setObjectName(_fromUtf8("confirm_button_2"))
        self.horizontalLayout_2.addWidget(self.confirm_button_2)
        self.table_layout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.table_layout.setRowStretch(0, 6)
        self.table_layout.setRowStretch(1, 1)
        self.horizontalLayout_3.addLayout(self.table_layout)
        spacerItem6 = QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 10, -1, 10)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.title_1 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.title_1.setFont(font)
        self.title_1.setAlignment(QtCore.Qt.AlignCenter)
        self.title_1.setObjectName(_fromUtf8("title_1"))
        self.verticalLayout.addWidget(self.title_1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setContentsMargins(30, 10, 30, 10)
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setVerticalSpacing(15)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.score_label_1 = QtGui.QLabel(self.centralwidget)
        self.score_label_1.setObjectName(_fromUtf8("score_label_1"))
        self.gridLayout_2.addWidget(self.score_label_1, 3, 0, 1, 1)
        self.name_label_1 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.name_label_1.setFont(font)
        self.name_label_1.setObjectName(_fromUtf8("name_label_1"))
        self.gridLayout_2.addWidget(self.name_label_1, 1, 0, 1, 1)
        self.player_name_1 = QtGui.QLabel(self.centralwidget)
        self.player_name_1.setObjectName(_fromUtf8("player_name_1"))
        self.gridLayout_2.addWidget(self.player_name_1, 1, 1, 1, 1)
        self.player_score_1 = QtGui.QLabel(self.centralwidget)
        self.player_score_1.setObjectName(_fromUtf8("player_score_1"))
        self.gridLayout_2.addWidget(self.player_score_1, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(0, 10, -1, 10)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.title_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.title_2.setFont(font)
        self.title_2.setAlignment(QtCore.Qt.AlignCenter)
        self.title_2.setObjectName(_fromUtf8("title_2"))
        self.verticalLayout_2.addWidget(self.title_2)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setContentsMargins(30, 10, 30, 10)
        self.gridLayout_3.setHorizontalSpacing(20)
        self.gridLayout_3.setVerticalSpacing(15)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.name_label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.name_label_2.setFont(font)
        self.name_label_2.setObjectName(_fromUtf8("name_label_2"))
        self.gridLayout_3.addWidget(self.name_label_2, 1, 0, 1, 1)
        self.score_label_2 = QtGui.QLabel(self.centralwidget)
        self.score_label_2.setObjectName(_fromUtf8("score_label_2"))
        self.gridLayout_3.addWidget(self.score_label_2, 3, 0, 1, 1)
        self.player_name_2 = QtGui.QLabel(self.centralwidget)
        self.player_name_2.setObjectName(_fromUtf8("player_name_2"))
        self.gridLayout_3.addWidget(self.player_name_2, 1, 1, 1, 1)
        self.player_score_2 = QtGui.QLabel(self.centralwidget)
        self.player_score_2.setObjectName(_fromUtf8("player_score_2"))
        self.gridLayout_3.addWidget(self.player_score_2, 3, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        spacerItem7 = QtGui.QSpacerItem(20, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem7)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        spacerItem8 = QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        spacerItem9 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        self.verticalLayout_5.addItem(spacerItem9)
        GameWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(GameWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 24))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        GameWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(GameWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        GameWindow.setStatusBar(self.statusbar)

        # enable buttons to indicate the player
        if GameWindow.mode is 1:
            self.confirm_button_1.setEnabled(False)
        elif GameWindow.player_index is 0:
            self.confirm_button_1.setEnabled(True)
            self.confirm_button_2.setEnabled(False)
        elif GameWindow.player_index is 1:
            self.confirm_button_2.setEnabled(True)
            self.confirm_button_1.setEnabled(False)
        

        self.retranslateUi(GameWindow)
        QtCore.QObject.connect(self.confirm_button_1, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda: self.first_confirm(GameWindow))
        QtCore.QObject.connect(self.confirm_button_2, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda: self.second_confirm(GameWindow))
        QtCore.QMetaObject.connectSlotsByName(GameWindow)

    def retranslateUi(self, GameWindow):
        GameWindow.setWindowTitle(_translate("GameWindow", "Coin Collection Game", None))
        self.GameTitle.setText(_translate("GameWindow", "Coin Collection Game", None))
        self.confirm_button_1.setText(_translate("GameWindow", "Player 1 : Confirm", None))
        self.confirm_button_2.setText(_translate("GameWindow", "Player 2 : Confirm", None))
        self.title_1.setText(_translate("GameWindow", "Player 1", None))
        self.score_label_1.setText(_translate("GameWindow", "Score : ", None))
        self.name_label_1.setText(_translate("GameWindow", "Name : ", None))
        self.player_name_1.setText(_translate("GameWindow", GameWindow.my_game.players[0].name, None))
        self.player_score_1.setText(_translate("GameWindow", str(GameWindow.my_game.players[0].score), None))
        self.title_2.setText(_translate("GameWindow", "Player 2", None))
        self.name_label_2.setText(_translate("GameWindow", "Name : ", None))
        self.score_label_2.setText(_translate("GameWindow", "Score : ", None))
        self.player_name_2.setText(_translate("GameWindow", GameWindow.my_game.players[1].name, None))
        self.player_score_2.setText(_translate("GameWindow", str(GameWindow.my_game.players[1].score), None))

    def record(self, GameWindow):
        # to make sure only one button can be hold by the player
        button = GameWindow.sender()
        idx = self.gridLayout.indexOf(button)
        click_index = self.gridLayout.getItemPosition(idx)
        click_x = click_index[0]
        click_y = click_index[1]
        if GameWindow.choose_x is -1:
            GameWindow.choose_x = click_x
            GameWindow.choose_y = click_y
        else:
            self.gridLayout.itemAt(GameWindow.choose_x * self.table_size + GameWindow.choose_y).widget().setChecked(False)
            GameWindow.choose_x = click_x
            GameWindow.choose_y = click_y

    def first_confirm(self, GameWindow):
        # the 1st player confirms his/her choice
        pre_x, pre_y = GameWindow.my_game.get_place()
        self.gridLayout.itemAtPosition(pre_x, pre_y).widget().setText("0")           # change "###" to be "0"
        GameWindow.my_game.player_move(0, GameWindow.choose_x, GameWindow.choose_y)  # move to a new place
        self.gridLayout.itemAtPosition(GameWindow.choose_x, GameWindow.choose_y).widget().setText("###")  # set new position to be "###"
        self.gridLayout.itemAtPosition(GameWindow.choose_x, GameWindow.choose_y).widget().setChecked(False)
        GameWindow.enable_button = GameWindow.my_game.find_points(GameWindow.choose_x, GameWindow.choose_y) 
        if len(GameWindow.enable_button) == 0:     # game over
            self.game_finish(GameWindow)
            return 0
        for i in range(self.gridLayout.count()):   # enable positions which could be reached
            item = self.gridLayout.itemAt(i).widget()
            if [i // self.table_size, i % self.table_size] in GameWindow.enable_button:
                item.setEnabled(True)
            else:
                item.setEnabled(False)
        GameWindow.player_index = 1                # change player index to 1
        self.player_score_1.setText(str(GameWindow.my_game.players[0].score))  # update scores
        self.player_score_2.setText(str(GameWindow.my_game.players[1].score))
        GameWindow.choose_x, GameWindow.choose_y = -1, -1
        self.confirm_button_1.setEnabled(False)                                # change confirm button
        self.confirm_button_2.setEnabled(True)

    def second_confirm(self, GameWindow):
        # the 2nd player confirms his/her choice
        pre_x, pre_y = GameWindow.my_game.get_place()
        self.gridLayout.itemAtPosition(pre_x, pre_y).widget().setText("0")          # set "###" to be "0"
        GameWindow.my_game.player_move(1, GameWindow.choose_x, GameWindow.choose_y) # move king
        GameWindow.enable_button = GameWindow.my_game.find_points(GameWindow.choose_x, GameWindow.choose_y)
        if len(GameWindow.enable_button) == 0:           # Game over
            self.gridLayout.itemAtPosition(GameWindow.choose_x, GameWindow.choose_y).widget().setText("###")
            self.gridLayout.itemAtPosition(GameWindow.choose_x, GameWindow.choose_y).widget().setChecked(False)
            self.game_finish(GameWindow)
            return 0
        if GameWindow.mode == 1:                         # if the game is in single mode, let PC to choose a position
            self.gridLayout.itemAtPosition(GameWindow.choose_x, GameWindow.choose_y).widget().setText("0")
            self.gridLayout.itemAtPosition(GameWindow.choose_x, GameWindow.choose_y).widget().setChecked(False)
            GameWindow.my_game.pc_move(0)                # PC moves king
            post_x, post_y = GameWindow.my_game.get_place()
            self.gridLayout.itemAtPosition(post_x, post_y).widget().setText("###")
        else:                                            # if the game is in two player mode, change turn to the 1st player
            self.gridLayout.itemAtPosition(GameWindow.choose_x, GameWindow.choose_y).widget().setText("###")
            self.gridLayout.itemAtPosition(GameWindow.choose_x, GameWindow.choose_y).widget().setChecked(False)
            post_x, post_y = GameWindow.choose_x, GameWindow.choose_y
            GameWindow.player_index = 0
            self.confirm_button_1.setEnabled(True)
            self.confirm_button_2.setEnabled(False)

        GameWindow.enable_button = GameWindow.my_game.find_points(post_x, post_y)
        if len(GameWindow.enable_button) == 0:           # Game over
            self.game_finish(GameWindow)
            return 0

        for i in range(self.gridLayout.count()):         # enable positions which could be reach
            item = self.gridLayout.itemAt(i).widget()
            if [i // self.table_size, i % self.table_size] in GameWindow.enable_button:
                item.setEnabled(True)
            else:
                item.setEnabled(False)
        self.player_score_1.setText(str(GameWindow.my_game.players[0].score))   # update score
        self.player_score_2.setText(str(GameWindow.my_game.players[1].score))
        GameWindow.choose_x, GameWindow.choose_y = -1, -1

    def game_finish(self, GameWindow):
        # called when game is over
        self.player_score_1.setText(str(GameWindow.my_game.players[0].score))   # update scores
        self.player_score_2.setText(str(GameWindow.my_game.players[1].score))
        for item in (self.gridLayout.itemAt(i).widget() for i in range(self.gridLayout.count())):  # unenable all buttons
            item.setEnabled(False)
        print_text = GameWindow.my_game.game_over()                             # get winner
        QtGui.QMessageBox.about(GameWindow, "Game Over", print_text)            # show a message box to indicate winner
        result = QtGui.QMessageBox.question(GameWindow, "Message" ,"Do you want to restart a new game?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)    # ask for restarting game.

        if result == QtGui.QMessageBox.Yes:
            ui = menu.Ui_MenuWindow()
            ui.setupUi(GameWindow)
            GameWindow.show()
        else:
            pass

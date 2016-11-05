#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: tong
# date  : 04/11/2016

from PyQt4 import QtGui
from coin_game import Game
import random

class MyWindow(QtGui.QMainWindow): 

    """ 
    This class is used to overload pyqt's MainWindow class to load and save the game state.

    :param mode          : an integer to indicate game mode (1 - single mode, 2 - two player mode)
    :param player_name   : a string list to store players' names
    :param csv_flag      : a bool value to indicate whether we load map from a csv file
    :param csv_file      : a string of the path of csv file
    :param map_size      : an integer of our map size
    :param choose_diff   : an integer to decide the intelligence of AI (0 - Easy, 1 - Middle, 2 - Hard)
    :param my_game       : a Game class instance
    :param enable_button : a list to store available buttons
    :param player_index  : an integer to indicate the current player index
    :param choose_x      : an integer to indicate current player's choose of coordinate x
    :param choose_y      : an integer to indicate current player's choose of coordinate y
    """

    def __init__(self, parent = None):

        super(MyWindow, self).__init__(parent)
        self.mode = 0
        self.player_name = []
        self.csv_flag = False
        self.csv_file = None
        self.map_size = None
        self.choose_diff = -1
        self.my_game = None    
        self.enable_button = []
        self.player_index = 0 if (random.randint(0, 100) % 2) == 0 else 1  # use a secret number to decide who begins game
        self.choose_x, self.choose_y = -1, -1 
 
    def closeEvent(self, event):
        # show a message box when quitting
        quit_msg = "Are you sure you want to quit the game?" 
        reply = QtGui.QMessageBox.question(self, 'Message', quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No) 

        if reply == QtGui.QMessageBox.Yes: 
            event.accept() 
        else: 
            event.ignore() 

    def create_game(self):
        # initialize game state
        self.my_game = Game(self.mode, self.map_size, self.csv_file, self.player_name, self.choose_diff)
        center = self.my_game.my_grid.size // 2
        self.enable_button = self.my_game.find_points(center, center)

        

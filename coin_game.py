#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: tong
# date  : 04/11/2016

import random
import csv
import os

INF = 10000      # maximum value for AI algorithm
value = ['5', '10', '20', '50', '100', '200']  # coin value

class Grid:

    """ 
    This class is used to create a grid to save the game map. It needs a positive odd integer or a csv file to initialize the map.

    :param __size: A private variable to keep the map size. It cannot be overwritten after the initialization.
                   But it can be read by using the function "size".
    :param grid  : A 2-dimension string list to save the map. It can be read and modified outside. It will be initialized
                   to be None. When the game starts, it will be filled with random value.

    """


    def __init__(self, size = None, csv_file = None):
        # a constructer with two optional choices - randomizing or loading csv file
        if csv_file is not None:                                # load csv file to initialize "grid" and "size"
            self.__size, self.grid = self.init_csv(csv_file)
        else:                                                   # initialize "size" and choose values randomly
            self.__size = size
            self.grid = [[random.choice(value) for col in range(size)] for row in range(size)]
        center = self.__size // 2
        self.grid[center][center] = '0'

    @property
    def size(self):
        # To make size visiable from outside
        return int(self.__size)

    def __contains__(self, item):
        # To overload keyword "in". Return True if grid(x, y) still has a coin, which means that the point can be reached.
        x,y = (int(i) for i in item)
        assert(x >= 0 and x < self.__size and y >= 0 and y < self.__size)
        return True if self.grid[x][y] != '0' else False

    def init_csv(self, csv_path):
        # To load grid from a csv file
        assert(os.path.exists(csv_path)), "The csv file does not exist, please check again."
        with open(csv_path, newline = '') as csvfile:
            grid_csv = csv.reader(csvfile)
            grid = [row for row in grid_csv]
            grid_size = len(grid)
        return grid_size, grid

class Player:

    """
    This class is used to create a player and save his/her state. It needs a name to initialize player's name.

    :param __name : A string of the player's name. It can be read from outside but cannot be modified.
    :param __score: A integer representing the player's score. It can be read from outside. To add the score, we have to use the
                    function add_score().
    """


    def __init__(self, str_name):
        # Initialize player's name. Set score to be 0. Set position to be (-1, -1) (invalid)
        self.__name = str_name
        self.__score = 0

    @property
    def name(self):
        # Let name can be read from outside
        return self.__name

    @property
    def score(self):
        # Let score can be read from outside
        return self.__score

    def add_score(self, value):
        # Add an integer "value" to score.
        self.__score += value


class Game:

    """
    The most important class in the game. It includes the functions of moving, judging and caulculating. It need five parameters
    to initialize. An integer "game_mode" to indicate whether we want to play with computer. An integer "size" to indicate the map size. 
    A string "csv_path" if we want to load map from a csv file. A string list to indicate two player's name. And an integer "difficulty"
    to decide the intelligence of AI.

    :param my_grid  : A grid instanse to save the game map.
    :param players  : A list to save two instanses of players.
    :param px       : An integer to record the x index of the king
    :param py       : An integer to record the y index of the king
    :param best_pos : A list of two elements [x, y] to save AI results
    :param mode     : An integer to record game mode. 1 - single mode. 2 - two player mode
    :param depth    : An integer to record game difficulty. (1 - easy, 3 - middle, 5 - hard)

    """

    def __init__(self, game_mode, size, csv_path, name_list, difficulty):
        # Initialize the game. Create a grid, a list of two players.
        self.my_grid = Grid(size, csv_path)      # create a grid
        center = self.my_grid.size // 2          # initialize position
        self.px, self.py = [center, center]      # initialize start point

        self.mode = game_mode
        self.players = [Player(name_list[0]), Player(name_list[1])]    # initialize player list
        self.dep = (2 * difficulty + 1) if difficulty != -1 else -1    # set game difficulty 
        self.best_pos = []

    def set_place(self, in_x, in_y):
        # set the king to point (in_x, in_y)
        assert(in_x >= 0 and in_x < self.my_grid.size and in_y >= 0 and in_y < self.my_grid.size), "Invalid place."
        self.px, self.py = in_x, in_y

    def get_place(self):
        # return the king's place
        return (self.px, self.py)

    def find_points(self, current_x, current_y):
        # find possible choices around (current_x, current_y)
        points = []
        g_size = self.my_grid.size
        for i in range(3):                                                     # test a 3*3 sub-map around player's old position
            for j in range(3):
                if (current_x+i-1) >= 0 and (current_x+i-1) < g_size and (current_y+j-1) >= 0 and (current_y+j-1) < g_size and (current_x+i-1, current_y+j-1) in self.my_grid:
                    points.append([current_x+i-1, current_y+j-1])              # if the point has non-zero value, add to list "pos_point" 
        return points

    def pc_move(self, index):
        # execute a move action for computer. 
        pre_x, pre_y = self.get_place()                               # get the king's position
        self.mini_max(pre_x, pre_y, self.dep, True)                   # find the best position using Minimax-algorithm
        post_x, post_y = (self.best_pos[i] for i in range(2))
        self.set_place(post_x, post_y)                                # move the king
        self.players[index].add_score(int(self.my_grid.grid[post_x][post_y]))
        self.my_grid.grid[post_x][post_y] = '0'                       # change value in grid

    def player_move(self, index, post_x, post_y):
        # execute a move action for ith player to point (post_x, post_y). 
        self.set_place(post_x, post_y)
        self.players[index].add_score(int(self.my_grid.grid[post_x][post_y]))
        self.my_grid.grid[post_x][post_y] = '0'                   # change value in grid

    def calculate_score(self):
        # Return the difference value of two players' scores
        return (self.players[0].score - self.players[1].score)

    def mini_max(self, current_x, current_y, depth, is_max):
        # The implement of AI algorithm.
        pos_point = self.find_points(current_x, current_y)
        if(len(pos_point) == 0 or depth == 0):              # if "game over" or "depth is 0", finish recursion
            return self.calculate_score()
        elif(is_max):                                       # PC's turn
            val = -INF
            for point in pos_point:                         # check all possible points
                diff_score = int(self.my_grid.grid[point[0]][point[1]])    # record value for restoring after recursion
                self.players[0].add_score(diff_score)                    # change state
                self.my_grid.grid[point[0]][point[1]] = '0'
                new_score = self.mini_max(point[0], point[1], depth-1, False)  # recursion
                if(val < new_score):                                           # update val
                    if(depth == self.dep):                                     # only update the position in top layer
                        self.best_pos = point
                    val = new_score
                self.my_grid.grid[point[0]][point[1]] = str(diff_score)        # finish calculation, restore value 
                self.players[0].add_score(-diff_score)                       # restore the player's point
            return val
        else:                                             # player's turn, the same as PC's turn, except for not updating the best position
            val = INF
            for point in pos_point:                         
                diff_score = int(self.my_grid.grid[point[0]][point[1]])
                self.players[1].add_score(diff_score)
                self.my_grid.grid[point[0]][point[1]] = '0'
                new_score = self.mini_max(point[0], point[1], depth-1, True)
                if(val > new_score):
                    val = new_score
                self.my_grid.grid[point[0]][point[1]] = str(diff_score)
                self.players[1].add_score(-diff_score)
            return val

    def game_over(self):
        # Excute when game is over. Decide winner and print scores.
        if self.calculate_score() > 0:
            return (self.players[0].name + " wins. His/Her score is " + str(self.players[0].score))
        elif self.calculate_score() < 0 :
            return (self.players[1].name + " wins. His/Her score is " + str(self.players[1].score))
        else:
            return "Two players have the same score. The game ends in a draw."


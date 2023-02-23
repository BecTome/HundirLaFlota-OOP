import random
import numpy as np
import sys
import os
sys.path.append(os.getcwd())

from HLF.utils import config

class Tablero:
    def_board_size = config.BOARD_SIZE
    boat_sign = config.BOAT_SIGN
    boat_sizes = config.BOAT_SIZES
    empty_sign = config.EMPTY_SIGN
    hit_sign = config.HIT_SIGN
    water_sign = config.WATER_SIGN

    def __init__(self, board_size=def_board_size):
        self.board_size = board_size
        self.tablero = np.full(shape=(self.board_size, self.board_size), fill_value=self.empty_sign)

    def __clear(self):
        self.tablero = np.full(shape=(self.board_size, self.board_size), fill_value=self.empty_sign)

    def random_init(self):
        self.__clear()
        self.info = [] # Debugging purpose
        for boat_size in self.boat_sizes:
            while True:
                orig = (random.randint(0, self.board_size - 1), random.randint(0, self.board_size - 1))
                orient = random.choice(["N", "S", "E", "W"])
                try:
                    self.place_boat(orient, orig, boat_size)
                    break
                except ValueError:
                    continue

            self.info.append((boat_size, orient, orig))
            
    def place_boat(self, orient, orig, boat_size):
        if self.__valid_position(orient, orig, boat_size):
            if orient == "W":
                self.tablero[orig[0] , (orig[1] - boat_size + 1):(orig[1] + 1)] = self.boat_sign
            elif orient == "E":
                self.tablero[orig[0] , orig[1]:(orig[1] + boat_size)] = self.boat_sign
            elif orient == "N":
                self.tablero[(orig[0] - boat_size + 1):(orig[0] + 1) , orig[1]] = self.boat_sign
            elif orient == "S":
                self.tablero[orig[0]:(orig[0] + boat_size) , orig[1]] = self.boat_sign
        else:
            raise ValueError("Invalid position for a boat")
    
    def __valid_position(self, orient, orig, boat_size):
        if orient == "N":
            cond_border = (orig[0] - boat_size + 1) >= 0
            cond_overlap = np.any(self.tablero[(orig[0] - boat_size + 1):(orig[0] + 1) , orig[1]] == self.boat_sign)
        elif orient == "S":
            cond_border = (orig[0] + boat_size - 1) < self.board_size
            cond_overlap = np.any(self.tablero[orig[0]:(orig[0] + boat_size) , orig[1]] == self.boat_sign)
        elif orient == "E":
            cond_border = (orig[1] + boat_size - 1) < self.board_size
            cond_overlap = np.any(self.tablero[orig[0] , orig[1]:(orig[1] + boat_size)] == self.boat_sign)
        elif orient == "W":
            cond_border = (orig[1] - boat_size + 1) >= 0
            cond_overlap = np.any(self.tablero[orig[0] , (orig[1] - boat_size + 1):(orig[1] + 1)] == self.boat_sign) 
        return cond_border and not cond_overlap

    def __str__(self):
        return str(self.tablero)
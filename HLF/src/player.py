import sys
import os
sys.path.append(os.getcwd())
from HLF.src.tablero import Tablero

class Player():

    def __init__(self, name, tablero):
        self.tablero = tablero
        self.tablero.random_init()
        self.name = name
    
    def receive_shot(self, x, y):
        if self.tablero.tablero[x][y] == self.tablero.boat_sign:
            self.tablero.tablero[x][y] = self.tablero.hit_sign
        elif self.tablero.tablero[x][y] == self.tablero.empty_sign:
            self.tablero.tablero[x][y] = self.tablero.water_sign

    def __str__(self):
        return self.name + "\n" + str(self.tablero) + "\n"

class Computer():

    def __init__(self, name, tablero):
        self.name = name
        self.__tablero = tablero
        self.__tablero.random_init()
        self.tablero = Tablero(tablero.board_size)

    def receive_shot(self, x, y):
        if self.__tablero.tablero[x][y] == self.__tablero.boat_sign:
            self.tablero.tablero[x][y] = self.__tablero.hit_sign
            self.__tablero.tablero[x][y] = self.__tablero.hit_sign
        elif self.__tablero.tablero[x][y] == self.__tablero.empty_sign:
            self.tablero.tablero[x][y] = self.__tablero.water_sign
            self.__tablero.tablero[x][y] = self.__tablero.water_sign
    
    def __str__(self):
        return self.name + "\n" + str(self.tablero) + "\n"
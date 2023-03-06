import sys
import os
from time import sleep
import numpy as np
sys.path.append(os.getcwd())
from HLF.src.tablero import Tablero

class Player():
    impacted = False
    finished = False

    def __init__(self, name, tablero):
        self.tablero = tablero
        self.tablero.random_init()
        self.name = name
    
    def receive_shot(self, x, y):
        if self.tablero.tablero[x][y] == self.tablero.boat_sign:
            self.tablero.tablero[x][y] = self.tablero.hit_sign
            self.impacted = True

        elif self.tablero.tablero[x][y] == self.tablero.empty_sign:
            self.tablero.tablero[x][y] = self.tablero.water_sign
            self.impacted = False
        
        self.finished = (np.sum(self.tablero.tablero == self.tablero.hit_sign) == sum(self.tablero.boat_sizes))
    
    def shoot(self, player_rival):
        print(f"Turno de {self.name}\n")
        while True:
            while True:
                try:
                    x = int(input("Introduzca coordenada X: "))
                    y = int(input("Introduzca coordenada Y: "))
                except ValueError:
                    print("Introduce valores enteros")
                    continue

                if player_rival.tablero.check_coordinates(x, y):
                    break
                else:
                    print("Introduzca coordenadas dentro del tablero y en las que no se haya disparado ya")
                    continue
            
            print(f"Ataque en {(x, y)}!!\n")

            sleep(3)

            player_rival.receive_shot(x, y)

            print(self)
            print(player_rival)

            if player_rival.impacted & player_rival.finished:
                break
            elif player_rival.impacted:
                print(f"TOCADO!! {self.name.upper()} DISPARA DE NUEVO\n")
                continue
            else:
                print("AGUA!!")
                break


    def __str__(self):
        return self.name + "\n" + str(self.tablero) + "\n"

class Computer():
    impacted = False
    finished = False

    def __init__(self, name, tablero):
        self.name = name
        self.__tablero = tablero
        self.__tablero.random_init()
        self.tablero = Tablero(tablero.board_size)

    def receive_shot(self, x, y):
        if self.__tablero.tablero[x][y] == self.__tablero.boat_sign:
            self.tablero.tablero[x][y] = self.__tablero.hit_sign
            self.__tablero.tablero[x][y] = self.__tablero.hit_sign
            self.impacted = True
        elif self.__tablero.tablero[x][y] == self.__tablero.empty_sign:
            self.tablero.tablero[x][y] = self.__tablero.water_sign
            self.__tablero.tablero[x][y] = self.__tablero.water_sign
            self.impacted = False
        
        self.finished = (np.sum(self.tablero.tablero == self.tablero.hit_sign) == sum(self.tablero.boat_sizes))

    def shoot(self, player_rival):
        print(f"Turno de {self.name}\n")
        while True:
            while True:
                x, y = np.random.randint(0, player_rival.tablero.board_size, 2)

                if player_rival.tablero.check_coordinates(x, y):
                    break
                else:
                    continue
            
            print(f"Ataque en {(x, y)}!!\n")

            sleep(3)

            player_rival.receive_shot(x, y)

            print(player_rival)
            print(self)

            if player_rival.impacted & player_rival.finished:
                break
            elif player_rival.impacted:
                print(f"TOCADO!! {self.name.upper()} DISPARA DE NUEVO\n")
                continue
            else:
                print("AGUA!!")
                break
        
    def __str__(self):
        return self.name + "\n" + str(self.tablero) + "\n"
from HLF.src.tablero import Tablero
from HLF.src.player import Player, Computer
from HLF.utils.config import BOARD_SIZE, BOAT_SIGN, HIT_SIGN, BOAT_SIZES
import numpy as np
from time import sleep

tab_jugador = Tablero(BOARD_SIZE)
tab_comp = Tablero(BOARD_SIZE)

player_alb = Player("Alberto", tab_jugador)
player_comp = Computer("Computer", tab_comp)

print(player_alb)
print(player_comp)

while True:
    while True:
        print(f"Turno de {player_alb.name}\n")

        while True:
            player_x = int(input("Introduzca coordenada X: "))
            player_y = int(input("Introduzca coordenada Y: "))

            if tab_comp.check_coordinates(player_x, player_y):
                break
            else:
                print("Introduzca coordenadas dentro del tablero y en las que no se haya disparado ya")

        print(f"Ataque en {(player_x, player_y)}!!\n")

        sleep(3)

        player_comp.receive_shot(player_x, player_y)

        print(player_alb)
        print(player_comp)

        if player_comp.impacted:
            if np.sum(player_comp.tablero.tablero == HIT_SIGN) == sum(BOAT_SIZES):
                break
            else:
                print(f"TOCADO!! {player_alb.name.upper()} DISPARA DE NUEVO\n")
                continue
        else:
            print("AGUA!!")
            break
    
    if np.sum(player_comp.tablero.tablero == HIT_SIGN) == sum(BOAT_SIZES):
        print(f"FIN DEL JUEGO. {player_alb.name.upper()} GANA")
        break

    while True:
        print(f"Turno de {player_comp.name}\n")
        while True:
            comp_x, comp_y = np.random.randint(0, BOARD_SIZE, 2)

            if tab_jugador.check_coordinates(comp_x, comp_y):
                break

        print(f"Ataque en {(comp_x, comp_y)}!!\n")
        
        sleep(3)

        player_alb.receive_shot(comp_x, comp_y)

        print(player_alb)
        print(player_comp)

        if player_alb.impacted:
            
            if np.sum(player_alb.tablero.tablero == HIT_SIGN) == sum(BOAT_SIZES):
                break
            else:
                print(f"TOCADO!! {player_comp.name.upper()} DISPARA DE NUEVO\n")
                continue
        else:
            break
    
    if np.sum(player_alb.tablero.tablero == HIT_SIGN) == sum(BOAT_SIZES):
        print(f"FIN DEL JUEGO. {player_comp.name.upper()} GANA")
        break







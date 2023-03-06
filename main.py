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
    player_alb.shoot(player_comp)
    if player_comp.finished:
        print(f"FIN DEL JUEGO. {player_alb.name.upper()} GANA")
        break

    player_comp.shoot(player_alb)
    if player_alb.finished:
        print(f"FIN DEL JUEGO. {player_comp.name.upper()} GANA")
        break







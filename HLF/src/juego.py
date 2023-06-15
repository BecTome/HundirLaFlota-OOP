from HLF.src.tablero import Tablero
from HLF.src.player import Player, Computer
from HLF.utils.config import BOARD_SIZE

class Juego:
    def __init__(self, player_name, computer_name):
        self.tab_jugador = Tablero(BOARD_SIZE)
        self.tab_comp = Tablero(BOARD_SIZE)

        self.player_alb = Player(player_name, self.tab_jugador)
        self.player_comp = Computer(computer_name, self.tab_comp)

        print(self.player_alb)
        print(self.player_comp)
        pass



    def start(self):
        while True:
            self.player_alb.shoot(self.player_comp)
            if self.player_comp.finished:
                print(f"FIN DEL JUEGO. {self.player_alb.name.upper()} GANA")
                break

            self.player_comp.shoot(self.player_alb)
            if self.player_alb.finished:
                print(f"FIN DEL JUEGO. {self.player_comp.name.upper()} GANA")
                break
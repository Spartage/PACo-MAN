import sys

##Para poder importar las cosas del folder principal
sys.path.insert(1, 'C:/Users/Administrador/Desktop/Trabajos/LP/Proyecto')

import Level
from Auxiliar import*

class Level3(Level.Level):
    def __init__(self):
        super().__init__()

    def getLayout(self):
        return [[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9 ,9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9 ,9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
[9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
[9, 1, 1, 0, 0, 3, 0, 0, 1, 1, 1 ,1, 1, 0, 0, 3, 0, 0, 1, 1, 9],
[9, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1 ,1, 0, 0, 1, 1, 1, 0, 0, 1, 9],
[9, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1 ,1, 0, 1, 1, 0, 1, 1, 0, 1, 9],
[9, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1 ,1, 0, 0, 0, 0, 0, 0, 0, 1, 9],
[9, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1 ,1, 0, 1, 1, 0, 1, 1, 0, 1, 9],
[9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
[9, 1, 1, 0, 1, 1, 1, 0, 1, 0, 6, 0, 1, 0, 1, 1, 1, 0, 1, 1, 9],
[9, 1, 1, 0, 0, 0, 0, 0, 1, 4, 1, 4, 1, 0, 0, 0, 0, 0, 1, 1, 9],
[9, 1, 1, 1, 1, 0, 1, 1, 1, 7, 5, 8, 1, 1, 1, 0, 1, 1, 1, 1, 9],
[9, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 9],
[9, 1, 1, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 1, 1, 9],
[9, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 9],
[9, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],
[9, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 9],
[9, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 9],
[9, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 9],
[9, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 9],
[9, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 9],
[9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 9],
[9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9]]

    ##Usamos una matriz y los numeros son los objetos que esta puede usar

    def getSprites(self):
        comida, rect = load_image('comida.png', -1)
        bloque, rect = load_image('block.png', -1)
        paco, rect = load_image('pac_right.png', -1)
        super_comida, rect = load_image('super_comida.png', -1)
        gwall, rect = load_image('gwall.png', -1)
        capucha0, rect = load_image('ghost0.png', -1)
        capucha1, rect = load_image ('ghost2.png', -1)
        capucha2, rect = load_image('ghost3.png', -1)
        capucha3, rect = load_image ('ghost1.png', -1)

        return [comida ,bloque, paco, super_comida, gwall, capucha0, capucha1, capucha2, capucha3]
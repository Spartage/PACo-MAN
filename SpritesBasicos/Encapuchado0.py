import sys

##Para poder importar las cosas del folder principal
sys.path.insert(1, 'C:/Users/Administrador/Desktop/Trabajos/LP/Proyecto')

import pygame
import Sprites
import random
from math import inf 
from Auxiliar import dist

from pygame.locals import*


# Encapuchado Random (CELESTE)

class Encapuchado0(Sprites.Spri):
    def __init__(self, centro, imagen, muerto_image, scared_image = None):
        super().__init__(centro, imagen)
        self.original_pos = centro
        self.normal_image = imagen
        self.muerto_image = muerto_image
        if scared_image != None:
            self.scared_image = scared_image
        else:
            self.scared_image = imagen
        self.dir = 0
        self.blink = False
        self.parpadear = False


    # Getters y setters

    def getScared(self):
        return self.scared

    def getPos(self):
        return [self.rect.centerx, self.rect.centery]
            
    # Un algoritmo para buscar la coordenada que busca el ghost
    # al igual que en el juego original

    def findTarget(self, paco, ghost1, estado):
        if self.muerto == True:
            return self.original_pos

        if estado == "Chase":
            PacOffset = (paco.getPos()[0] + self.sDir(self.dir, "x") * self.movement * 2, paco.getPos()[1] + self.sDir(self.dir, "y") * self.movement * 2)
            inicial = ghost1.getPos()
            target = (PacOffset[0] - inicial[0], PacOffset[1] - inicial[1])
            return [x*2 for x in target]
        elif estado == "Scatter":
            return (504, 552)


    def update(self, block_group, paco, capucha1, estado):
        target = self.findTarget(paco, capucha1, estado)
        self.pathfinding(self.dir, block_group, target)
        self.Parpadeo()
        if self.muerto == True and self.getPos() == self.original_pos:
            self.muerto = False
            self.Scared(False)
        self.dir = self.path.pop()
        xMov = yMov = 0
        if self.dir == 1:
            xMov = -self.SPEED
        elif self.dir == 2:
            xMov = self.SPEED
        elif self.dir == 3:
            yMov = -self.SPEED
        elif self.dir == 4:
            yMov = self.SPEED

        self.rect.move_ip(xMov, yMov)

        if pygame.sprite.spritecollideany(self, block_group):
            self.rect.move_ip(-xMov, -yMov)

    def Scared(self, scared):
        self.scared = scared
        if scared:
            self.image = self.scared_image
        else:
            self.image = self.normal_image

    def Eaten(self): 
        self.muerto = True
        self.image = self.muerto_image

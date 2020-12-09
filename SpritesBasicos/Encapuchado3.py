import sys

##Para poder importar las cosas del folder principal
sys.path.insert(1, 'C:/Users/Administrador/Desktop/Trabajos/LP/Proyecto')

import pygame
import Sprites
from pygame.locals import*
from Auxiliar import dist

# Encapuchado Timido (CLYDE)

class Encapuchado3(Sprites.Spri):
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

    def getScared(self):
        return self.scared

    def getPos(self):
        return [self.rect.centerx,self.rect.centery]

    def findTarget(self, paco):
        if self.muerto == True and self.getPos() == self.original_pos:
            self.muerto = False
            self.Scared(False)
        if self.muerto == True:
            return self.original_pos
        distancia = dist(paco.getPos(), self.getPos()) / 24   #Siendo 24 el tamaño de un bloque
        if distancia > 8:
            return paco.getPos()
        else:
            return (0, 552)

    def update(self, block_group, paco):
        target = self.findTarget(paco)
        self.pathfinding(self.dir, block_group, target)
        self.dir = self.path.pop()
        self.Parpadeo()
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
        if self.scared != scared:
            self.scared = scared
        if scared:
            self.image = self.scared_image
        else:
            self.image = self.normal_image

    def Eaten(self):
        self.muerto = True
        self.image = self.muerto_image
import pygame

import Sprites
import random
from math import inf 
from Auxiliar import dist

from pygame.locals import*

class Spri(pygame.sprite.Sprite):
    def __init__(self, centro, image):
        super().__init__()

        ##Aca seteamos la imagen, el objeto rectangular
        ##y el punto en donde lo pondremos en la pantalla

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = centro
        self.SPEED = 2
        self.recorrido = []
        self.path = []
        self.movement = 24/self.SPEED
        self.scared = False
        self.muerto = False


    def setParpadear(self, valor):
        self.parpadear = valor

    def setMuerto(self, valor):
        self.muerto = valor
        
    def getMuerto(self):
        return self.muerto

    def canMove(self, dir, block_group):
        
        if dir == 1:
            rectTest = self.rect.move ((-self.SPEED, 0))
        elif dir == 2:
            rectTest = self.rect.move ((self.SPEED, 0))
        elif dir == 3:
            rectTest = self.rect.move ((0, -self.SPEED))
        elif dir == 4:
            rectTest = self.rect.move ((0, self.SPEED))

        for block in block_group:
            if rectTest.colliderect(block):
                return False
        return True

    def Parpadeo(self):
        if self.parpadear == True and self.getScared() == True and self.muerto == False:
            if self.blink == False:
                self.image = self.normal_image
                self.blink = True
            else:
                self.image = self.scared_image
                self.blink = False
        else:
            return

    # Simplemente buscamos la direccion contraria
    def reverseDir(self, dir):
        if dir == 1:
            return 2
        elif dir == 2:
            return 1
        elif dir == 3:
            return 4
        elif dir == 4:
            return 3 
        elif dir == 0:
            return 0

    # Retorna la direccion de la speed que hay que tomar segun la direccion original por asi decirlo
    def sDir(self, dir, eje):
        if dir == 0:
            return self.SPEED
        elif dir == 1 and eje == "x":
            return -self.SPEED
        elif dir == 2 and eje == "x":
            return self.SPEED
        elif dir == 3 and eje == "y":
            return -self.SPEED
        elif dir == 4 and eje == "y":
            return self.SPEED
        else:
            return 0


    # Con esto veremos al bloque que se debe mover, segun el target que busca

    # dir = Direccion (1 = a, 2 = d, 3 = w, 4 = s)
    # target =(x, y)
    def pathfinding(self, dir, block_group, target):
        nope = self.reverseDir(dir) # Guardamos la direccion que no debemos tomar
        minDist = inf
        newDir = 0
    
        if self.path == []:
            for i in range(1,5):
                if i != nope:
                    if self.canMove(i, block_group):
                        # Quedo feo porque tuvimos que separarar el getpos en x e y, y multiplicarlo para ver como quedara al moverse
                        # una tile completa
                        if dist((self.getPos()[0] + self.sDir(i, "x") * self.movement, self.getPos()[1] + self.sDir(i, "y") * self.movement), target) <= minDist:
                            minDist = dist(self.getPos(), target)
                            newDir = i
            self.path = [newDir for x in range(8)]


    


                


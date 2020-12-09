import sys

##Para poder importar las cosas del folder principal
sys.path.insert(1, 'C:/Users/Administrador/Desktop/Trabajos/LP/Proyecto')

import pygame
import Sprites
from Auxiliar import load_image


from pygame.locals import*

# Eventos
SUPER_STATE_START = pygame.USEREVENT + 1
SUPER_STATE_OVER = SUPER_STATE_START +1
PACO_MUERTO = SUPER_STATE_OVER + 1
EMERGENCIA = PACO_MUERTO + 1

Score = 0
class Paco(Sprites.Spri):
    def __init__(self, centro, imagen):
        super().__init__(centro, imagen)
        self.leftcomida = 1
        self.SPEED = 3
        self.puntuaciones = [5, 25, 50] # La cantidad de puntos que se darán segun lo que conseguiste, el indice corresponde a los de self.logros
        self.logros = [0, 0, 0] # Lista de la cantidad de cosas que has conseguido, para calcular score [comida, super_comida, monstruos comidos]
        self.pacoR_image, rect = load_image('pac_right.png', -1)
        self.pacoL_image, rect = load_image('pac_left.png', -1)
        self.pacoU_image, rect = load_image('pac_up.png', -1)
        self.pacoD_image, rect = load_image('pac_down.png', -1)
        # Parametros para que no haya que apretar una tecla para que siga moviendose
        # Como en el P-M original
        self.dir = 1 # dir que esta tomando
        self.nextdir = 0 # dir que tomará
        self.xdir = [0, -self.SPEED, self.SPEED, 0, 0] # (0, a, d, w, s)
        self.ydir = [0, 0, 0, -self.SPEED, self.SPEED]


    ## Getters y Setters

    def getLeftComida(self):
        return self.leftcomida

    def getSPEED(self):
        return self.SPEED

    def setSPEED(self, s):
        self.SPEED = s

    def getPos(self):
        return [self.rect.centerx,self.rect.centery]

    def getLogros(self):
        return self.logros

    def getPuntuaciones(self):
        return self.puntuaciones
    
    def resetLogros(self):
        self.logros = [0, 0, 0]


    # Movimiento al presionar una tecla

    def Press(self, key):
        self.dir = self.nextdir
        if(key == K_w):
            self.nextdir = 3
        elif(key == K_s):
            self.nextdir = 4
        elif(key == K_a):
            self.nextdir = 1
        elif(key == K_d):
            self.nextdir = 2

    def Orientador(self, dir):
        if dir == 1:
            self.image = self.pacoL_image
        elif dir == 2:
            self.image = self.pacoR_image
        elif dir == 3:
            self.image = self.pacoU_image
        elif dir == 4:
            self.image = self.pacoD_image

    ##La forma en que el sprite se updateara
    def update(self, block_group, comida_group, super_comida_group, encapuchado0_group, encapuchado1_group, encapuchado2_group, encapuchado3_group, gwall_group):
        if self.nextdir == 0:
            return
        self.rect.move_ip(self.xdir[self.nextdir],self.ydir[self.nextdir])
        
        self.Orientador(self.nextdir)
        # Colision con una pared
        if pygame.sprite.spritecollide(self, block_group, False) or pygame.sprite.spritecollide(self, gwall_group, False):
            self.rect.move_ip(-self.xdir[self.nextdir],-self.ydir[self.nextdir])
            self.rect.move_ip(self.xdir[self.dir],self.ydir[self.dir])
            self.Orientador(self.dir)
            if pygame.sprite.spritecollide(self, block_group, False) or pygame.sprite.spritecollide(self, gwall_group, False):
                self.rect.move_ip(-self.xdir[self.dir],-self.ydir[self.dir])
                self.dir = self.nextdir = 0
        else:
            self.dir = 0

        L_Encapuchado = pygame.sprite.spritecollide(self, encapuchado0_group, False)
        L_Encapuchado += pygame.sprite.spritecollide(self, encapuchado1_group, False)
        L_Encapuchado += pygame.sprite.spritecollide(self, encapuchado2_group, False)
        L_Encapuchado += pygame.sprite.spritecollide(self, encapuchado3_group, False)
        if (len(L_Encapuchado) > 0):
            self.EncapuchadoCollide(L_Encapuchado)
        else:
            L_Comida = pygame.sprite.spritecollide(self, comida_group, True)
            if (len(L_Comida) > 0):
                self.logros[0] = 1
                self.leftcomida = len(comida_group)
            elif len(L_Comida) == 0:
                self.logros[0] = 0
            if (len(pygame.sprite.spritecollide(self, super_comida_group, True)) > 0):
                self.super = True
                self.logros[1] = 1
                pygame.event.post(pygame.event.Event(SUPER_STATE_START, {}))
                pygame.time.set_timer(SUPER_STATE_OVER, 0)
                pygame.time.set_timer(SUPER_STATE_OVER, 8000)
                pygame.time.set_timer(EMERGENCIA, 0)
                pygame.time.set_timer(EMERGENCIA, 6000)
            if len(pygame.sprite.spritecollide(self, super_comida_group, False)) == 0:
                self.logros[1] = 0

    # Vemos que ocurre si chocamos con un montruo, en el caso de que estaba
    # asustado o no, y si tenemos vidas(aun no implementado esto ultimo)

    def EncapuchadoCollide(self, L_Encapuchado):
        if len(L_Encapuchado) == 0:
            return
        for encapuchado in L_Encapuchado:
            if encapuchado.getScared() == True and encapuchado.getMuerto() == False:
                self.logros[2] = 1
                encapuchado.Eaten()
            elif encapuchado.getScared() == False and encapuchado.getMuerto() == False:
                self.logros[2] = 0
                pygame.event.post(pygame.event.Event(PACO_MUERTO, {}))

        


        
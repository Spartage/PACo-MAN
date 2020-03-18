

class Level:
    def __init__(self):
        #Definimos los valores que tomaran los numeros en la matriz
        self.COMIDA = 0
        self.BLOQUE = 1
        self.PACO = 2
        self.SUPERCOMIDA = 3
        self.GWALL = 4
        self.CAPUCHA0 = 5
        self.CAPUCHA1 = 6
        self.CAPUCHA2 = 7
        self.CAPUCHA3 = 8
    
    def getCOMIDA(self):
        return self.COMIDA

    def getBLOQUE(self):
        return self.BLOQUE

    def getPACO(self):
        return self.PACO
    
    def getCAPUCHA0(self):
        return self.CAPUCHA0

    def getCAPUCHA1(self):
        return self.CAPUCHA1

    def getCAPUCHA2(self):
        return self.CAPUCHA2

    def getCAPUCHA3(self):
        return self.CAPUCHA3

    def getSUPERCOMIDA(self):
        return self.SUPERCOMIDA

    def getGWALL(self):
        return self.GWALL

    ##Deberia retornar la matriz con la forma del nivel
    def getLayout(self):
        pass

    ##Aca retornamos una lista con las imagenes que usaremos
    ##(Las correspondientes a los números en el layout)
    def getImages(self):
        pass


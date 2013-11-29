# coding: latin-1 

from lib import Object,ObjectEixo,ObjectFicha,BaseMain,ObjectEvent,Animation,GameState,Text,Music
import pygame
from random import Random
from math import sin,tan,radians,sqrt



class DrawVector:
    def __init__(self,lista,tela):
        for i in range(len(lista)):
            try:lista[i].draw(tela)
            except: 
                for a in range(4):
                    lista[i][a].draw(tela)
            pass
        pass
    pass


class Actions:
    
    def __init__(self,faseBD,state,limitState = 1):
        self.faseBD = faseBD
        self.firstMotion = None
        self.canFirstMotion = True
                
        self.firstClick = None
        self.canFirstClick = True
        
        self.state= state
        self.limitState = limitState
        pass
    
    def event(self,event,time):
        
        if not pygame.event.get() == [] and self.canFirstMotion:
            self.firstMotion = time
            self.canFirstMotion = False
    
        if event.type == pygame.MOUSEBUTTONUP and self.canFirstClick:
            self.firstClick = time
            self.canFirstClick = False
        pass
    
    
    def update(self,ficha,eixoL,eixoR):
        
        if self.state < self.limitState :
            for k in ficha:
                if k.plugged:
                    self.state = 1
                  
        
        #Outros
        '''
        for f in ficha:
            if f.state== "Clicking":
                #self.faseBD.append("Nome: "+f.name + "// Peso:"+ str(f.peso)+ "// Coleção: "+f.colection + "// Tipo:"+ f.type+ "--> Esta foi clicado  )            
        pass
        '''
    

class Balance:
   
    posBase = 0        
    
    def settingNewPosition(self,eixoLFinal,eixoRFinal,vas):
        
        if not Vassoura.stateRotation == Vassoura.oldstateRotation:
 
            for k in range(4):
                for i in range(len(eixoLFinal)):                
                    eixoLFinal[i][k].rect.x = vas.rect.x+26+15*(i)
                    eixoLFinal[i][k].rect.y = vas.rect.y+vas.image.get_height()+k*20
                    
                for i in range(len(eixoRFinal)):
                    eixoRFinal[i][k].rect.x = eixoLFinal[len(eixoLFinal)-1][0].rect.x+15*2+i*15
                    eixoRFinal[i][k].rect.y = vas.rect.y+vas.image.get_height()+k*20
                    
            
        Balance.posBase = eixoLFinal[len(eixoLFinal)-1][0].rect.x+16
            
        
        return [eixoLFinal,eixoRFinal]


    def setCenter(self,vas,eixoL,eixoR,setWeight = True):
        Vassoura.oldstateRotation = Vassoura.stateRotation
        Vassoura.stateRotation = 'Center'
        eixoTotal = []
        eixoLFinal=[]
        eixoRFinal= []
        
        for i in eixoL:
            eixoTotal.append(i)
        for i in eixoR:
            eixoTotal.append(i)

        for i in range(len(eixoTotal)):
            
            if i <= 25:
                eixoLFinal.append(eixoTotal[i])
            if i > 25:
                eixoRFinal.append(eixoTotal[i])
        
        if setWeight:
            self.settingNewPosition(eixoLFinal, eixoRFinal, vas)
            
        return eixoLFinal,eixoRFinal
    

    def setRight(self,vas,eixoL,eixoR,setWeight = True):
        Vassoura.oldstateRotation = Vassoura.stateRotation
        Vassoura.stateRotation = 'Right'
                
        eixoTotal = []
        eixoLFinal=[]
        eixoRFinal= []
        
        for i in eixoL:
            eixoTotal.append(i)

        for i in eixoR:
            eixoTotal.append(i)

        

        for i in range(len(eixoTotal)):
            if i <= 38:
                eixoLFinal.append(eixoTotal[i])
            if i > 38:
                eixoRFinal.append(eixoTotal[i])
        
        if setWeight:
            self.settingNewPosition(eixoLFinal, eixoRFinal, vas)
        
        return eixoLFinal,eixoRFinal
    

    def setLeft(self,vas,eixoL,eixoR,setWeight = True):
        Vassoura.oldstateRotation = Vassoura.stateRotation
        Vassoura.stateRotation = 'Left'
        
        eixoTotal = []
        eixoLFinal=[]
        eixoRFinal= []
        

        for i in eixoL:
            eixoTotal.append(i)

        for i in eixoR:
            eixoTotal.append(i)

        

        for i in range(len(eixoTotal)):
            if i <= 12:
                eixoLFinal.append(eixoTotal[i])
            if i > 12 and i < len(eixoTotal):
                eixoRFinal.append(eixoTotal[i])
                    
        if setWeight:
            self.settingNewPosition(eixoLFinal, eixoRFinal, vas)
            
        return eixoLFinal,eixoRFinal
    

    def __init__(self,balance = False):

        self.Draweixos = balance
        self.stickBroomLeft = 100
        self.stickBroomRight = 100
        
        pass

    def draw(self,tela,eixoL,eixoR):

        if self.Draweixos:
            DrawVector(eixoL, tela)
            DrawVector(eixoR, tela)

        pass


class Vassoura:
    
    
    stateRotation = ''
    oldstateRotation = 'Null'
    
    def onClickVas(self):
        self.angle = 0
        pass

        
    def __init__(self,faseCur='Fase1',onClickVas=None):

        self.faseCur = faseCur

        self.angle = 0
        self.MAXangle = 10
        self.MINangle = -10
        ''
        if faseCur == 'Fase8':            
            self.MAXangle = 10
            self.MINangle = -10
            pass
        ''
        self.rotationMode = True
 
        self.posVassoura = [7,328]

        src = "src/Fases/Fase1/0.png"

        self.rand = Random()
        
        self.acrescimoDeLargura=0
        
        if faseCur == "Fase4":
            self.posVassoura = [50,380]
            src = "src/Fases/Fase4/0.png" 
            self.acrescimoDeLargura=0           

        if faseCur == "Fase8":
            #self.posVassoura = [82,350]
            self.posVassoura = [82,294]
            src = "src/Fases/Fase8/0.png"
            #src = "src/Fases/Fase4/0.png" 
            #self.acrescimoDeLargura = 30


        self.rotationMode = True
        
        if onClickVas:
            onClickVas = self.onClickVas
            
        self.vas = ObjectEvent((self.posVassoura[0],self.posVassoura[1]),src,None,None,onClickVas)

        #self.objectNull = Object("src/Fases/Fichas/eixo.png")

    def draw(self,tela):
        self.vas.draw(tela)
        #self.objectNull.rect.x,self.objectNull.rect.y=self.vas.rect.center
        #self.objectNull.draw(tela)
        #print self.objectNull.rect.x
        pass

    def event (self,event):

        if event.type == pygame.MOUSEMOTION:
            self.vas.update(pygame.mouse.get_pos())

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.vas.clickStart(pygame.mouse.get_pos())

        if event.type == pygame.MOUSEBUTTONUP:
            if self.vas.clickEnd(pygame.mouse.get_pos()):
                return
            pass
        pass


        pass

    def update(self,ficha,base,dt):
        
        if self.angle > self.MAXangle:
            if ficha.resultWeigth != 0:
                self.angle = self.MAXangle
        if self.angle < self.MINangle:
            if ficha.resultWeigth != 0:
                self.angle = self.MINangle
        
        pointRotation = ficha.eixosLeft[0][0].image.get_width()*38
        #pointRotation = base.rect.x-self.vas.image.get_width()/2
        
        self.vas.rotate(self.angle)
        if Vassoura.stateRotation == "Right":
            self.vas.rotate(self.angle)
            self.vas.rotateRight(self.angle, self.MAXangle,self.MINangle,pointRotation)
        elif Vassoura.stateRotation == "Left":
            self.vas.rotateLeft(self.angle, self.MAXangle,self.MINangle,pointRotation)



class Fichas:
    

    def reset(self):

        for i in self.objectFichas:
            i.rect.x, i.rect.y = i.oldPos
        pass


    def reverse(self,vector,pos):

        self.posFinal = len(vector)+1
        for i in range(self.posFinal):

            if i == pos:
                return self.posFinal

            self.posFinal-=1

    def setWeigth (self,vector,positionVector,peso,reverse = False):

        self.pos = positionVector
        self.pos+=1

        if vector[positionVector][0] == 0:
            if reverse:
                self.pos = self.reverse(vector, self.pos)
            vector[positionVector][0] += peso*self.pos

        return vector

    def numberWeigth(self,weigth,number):

        if number > 0:
            if weigth >= 0 :
               x = 1*number

            if weigth >= 62:
               x = 2*number

            if weigth >= 122:
               x = 3*number
        if number < 0:
            if weigth < 0:
               x =  1*number

            if weigth <= -62 :
                x =  2*number

            if weigth <= -122:
                x = 3*number
        return x

        pass

    def takePosEixos(self,weigth,base=None):


        if weigth > 0 and self.vas.angle < 22:
            speed = self.numberWeigth(weigth, 1)


        if weigth < 0 and self.vas.angle > -22:
            speed = self.numberWeigth(weigth, -1)

        if weigth == 0 :

            if self.vas.angle > 0:
                speed = 1
                pass
            if self.vas.angle < 0:
                speed = -1
                pass
            if self.vas.angle == 0:
                speed = 0
                pass

            pass

        self.vas.angle += -speed

        if self.vas.angle > self.vas.MAXangle:
            if weigth != 0:
                self.vas.angle = self.vas.MAXangle
        if self.vas.angle < self.vas.MINangle:
            if weigth != 0:
                self.vas.angle = self.vas.MINangle

        
        angle = self.vas.angle 
        
        if not self.vas.angle == 0:
            if self.vas.angle <0:
                angle = self.vas.angle
            if self.vas.angle >0:
                angle = self.vas.angle
           
        #if weigth == 0 and self.vas.angle == 1 or self.vas.angle ==-1:
        #    angle = 0
        #    self.vas.vas.image = self.vas.vas.oldIdle

            
        for a in range(4):
            for i in range(len(self.eixosLeft)):
                
                if self.rotate:
                            
                        #raio = self.vas.vas.rect.x - (self.vas.vas.rect.x + 26+len(self.eixosLeft)-1-i*15)
                        raio = (self.vas.vas.rect.x + self.vas.vas.image.get_width()/2)-self.eixosLeft[i][0].rect.x
                                
                        if Vassoura.stateRotation == 'Left' and self.base is not None:                         
                            raio = self.base.rect.x-self.eixosLeft[i][0].rect.x 
                        elif Vassoura.stateRotation == 'Right'and self.base is not None:
                            raio = self.base.rect.x - self.eixosLeft[i][0].rect.x                        
                        

                        y = sin(radians(angle))*raio
                        x = tan(radians(angle))*y
    
                        if self.vas.angle > 0:
                            #self.eixosLeft[len(self.eixosLeft)-1-i][a].rect.y = self.eixosLeft[len(self.eixosLeft)-1-i][a].oldPos[1] + y
                            self.eixosLeft[i][a].rect.y = self.eixosLeft[i][a].oldPos[1] + y
                            pass
    
                        if self.vas.angle < 0:
    
                            #self.eixosLeft[len(self.eixosLeft)-1-i][a].rect.y = self.eixosLeft[len(self.eixosLeft)-1-i][a].oldPos[1] + y
                            self.eixosLeft[i][a].rect.y = self.eixosLeft[i][a].oldPos[1] + y
                            pass
    
                        if self.vas.angle == 0:
                            self.eixosLeft[i][a].rect.y = self.eixosLeft[i][a].oldPos[1]
                                

                self.speed = 0
                pass
            
            for i in range(len(self.eixosRight)):
                
                if self.rotate:
         
                        raio = self.eixosRight[i][0].rect.x - (self.vas.vas.rect.x + self.vas.vas.image.get_width()/2)
         
                        if Vassoura.stateRotation == 'Left'and self.base is not None:
                            raio = self.vas.vas.rect.x - (self.vas.vas.rect.x +26+ 15*i)                            
                        elif Vassoura.stateRotation == 'Right'and self.base is not None:
                            raio = self.eixosRight[i][0].rect.x - self.base.rect.x
                        
                        
                        if raio < 0:
                            raio *=-1
                                
                        y = sin(radians(angle))*raio
                        x = tan(radians(angle))*y
    
                        if self.vas.angle > 0:
    
                            self.eixosRight[i][a].rect.y = self.eixosRight[i][a].oldPos[1] - y
                            pass
    
                        if self.vas.angle < 0:
    
                            self.eixosRight[i][a].rect.y = self.eixosRight[i][a].oldPos[1] - y
                            pass
    
                        if self.vas.angle == 0:
                            self.eixosRight[i][a].rect.y = self.eixosRight[i][a].oldPos[1]
    
                
                self.speed = 0
                
                pass
    
            #print self.vas.angle,weigth
            
            pass
        

    
        

                             


    def __init__(self,faseCur = '',vas = None,objects = None,base = None):

        self.objectMain = objects

        self.vas = vas
        self.base = base

        self.faseCur = faseCur
        
        if faseCur == "Fase1" or faseCur == "Fase8":
            self.rotate = True
        else :
            self.rotate = False    

        self.rand = Random()

        self.speed = 0

        self.objectFichas = []

        self.eixosLeft = []
        self.eixosRight = []

        self.XFirst,self.YFirst = 180-27,19 
        self.oldOBX = self.initPositionObjectsX = 180-27
        self.oldOBY = self.initPositionObjectsY = 64

        self.eixo = pygame.image.load("src/Fases/Fichas/eixo.png").convert_alpha()

        self.initPositionEixoLeftX = 111
        
        self.initPositionEixoY = self.vas.vas.rect.y+self.vas.vas.image.get_height()
        
        self.initPositionEixoRigthX = self.initPositionEixoLeftX + (27 * 15)
        
        self.nameFichas = []
        self.srcFichas = []
        
        
        self.stickBroomLeft,self.stickBroomRight = 100,100
        self.weightLeft = []
        self.weightRight = []
        self.weightLeftPlugged = []
        self.weightRightPlugged = []
        self.orderFichas = []
        self.attributes = []
        #or faseCur == "Fase8"
        if faseCur == "Fase1" :
            self.initPositionEixoY -=21
        
        self.nameFichas = ('Ficha da teia da aranha',
                            'Ficha da casca do caracol',
                            'Ficha da tromba do elefante',
                            'Ficha da crista do galo',
                            'Ficha do rabo do macaco ',
                            'Ficha do bico do papagaio',
                            'Ficha das orelhas do rato',
                            'Ficha da ubere',
                            'Ficha do abacaxi',
                            'Ficha da macieira',
                            'Ficha da bananeira',
                            'Ficha do bolo',
                            'Ficha da casa',
                            'Ficha do moinho',                            
                            'Ficha do indio',                            
                            'Ficha da camera',
                            'Ficha do piano',
                            'Ficha do pirata',                            
                            'Ficha da coroa do abacaxi',
                            'Ficha da maï¿½ï¿½',                            
                            'Ficha da banana',
                            'Ficha das velas do bolo',
                            'Ficha do telhado da casa',
                            'Ficha das pï¿½s do catavento',
                            'Ficha do cocar',                            
                            'Ficha da fotografia',
                            'Ficha da partitura',
                            'Ficha do chapï¿½u',                            
                            'Ficha da cesta do balï¿½o',
                            'Ficha da betoneira',
                            'Ficha da hï¿½lice',
                            'Ficha do guidon',
                            'Ficha do capacete',
                            'Ficha da roda grande',
                            'Ficha dos trilhos',                            
                            'Ficha da bandeirola do triciclo',                            
                            'Ficha da teia da aranha',
                            'Ficha da casca do caracol',
                            'Ficha da tromba do elefante',
                            'Ficha da crista do galo',                            
                            'Ficha do rabo do macaco',
                            'Ficha do bico do papagaio',
                            'Ficha das orelhas do rato',
                            'Ficha da ubere',                            
                            'Ficha das velas do bolo',
                            'Ficha do telhado da casa',
                            'Ficha das pï¿½s do catavento',
                            'Ficha do cocar',
                            'Ficha da fotografia',
                            'Ficha da partitura',
                            'Ficha do chapï¿½u',
                            'Ficha da coroa do abacaxi',
                            'Ficha da maï¿½ï¿½',
                            'Ficha da banana',                            
                            'Ficha do Balï¿½o',                            
                            'Ficha da Betoneira',                            
                            'Ficha do helicï¿½ptero',
                            'Ficha do jet-ski',
                            'Ficha do motoqueiro',
                            'Ficha do trator',                            
                            'Ficha do trem',
                            'Ficha do Triciclo',                            
                            'Ficha da cesta do balï¿½o',
                            'Ficha da betoneira',
                            'Ficha da hï¿½lice',
                            'Ficha do guidon',
                            'Ficha do capacete',
                            'Ficha da roda grande',
                            'Ficha dos trilhos',
                            'Ficha da bandeirola do triciclo',                            
                            'Ficha da Aranha',
                            'Ficha do Caracol',                            
                            'Ficha do Elefante',
                            'Ficha do Galo',
                            'Ficha do Macaco ',
                            'Ficha do Papagaio',
                            'Ficha do Rato',
                            'Ficha da vaca',                            
                            'Ficha da teia da aranha',
                            'Ficha da casca do caracol',                            
                            'Ficha da tromba do elefante',
                            'Ficha da crista do galo',
                            'Ficha do rabo do macaco ',
                            'Ficha do bico do papagaio',
                            'Ficha das orelhas do rato',
                            'Ficha da ubere',                            
                            'Ficha da coroa do abacaxi',
                            'Ficha da maï¿½ï¿½',
                            'Ficha da banana',
                            'Ficha das velas do bolo',
                            'Ficha do telhado da casa',
                            'Ficha das pï¿½s do catavento',
                            'Ficha do cocar',                            
                            'Ficha da fotografia',
                            'Ficha da partitura',
                            'Ficha do chapï¿½u',                            
                            'Ficha da cesta do balï¿½o',
                            'Ficha da betoneira',
                            'Ficha da hï¿½lice',
                            'Ficha do guidon',                            
                            'Ficha do capacete',
                            'Ficha da roda grande',
                            'Ficha dos trilhos',
                            'Ficha da bandeirola do triciclo')
        
        
        
        

        
        
        for i in range(1,105):

            

            if i <= 36:
                peso = 1
                if i <= 8:
                    colection = "Animais"
                    type = 'Partes todo'
                    
                elif i > 8 and i <= 28:
                    colection = "Miscelania"
                    if i < 19:                        
                        type = 'Figuras todo'
                    if i > 18:
                        type = 'Partes todo'     
                                
                elif i > 28 and i <= 36:
                    colection = "Transportes"
                    type = 'Partes todo'
                    
                    
                pass

            if i > 36 and i <= 70 :
                peso = 2
                if i > 36 and i <= 44:
                    colection = "Animais"
                    type = 'Partes todo'
                    
                elif i > 44 and i <= 54:
                    colection = "Miscelania"
                    type = 'Partes todo'
                    
                elif i > 54:
                    colection = "Transportes"
                    if i < 63:
                        type = 'Figuras todo'
                    if i > 62:    
                        type = 'Partes todo'                    
                pass

            if i > 70 :
                peso = 3
                if i > 70 and i <= 86:
                    colection = "Animais"
                    if i < 79:
                        type = 'Figuras todo'                    
                    if i > 78:
                        type = 'Partes todo'
                                            
                elif i > 86 and i <= 96:
                    colection = "Miscelania"
                    type = 'Partes todo'
                    
                elif i > 96:
                    colection = "Transportes"
                    type = 'Partes todo'
                pass
            
     
            
            self.srcFichas.append(["src/Fases/Fichas/PESO "+str(peso)+"/"+colection+"/"+type+"/"+str(i)+"-idle.png" ,
                              "src/Fases/Fichas/PESO "+str(peso)+"/"+colection+"/"+type+"/"+str(i)+"-hover.png",
                              "src/Fases/Fichas/PESO "+str(peso)+"/"+colection+"/"+type+"/"+str(i)+"-click.png"])
            
            self.attributes.append([peso,colection,type])
            pass

       
        
        for a in range(len(self.nameFichas)):                    
                if self.nameFichas[a].find('abacaxi') != -1:
                    self.orderFichas.append(a)              
            
        for a in range(len(self.nameFichas)):  
                if self.nameFichas[a].find("macieira") != -1:
                    self.orderFichas.append(a)
                if self.nameFichas[a].find("maï¿½ï¿½") != -1:
                    self.orderFichas.append(a)    
            
        for a in range(len(self.nameFichas)):  
                if self.nameFichas[a].find("bananeira") != -1:
                    self.orderFichas.append(a)
                if self.nameFichas[a].find("banana") != -1:
                    self.orderFichas.append(a)
                    
        for a in range(len(self.nameFichas)):  
                if self.nameFichas[a].find("bolo") != -1:
                    self.orderFichas.append(a)
                    
        for a in range(len(self.nameFichas)):  
                if self.nameFichas[a].find("casa") != -1:
                    self.orderFichas.append(a)
                    
        for a in range(len(self.nameFichas)):  
                if self.nameFichas[a].find("moinho") != -1:
                    self.orderFichas.append(a)
                if self.nameFichas[a].find("catavento") != -1:
                    self.orderFichas.append(a)                
                    
        for a in range(len(self.nameFichas)):  
                if self.nameFichas[a].find("indio") != -1:
                    self.orderFichas.append(a)
                if self.nameFichas[a].find("cocar") != -1:
                    self.orderFichas.append(a)
                    
        for a in range(len(self.nameFichas)):  
                if self.nameFichas[a].find("camera") != -1:
                    self.orderFichas.append(a)
                if self.nameFichas[a].find("fotografia") != -1:
                    self.orderFichas.append(a)
                    
        for a in range(len(self.nameFichas)):  
                if self.nameFichas[a].find("piano") != -1:
                    self.orderFichas.append(a)
                if self.nameFichas[a].find("partitura") != -1:
                    self.orderFichas.append(a)
                    
        for a in range(len(self.nameFichas)):  
                if self.nameFichas[a].find("pirata") != -1:
                    self.orderFichas.append(a)
                if self.nameFichas[a].find("chapï¿½u") != -1:
                    self.orderFichas.append(a)
                    
        for a in range(len(self.nameFichas)):  
                if self.nameFichas[a].find("Balï¿½o") != -1:
                    self.orderFichas.append(a)
        for a in range(len(self.nameFichas)):  
                if self.nameFichas[a].find("cesta") != -1:
                    self.orderFichas.append(a)
                    
        for a in range(len(self.nameFichas)):  
                if self.nameFichas[a].find("Betoneira") != -1:
                    self.orderFichas.append(a)
        for a in range(len(self.nameFichas)):  
                if self.nameFichas[a].find("betoneira") != -1:
                    self.orderFichas.append(a)
                    
        for a in range(len(self.nameFichas)):  
                if self.nameFichas[a].find("helicï¿½ptero") != -1:
                    self.orderFichas.append(a)
        for a in range(len(self.nameFichas)):
                if self.nameFichas[a].find("hï¿½lice") != -1:
                    self.orderFichas.append(a)
                    
        for a in range(len(self.nameFichas)):  
                if self.nameFichas[a].find("jet-ski") != -1:
                    self.orderFichas.append(a)
        for a in range(len(self.nameFichas)):
                if self.nameFichas[a].find("guidon") != -1:
                    self.orderFichas.append(a)
                                                    
        for a in range(len(self.nameFichas)):  
                if self.nameFichas[a].find("motoqueiro") != -1:
                    self.orderFichas.append(a)
        for a in range(len(self.nameFichas)):
                if self.nameFichas[a].find("capacete") != -1:
                    self.orderFichas.append(a)
                    
        for a in range(len(self.nameFichas)):  
                if self.nameFichas[a].find("trator") != -1:
                    self.orderFichas.append(a)
        for a in range(len(self.nameFichas)):
                if self.nameFichas[a].find("roda grande") != -1:
                    self.orderFichas.append(a)
                    
        for a in range(len(self.nameFichas)):  
                if self.nameFichas[a].find("trem") != -1:
                    self.orderFichas.append(a)
        for a in range(len(self.nameFichas)):
                if self.nameFichas[a].find("trilhos") != -1:
                    self.orderFichas.append(a)
                    
        for a in range(len(self.nameFichas)):  
                if self.nameFichas[a].find("Triciclo") != -1:
                    self.orderFichas.append(a)  
        for a in range(len(self.nameFichas)):  
                if self.nameFichas[a].find("bandeirola") != -1:
                    self.orderFichas.append(a)                
                    
        for a in range(len(self.nameFichas)):  
                if self.nameFichas[a].find("Aranha") != -1:
                    self.orderFichas.append(a)
        for a in range(len(self.nameFichas)):  
                if self.nameFichas[a].find("teia") != -1:
                    self.orderFichas.append(a)
                    
        for a in range(len(self.nameFichas)):  
                if self.nameFichas[a].find("Caracol") != -1:
                    self.orderFichas.append(a)
        for a in range(len(self.nameFichas)):  
                if self.nameFichas[a].find("casca") != -1:
                    self.orderFichas.append(a)
                    
        for a in range(len(self.nameFichas)):  
                if self.nameFichas[a].find("Elefante") != -1:
                    self.orderFichas.append(a)
        for a in range(len(self.nameFichas)):  
                if self.nameFichas[a].find("tromba") != -1:
                    self.orderFichas.append(a)
                    
        for a in range(len(self.nameFichas)):  
                if self.nameFichas[a].find("Galo") != -1:
                    self.orderFichas.append(a)
        for a in range(len(self.nameFichas)):  
                if self.nameFichas[a].find("crista") != -1:
                    self.orderFichas.append(a)
                    
        for a in range(len(self.nameFichas)):  
                if self.nameFichas[a].find("Macaco") != -1:
                    self.orderFichas.append(a)
        for a in range(len(self.nameFichas)):  
                if self.nameFichas[a].find("rabo do macaco") != -1:
                    self.orderFichas.append(a)
                    
        for a in range(len(self.nameFichas)):  
                if self.nameFichas[a].find("Papagaio") != -1:
                    self.orderFichas.append(a)
        for a in range(len(self.nameFichas)):  
                if self.nameFichas[a].find("bico") != -1:
                    self.orderFichas.append(a)
                                
        for a in range(len(self.nameFichas)):  
                if self.nameFichas[a].find("Rato") != -1:
                    self.orderFichas.append(a)
        for a in range(len(self.nameFichas)):  
                if self.nameFichas[a].find("orelhas") != -1:
                    self.orderFichas.append(a)
                    
        for a in range(len(self.nameFichas)):  
                if self.nameFichas[a].find("vaca") != -1:
                    self.orderFichas.append(a)
        for a in range(len(self.nameFichas)):
                if self.nameFichas[a].find("ubere") != -1:
                    self.orderFichas.append(a)
                
                
                            
            
            
        for i in range(len(self.orderFichas)):
            
            
            if self.initPositionObjectsY >= (self.oldOBY+(45*4)):
                self.initPositionObjectsY = self.oldOBY
                self.initPositionObjectsX += 27
                pass
            
            x,y = self.initPositionObjectsX,self.initPositionObjectsY-44
            
            x = self.initPositionObjectsX
            self.initPositionObjectsY += 45
            
            self.objectFichas.append(ObjectFicha([x,y],self.srcFichas[self.orderFichas[i]][0],
                                                 self.srcFichas[self.orderFichas[i]][1],
                                                 self.srcFichas[self.orderFichas[i]][2],
                                                 self.attributes[self.orderFichas[i]][0],
                                                 self.attributes[self.orderFichas[i]][1],
                                                 self.attributes[self.orderFichas[i]][2],
                                                 self.nameFichas[self.orderFichas[i]]))
            
            
            pass
            
        
        
        for i in range(26):

                #====EIXOS
                aux = 20
                self.eixosLeft.append([ObjectEixo(self.eixo, self.initPositionEixoLeftX,self.initPositionEixoY),
                                      ObjectEixo(self.eixo, self.initPositionEixoLeftX,self.initPositionEixoY+aux),
                                      ObjectEixo(self.eixo, self.initPositionEixoLeftX,self.initPositionEixoY+aux*2),
                                      ObjectEixo(self.eixo, self.initPositionEixoLeftX,self.initPositionEixoY+aux*3)])
                '''
                self.eixosRight.append([ObjectEixo(self.eixo, self.initPositionEixoRigthX,self.initPositionEixoY),
                                       ObjectEixo(self.eixo, self.initPositionEixoRigthX,self.initPositionEixoY+aux),
                                       ObjectEixo(self.eixo, self.initPositionEixoRigthX,self.initPositionEixoY+aux*2),
                                       ObjectEixo(self.eixo, self.initPositionEixoRigthX,self.initPositionEixoY+aux*3)])
                '''
                self.eixosRight.append([ObjectEixo(self.eixo, self.initPositionEixoRigthX,self.initPositionEixoY),
                                       ObjectEixo(self.eixo, self.initPositionEixoRigthX,self.initPositionEixoY+aux),
                                       ObjectEixo(self.eixo, self.initPositionEixoRigthX,self.initPositionEixoY+aux*2),
                                       ObjectEixo(self.eixo, self.initPositionEixoRigthX,self.initPositionEixoY+aux*3)])
                
                self.initPositionEixoLeftX += 15
                self.initPositionEixoRigthX += 15

                self.weightLeft.append([0,0,0,0])
                self.weightRight.append([0,0,0,0])
                
                self.weightLeftPlugged.append([False,False,False,False])
                self.weightRightPlugged.append([False,False,False,False])
                
                self.eixosLeft[i][0].enable = True
                self.eixosRight[i][0].enable = True
                
                pass
         
        tempVector = []
        
        for i in self.objectFichas:
            tempVector.append(i)
        
        
            
        self.objectFichas[0].rect.x = tempVector[48].oldPos[0]
        self.objectFichas[4].rect.x = tempVector[20].oldPos[0]     
        self.objectFichas[8].rect.x = tempVector[4].oldPos[0]
        self.objectFichas[12].rect.x = tempVector[100].oldPos[0]
        self.objectFichas[16].rect.x = tempVector[72].oldPos[0]
        self.objectFichas[20].rect.x = tempVector[80].oldPos[0]
        self.objectFichas[24].rect.x = tempVector[76].oldPos[0]
        self.objectFichas[28].rect.x = tempVector[16].oldPos[0]
        self.objectFichas[32].rect.x = tempVector[40].oldPos[0]
        self.objectFichas[36].rect.x = tempVector[8].oldPos[0]
        self.objectFichas[40].rect.x = tempVector[0].oldPos[0]
        self.objectFichas[44].rect.x = tempVector[92].oldPos[0]
        self.objectFichas[48].rect.x = tempVector[44].oldPos[0]
        self.objectFichas[52].rect.x = tempVector[68].oldPos[0]
        self.objectFichas[56].rect.x = tempVector[96].oldPos[0]
        self.objectFichas[60].rect.x = tempVector[12].oldPos[0]
        self.objectFichas[64].rect.x = tempVector[60].oldPos[0]
        self.objectFichas[68].rect.x = tempVector[28].oldPos[0]
        self.objectFichas[72].rect.x = tempVector[52].oldPos[0]
        self.objectFichas[76].rect.x = tempVector[24].oldPos[0]
        self.objectFichas[80].rect.x= tempVector[32].oldPos[0]
        self.objectFichas[84].rect.x = tempVector[88].oldPos[0]
        self.objectFichas[88].rect.x = tempVector[56].oldPos[0]
        self.objectFichas[92].rect.x = tempVector[36].oldPos[0]
        self.objectFichas[96].rect.x = tempVector[84].oldPos[0]
        self.objectFichas[100].rect.x = tempVector[64].oldPos[0]
  
        
        for i in self.objectFichas:
            i.oldPos = i.rect.x,i.rect.y
        
        
        if faseCur == "Fase4":

            if objects is not None:

                for i in range(len(self.objectFichas)):

                    x = 200

                    if i <= 8:
                        x= i*50+x
                        y = 80
                        self.objectFichas[self.orderFichas[i]].rect.x = x
                        self.objectFichas[self.orderFichas[i]].rect.y = y
                        pass
                    if i > 8 and i <= 16:
                        x= (16-i)*60+150
                        y = 220
                        self.objectFichas[self.orderFichas[i]].rect.x = x
                        self.objectFichas[self.orderFichas[i]].rect.y = y
                        pass
                    if i > 16 and i <= 24:
                        x= (24-i)*80+x
                        y = 60
                        self.objectFichas[self.orderFichas[i]].rect.x = x
                        self.objectFichas[self.orderFichas[i]].rect.y = y
                        pass
                    if i > 24 and i <= 32:
                        x= (32-i)*70+x
                        y = 130
                        self.objectFichas[self.orderFichas[i]].rect.x = x
                        self.objectFichas[self.orderFichas[i]].rect.y = y
                        pass
                    if i > 32 and i <= 40:
                        x= (40-i)*60+x
                        y = 180
                        self.objectFichas[self.orderFichas[i]].rect.x = x
                        self.objectFichas[self.orderFichas[i]].rect.y = y
                        pass
                    if i > 40 and i <= 48:
                        x= (48-i)*50+100
                        y = 220
                        self.objectFichas[self.orderFichas[i]].rect.x = x
                        self.objectFichas[self.orderFichas[i]].rect.y = y
                        pass
                    if i > 48 and i <= 56:
                        x= (56-i)*50+x
                        y = 30
                        self.objectFichas[self.orderFichas[i]].rect.x = x
                        self.objectFichas[self.orderFichas[i]].rect.y = y
                        pass
                    if i > 56 and i <= 64:
                        x= (64-i)*80+x
                        y = 250
                        self.objectFichas[self.orderFichas[i]].rect.x = x
                        self.objectFichas[self.orderFichas[i]].rect.y = y
                        pass
                    if i > 64 and i <= 72:
                        x= (72-i)*100+x-30
                        y = 280
                        self.objectFichas[self.orderFichas[i]].rect.x = x
                        self.objectFichas[self.orderFichas[i]].rect.y = y
                        pass
                    if i > 72 and i <= 80:
                        x= (80-i)*50+50
                        y = 300
                        self.objectFichas[self.orderFichas[i]].rect.x = x
                        self.objectFichas[self.orderFichas[i]].rect.y = y
                        pass
                    if i > 80 and i <= 88:
                        x= (88-i)*75+x
                        y = 320
                        self.objectFichas[self.orderFichas[i]].rect.x = x
                        self.objectFichas[self.orderFichas[i]].rect.y = y
                        pass
                    if i > 88 and i <= 96:
                        x= (96-i)*80+x
                        y = 350
                        self.objectFichas[self.orderFichas[i]].rect.x = x
                        self.objectFichas[self.orderFichas[i]].rect.y = y
                        pass
                    if i > 96 and i <= 104:
                        x= (104-i)*50+350
                        y = 300
                        self.objectFichas[self.orderFichas[i]].rect.x = x
                        self.objectFichas[self.orderFichas[i]].rect.y = y
                        pass


        self.fichaCur = None
        self.rigth,self.left,self.resultWeigth = 0,0,0
        self.resultWeigth2 = 0


        pass


    def draw(self,tela):
        '''
        for k in range(4):
            for i in range(len(self.eixosLeft)):
                if self.eixosLeft[i][k].enable:
                    self.eixosLeft[i][k].draw(tela)
                    
            for i in range(len(self.eixosRight)):
                if self.eixosRight[i][k].enable:
                    self.eixosRight[i][k].draw(tela)
        
        
        
        for k in range(4):
            for a in range(len(self.eixosRight)):
                
                if self.eixosRight[a][k].canDraw and k >0:
                        self.eixosRight[a][k].draw(tela)
                        self.eixosRight[a][k].canDraw = False
        '''
                    
        DrawVector(self.objectFichas, tela)
        if not self.fichaCur is None:
            self.fichaCur.draw(tela)
        
            
        pass

    def event (self,event):

        if event.type == pygame.MOUSEMOTION:
            for q in self.objectFichas:
                q.update(pygame.mouse.get_pos())
                if q.hovering:
                    self.fichaCur = q

        if event.type == pygame.MOUSEBUTTONDOWN:
            for q in self.objectFichas:
                q.clickStart(pygame.mouse.get_pos())

        if event.type == pygame.MOUSEBUTTONUP:
            for q in self.objectFichas:
                if q.clickEnd(pygame.mouse.get_pos()):
                    return


    def update(self,dt,actions,vas = None):
        
        for i in self.objectFichas:
    
            #i.plugged = True

            if i.state == "Clicking":    
                '''            
                for a in self.objectFichas:
                    if not i == a and a.state == 'Clicking':                                                                        
                        a.rect.y =i.rect.y+ i.image.get_height()-3
                        break
                '''
                #print i.name,i.peso,i.colection,i.type
                
                i.image = i.click
                x,y = pygame.mouse.get_pos()
                vx = x - i.click.get_width()/2
                vy = y - i.click.get_height()/2
                dx,dy = False,False
                
                deltaSx = (x-i.oldPosDeltaS[0]) - i.click.get_width()/4
                deltaSy = (y-i.oldPosDeltaS[1]) - i.click.get_height()/4
                               
                
                if i.peso >1:
                    vx,vy = 0,0
                    
                    if i.peso == 2:
                        a = 1        
                    elif i.peso == 3:
                        a = 0.1
                        pass
                                    
                    if deltaSx < 0:
                        deltaSx *=-1
                        dx = True
                    if deltaSy < 0:
                        deltaSy *=-1
                        dy = True                
                    
                                           
                    vx = sqrt(int(2*a*deltaSx))
                   
                    vy = sqrt(int(2*a*deltaSy))
                    
                    
                    
                    if deltaSx == 0:
                        vx = 0
                    if deltaSy == 0:
                        vy = 0
                        
                    if dx:
                        vx *=-1
                    if dy:
                        vy *=-1    
                    
                    i.rect.x  += vx
                    i.rect.y += vy
                    
                else:                                         
                    i.rect.x  = vx
                    i.rect.y = vy
                    pass
                    
                i.oldPosDeltaS = [i.rect.x,i.rect.y]
                
                pass

            if i.state == "Idle":
                btn = False
                
                
                if (self.faseCur == "Fase1" or self.faseCur == "Fase8" or self.faseCur == 'Fase4') and self.rotate:
                    
                    #for i in self.objectFichas:
                    #    i.plugged = False
                    '''
                    oldRect = i.rect
                    i.rect = i.click.get_rect()
                    i.rect.x,i.rect.y = oldRect.x,oldRect.y
                    print self.objectFichas[0].rect.x,self.objectFichas[0].rect.y
                    '''
                    
                    for k in range(4):
                        
                        for a in range(len(self.eixosRight)):                            
                            if i.rect.colliderect(self.eixosRight[a][k]) and self.eixosRight[a][k].enable and not self.eixosRight[a][k].plugged and not i.plugged:
                                
                                btn = self.reviewEixo(i,k,a,self.eixosRight,'Right')                                
                                
                                break                            
                            
                            
                        for a in range(len(self.eixosLeft)):                            
                            if i.rect.colliderect(self.eixosLeft[a][k]) and self.eixosLeft[a][k].enable and not self.eixosLeft[a][k].plugged and not i.plugged: 
         
                                btn = self.reviewEixo(i,k,a,self.eixosLeft,'Left')
                                
                                break
                            
                            
                                
                                
                #print self.eixosRight[0][0].enable ,self.eixosRight[0][1].enable,self.eixosRight[0][2].enable,self.eixosRight[0][3].enable 
                #print self.eixosLeft[0][1].enable,self.eixosLeft[0][1].plugged 
                    
                if self.faseCur == "Fase4" and vas is not None:

                    for ob in self.objectMain:
                        if i.rect.colliderect(vas) or i.rect.colliderect(ob):
                            speed = 0
                            if i.rect.y <= vas.rect.y+i.click.get_height()/2 :
                                speed = -1

                            if i.rect.y >= vas.rect.y:
                                speed = 1

                            if i.rect.y >= 580 or i.rect.y <= 0:
                                speed = -1

                                if i.rect.y <= 0:
                                    speed = 1

                                loop = True
                                while loop:
                                    if i.rect.colliderect(vas) or i.rect.colliderect(ob):
                                        if i.rect.x <= 500:
                                            i.rect.x+= 1
                                        if i.rect.x > 500:
                                            i.rect.x+= -1

                                        i.rect.y+= speed
                                    else:
                                        loop = False
                                pass

                            i.rect.y+= speed
                        pass


                if not btn:

                    if self.faseCur == "Fase1" or self.faseCur == "Fase8":
                        if i.rect.x > 850 or i.rect.x < 140 or i.rect.y > 160:
                            i.rect.x , i.rect.y = i.oldPos
                            pass

                for o in self.objectFichas:
                    if not i == o:

                        if i.rect.colliderect(o):
                            speed = 0
                            if i.rect.x <= o.rect.x+o.click.get_width()/2 :
                                speed = -1
                                pass
                            if i.rect.x >= o.rect.x:
                                speed = 1
                                pass

                            if i.rect.x >= 850 or i.rect.x <= 175:
                                break

                            i.rect.x+= speed

            
            
            
            pass
        

        #ACTIONS
        
        actions.update(self.objectFichas,self.eixosLeft,self.eixosRight)
        


        self.rigth = self.left = self.resultWeigth = 0

        for i in range(len(self.weightLeft)):
            for a in range(4):
                self.left += self.weightLeft[i][a]
                
            
        for i in range(len(self.weightRight)):
            for a in range(4):
                self.rigth += self.weightRight[i][a]
        
        #print self.rigth,self.left
        self.resultWeigth = self.rigth-self.left
            
        if not self.faseCur== 'Fase8':
            
            if Vassoura.stateRotation == 'Left':
                self.stickBroomLeft,self.stickBroomRight=150,50
            elif Vassoura.stateRotation == 'Right':
                self.stickBroomLeft,self.stickBroomRight=50,150
            elif Vassoura.stateRotation == 'Center':
                self.stickBroomLeft,self.stickBroomRight=100,100 
        
        
        self.resultWeigth += self.stickBroomLeft-self.stickBroomRight
        
        for i in range(len(self.weightLeft)):
            for a in range(4):                
                self.weightLeft[i][a] = 0
        for i in range(len(self.weightRight)):
            for a in range(4):                
                self.weightRight[i][a] = 0

        '''
        for i in self.objectFichas:
            if i.plugged:
                print i.rect,i.image.get_rect()
       
        
        for k in range(4):
            for a in range(len(self.eixosRight)):
                if self.eixosRight[a][k].enable and k>0:
                    self.eixosRight[a][k].canDraw = True
        '''
        for i in self.objectFichas:
            i.plugged = False
            
        for k in range(4):
            
                        for a in range(len(self.eixosLeft)):                
                            self.eixosLeft[a][k].enable = False
                            self.eixosLeft[a][k].plugged = False
                            self.eixosLeft[a][0].enable = True
                        
                        
                        for a in range(len(self.eixosRight)):     
                                   
                            self.eixosRight[a][k].enable = False
                            self.eixosRight[a][k].plugged = False
                            self.eixosRight[a][0].enable = True
        
   
        #print Vassoura.stateRotation
        #print Vassoura.stateRotation,self.resultWeigth

        #=================================================
        #=================================================
    
        
        return self.takePosEixos(self.resultWeigth)

    pass


    def reviewEixo(self,ficha,k,a,eixo,stateEixo):
        '''
        for k in range(4):
                        
                        for a in range(len(eixo)):
                            
                            if ficha.rect.colliderect(eixo[a][k]) and eixo[a][k].enable:
                                btn = True
                                
                                ficha.rect.x ,ficha.rect.y = eixo[a][k].rect.x , eixo[a][k].rect.y
                                
                                if stateEixo == 'Left':
                                    self.weightLeft[a][k]=ficha.peso*(26-a)
                                elif stateEixo == 'Right':
                                    self.weightRight[a][k] = ficha.peso*(a+1)
                                
                                ficha.image = ficha.click
                                #if i.hovering == True:
                                #    i.image = i.hover
                                #else : i.image = i.click
                                ficha.plugged = True
                                
                                eixo[a][k].enable = False
                                
                                if not k > 2:
                                    eixo[a][k+1].enable = True
                                  
                                return btn
           '''                 
                 
        
        ficha.rect.x ,ficha.rect.y = eixo[a][k].rect.x , eixo[a][k].rect.y
                                
        if stateEixo == 'Left':
            self.weightLeft[a][k]=ficha.peso*(len(self.eixosLeft)-a)
        elif stateEixo == 'Right':
            self.weightRight[a][k] = ficha.peso*(a+1)
                                
        ficha.image = ficha.click
                                
        ficha.plugged = True
                                
        eixo[a][k].enable = False
                
  
        try:
            eixo[a][k+1].enable = True
        except: 
            pass

        #if eixo[a][1].enable: print 'OK'
        return True

# coding: latin-1 
import pygame, os,sys
from pygame.locals import *
from random import Random
import time,socket
from EmailConnection import Email
from random import Random
from math import sin,tan,radians,sqrt,cos

class BaseMain(object):

    size = [1024,615]
    tela = None
    
    def __init__(self):


        os.environ["SDL_VIDEO_CENTERED"] = "1"

        self.size = BaseMain.size
        self.baseSurface = pygame.display.set_mode((self.size),pygame.NOFRAME)
        #self.baseSurface = pygame.display.set_mode((self.size),pygame.FULLSCREEN)
        self.tela = pygame.Surface((self.size), pygame.SRCALPHA, 32)


        self.telaCurrent = pygame.Surface((self.size), pygame.SRCALPHA, 32)
        self.telaNext = pygame.Surface((self.size), pygame.SRCALPHA, 32)

        self.time = pygame.time.Clock()
        pygame.display.set_caption("Jogo da Vassoura")

        BaseMain.tela = self.tela
        
        #Set Fps=30
        self.fps = pygame.time.Clock()
        self.fpsTick = 30
        pass

    def deltaTime(self):

        self.dt = self.fps.tick(self.fpsTick)

        #Pegando o FPS e jogando na tela
        pygame.display.set_caption("Jogo da Vassoura - %d fps" % self.fps.get_fps())

        return self.dt/1000.0

    def draw(self,CurrentState):
        BaseMain.tela = self.tela
        self.baseSurface.blit(self.tela,(0,0))
        CurrentState.draw(self.tela)
        pass


    def updateScreen(self):

        pygame.display.flip()

        pass

    pass

class Timer(object):
    
    def __init__(self):
        self._time = 0
        pass 
    
    def updateTime(self):        
        self._time = pygame.time.get_ticks()/1000
        pass
    
    def get_time(self):
        return self._time
    
    pass


class BD(object):
    
    formCadastro = []
    
    actionsUser = []
    
    fase1Register = []
    
    fase3Register = []
    
    fase4Register = []
    
    fase6Register = []
    
    fase8Register = []
    
    fase10Register = []
    
    @staticmethod
    def oldtxt():           
        docR = open('src/bd/'+str(BD.formCadastro[0])+'.txt', 'r')
        oldtxt = docR.read()
        docR.close()               
        return oldtxt
    
    
    @staticmethod
    def setDataForms():
                 
        txt = ''
        txt += '''
        ==================================
        ==================================
        ================================== '''+"\n"+"\n"+"\n"
        
        txt += "Data : "+str(time.strftime("%d-%m-%Y %H:%M:%S"))+"\n"
        
        
        #for i in BD.formCadastro:
        txt += "Nome : "+ str(BD.formCadastro[0])+"\n"
        txt += "Ano Escolar : "+ str(BD.formCadastro[1])+"\n"
        txt += "Idade : "+ str(BD.formCadastro[2])+"\n"
        txt += "Escola : "+ str(BD.formCadastro[3])+"\n"
        
        
        docW = open('src/bd/'+str(BD.formCadastro[0])+'.txt', 'w')
            
        docW.write(txt)
        docW.close()
        
        pass
    
    
    @staticmethod
    def getFinalTime(time):
        
        return [0,0,0]
    
    
    @staticmethod
    def setDataFases(fase,actions,ficha,time):
        
        
        finalTime = BD.getFinalTime(time)
        finalTime1 = BD.getFinalTime(actions.firstMotion)
        finalTime2 = BD.getFinalTime(actions.firstClick)
        
        # Divisao do tempo
        if time < 60 : 
            hora = 0 
            minuto = 0
            segundo = time 
        
        
        txt = BD.oldtxt()
        
        txt += '''
        ==================================
                    '''+ fase +'''
        ================================== '''+"\n"+"\n"
        txt+= '''Tempo total da fase: '''+ str(finalTime[2]) + str(finalTime[1]) + str(finalTime[0]) +'''.
        Tempo para a primeira reação:'''+ str(finalTime1[2]) + str(finalTime1[1]) + str(finalTime1[0]) + '''
        Tempo para a primeira reação:'''+ str(finalTime2[2]) + str(finalTime2[1]) + str(finalTime2[0]) 
        
        txt+="\n"+"\n"
        
        for f in ficha.objectFichas:
            txt+=  f.name + "// Peso:"+ str(f.peso)+ "// " +f.colection + "// "+ f.type+ "--> Clicado "+str(f.countOfClicked)+" veze(s)."+"\n"+"\n"            
        pass
        
        
        txt += '''
        ==================================
        ==================================
        ================================== '''+"\n"+"\n"+"\n"
        
        docW = open('src/bd/'+str(BD.formCadastro[0])+'.txt', 'w')
            
        docW.write(txt)
        docW.close()
        
        pass
    
    @staticmethod
    def setDataFase1(fase,ficha,eixoL,eixoR):
        
        
        
        pass
    
    @staticmethod
    def setDataFase3():        
        BD.setDataQuestion(BD.fase3Register,'Fase 3')
        pass
    
    @staticmethod
    def setDataFase4():
        pass
    
    @staticmethod
    def setDataFase5():
        pass
    
    @staticmethod
    def setDataFase6():        
        BD.setDataQuestion(BD.fase6Register,'Fase 6')        
        pass
    
    @staticmethod
    def setDataFase8():
        pass
    
    @staticmethod
    def setDataFase10():
        BD.setDataQuestion(BD.fase10Register, 'Fase 10')
        pass
    
    @staticmethod
    def setDataQuestion(quest,fase):
        
        txt = BD.oldtxt()
        
        txt += '''
        ==================================
                    '''+ fase +'''
        ================================== '''+"\n"+"\n"
        
        txt += str(quest)
        
        txt += '''
        ==================================
        ==================================
        ================================== '''+"\n"+"\n"+"\n"
        
        docW = open('src/bd/'+str(BD.formCadastro[0])+'.txt', 'w')
            
        docW.write(txt)
        docW.close()
        
        pass
    
    @staticmethod
    def setText(text,fase):
        
        txt = BD.oldtxt()
        
        txt += "\n"+"\n"+'''
        
        InterrupÃ§Ã£o !!
        ==================================
                '''+ fase +'''
        ================================== '''+"\n"+'''
        
                '''+text+"\n"+'''
        
         Final da InterrupÃ§Ã£o !!
        ==================================
        '''+"\n"+"\n"
        
        
        docW = open('src/bd/'+str(BD.formCadastro[0])+'.txt', 'w')
            
        docW.write(txt)
        docW.close()
        
        pass
    
    
    @staticmethod
    def send():
        if BD.testConnection():
            txt = "Nome : "+ str(BD.formCadastro[0])+"\n"
            txt += "Ano Escolar : "+ str(BD.formCadastro[1])+"\n"
            txt += "Idade : "+ str(BD.formCadastro[2])+"\n"
            txt += "Escola : "+ str(BD.formCadastro[3])+"\n"
            try:
                Email().send('gamesinteligentes@gmail.com', ['gamesinteligentes@gmail.com'], 'Jogo da Vassoura '+str(BD.formCadastro[0]),str(txt), ['src/bd/'+BD.formCadastro[0]+'.txt'])              
            except:
                try:
                    Email().send('gamesinteligentes@gmail.com', ['gamesinteligentes@gmail.com'], 'Jogo da Vassoura '+str(BD.formCadastro[0]),str(txt), ['src/bd/'+BD.formCadastro[0]+'.txt'])                
                except:
                    print "Falha ao enviar o email!"
                    pass
                                
        else:
            
            print 'Falha ao enviar o email!NÃ£o hÃ¡ conexÃ£o com a internet!'
            pass
            
    
    
    
    @staticmethod
    def testConnection():
        
        
        links = ['www.google.com', 'www.yahoo.com', 'www.bb.com.br']
        
        for host in links:
            a=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            a.settimeout(.5)
            try:
                b=a.connect_ex((host, 80))
                if b==0: 
                    return True
            except:
                pass
            a.close()
            return False
    
    

class GameState(object):

    def __init__(self):
        self.fps = 30
        pass

    def draw(self, tela):
        pass

    def update(self,dt):
        pass

    def event(self, event):
        pass




class Object(object):

    def __init__(self,file,posx = 0, posy = 0):

        self.oldIdle = self.image = pygame.image.load(file).convert_alpha()
        self.oldRect = self.rect = self.image.get_rect()
        self.oldRect.x,self.oldRect.y = self.rect.x,self.rect.y = posx,posy
        self.oldPos = posx,posy
        self.reverseIdle = self.reverse()
        self.canRotation = False
        pass

    def draw(self,tela):
        tela.blit(self.image, self.rect)
        pass
    
    def tranform(self,point=1.0):
        
        self.image = self.oldIdle
        #self.image = pygame.transform.scale(self.image,(1200,800))
        self.image = pygame.transform.rotozoom(self.image,0,point)
            
        pass

    def reverse(self):

        self.imageRotate = self.oldIdle

        oldrectCenter = self.rect.center
        self.imageRotate =  pygame.transform.rotate(self.imageRotate,180)

        self.rect = self.imageRotate.get_rect()
        self.rect.center = oldrectCenter

        return self.imageRotate

    def rotate(self,angle):

        self.imageRotate = self.oldIdle

        oldrectCenter = self.rect.center
        
        self.imageRotate =  pygame.transform.rotate(self.imageRotate,angle)

        self.rect = self.imageRotate.get_rect()
        
        self.rect.center = oldrectCenter

        self.image = self.imageRotate
        
        pass
    
    def rotateLeft(self,angle,MAXangle,MINangle,pointRotation):
        
        #DeltaH = tan(radians(angle))*(pointRotation)
        DeltaS = self.oldIdle.get_width()-self.image.get_width()
        DeltaH = sin(radians(angle))*(pointRotation)
        
        if not angle == 0:   
            
            self.rotate(angle)
            
            if angle < 0 and angle <= MAXangle:
                self.rect.y = self.oldRect.y + DeltaH*2
                #self.rect.x = self.oldRect.y + DeltaS
                
            if angle > 0 and angle >= MINangle:
                self.rect.y = self.oldRect.y - DeltaH*2
                #self.rect.x = self.oldRect.y - DeltaS
        
        
        
        pass
    
    def rotateRight(self,angle,MAXangle,MINangle,pointRotation):
        
        #DeltaH = tan(radians(angle))*(pointRotation)
        #DeltaS = self.oldIdle.get_width()-self.image.get_width()
        DeltaS = pointRotation/cos(radians(angle))
        
        DeltaH = sin(radians(angle))*(pointRotation)
        
        if not angle == 0:   
            
            self.rotate(angle)
            
            if angle > 0 and angle <= MAXangle:
                
                self.rect.y = self.oldRect.y - DeltaH
                #self.rect.x = self.oldRect.x - DeltaS
         
            if angle < 0 and angle >= MINangle:
                
                self.rect.y = self.oldRect.y + DeltaH
                #self.rect.x = self.oldRect.x + DeltaS
         
            
        pass
    
    def rotateLeft2(self,angle,MAXangle,MINangle,ficha=None,raio = 13):
        
        if ficha is not None:
            DeltaH = tan(radians(angle))*(raio * ficha.objectFichas[0].image.get_width())
        else:
            if not raio != 13:
                raio = (self.image.get_width()/4)
            DeltaH = tan(radians(angle))*(raio)
            
        #DeltaS = int(tan(radians(angle))*DeltaH)
        DeltaS = self.oldIdle.get_width()-self.image.get_width()
    
        if not angle == 0:   
            
            self.rotate(angle)
            
            if angle < 0 and angle <= MAXangle:
                self.rect.y = self.oldRect.y + DeltaH
                #self.rect.x = self.oldRect.y + DeltaS
                
            if angle > 0 and angle >= MINangle:
                self.rect.y = self.oldRect.y - DeltaH*2
                #self.rect.x = self.oldRect.y - DeltaS
            
        pass
    
    
    def rotateRight2(self,angle,MAXangle,MINangle,ficha=None,raio = 13):
        
        if ficha is not None:
            #DeltaH = tan(radians(angle))*(raio * ficha.objectFichas[0].image.get_width())
            DeltaH = tan(radians(angle))*((self.image.get_width()-102)/6)*2.2
            
        else:
            if not raio != 13:
                raio = (self.image.get_width()/6)*2.2
            DeltaH = tan(radians(angle))*(raio)
            
        DeltaS2 = int(tan(radians(angle))*DeltaH)
        DeltaS = (self.oldIdle.get_width()-self.image.get_width())
        
        if DeltaS > 0:
            DeltaS *=-1
        
        if not angle == 0:   
            
            self.rotate(angle)
            
            if angle > 0 and angle <= MAXangle:
                self.rect.y = self.oldRect.y - DeltaH
                self.rect.x = self.oldRect.x - DeltaS
         
            if angle < 0 and angle >= MINangle:
                self.rect.y = self.oldRect.y + DeltaH*2
                self.rect.x = self.oldRect.x + DeltaS
         
            
        pass


class ObjectPoint(Object):

    def __init__(self,file,posx = 0, posy = 0):
        self.oldIdle = self.image = pygame.image.load(file).convert_alpha()
        self.oldRect = self.rect = self.image.get_rect()
        self.oldRect.x,self.oldRect.y = self.rect.x,self.rect.y = posx,posy
        self.oldPos = posx,posy
        self.reverseIdle = self.reverse()
        self.plugged = False
        self.enable = False
        self.objectPlugged = None
        pass

 

class ObjectEixo(Object):

    def __init__(self,file,posx = 0, posy = 0):
        self.oldPos = posx,posy
        self.image = file
        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y = posx,posy
        self.enable = False
        self.objectPlugged = None
        self.plugged = False
        self.canDraw = False
        pass


class ObjectEvent(Object):

    def __init__(self, pos, idleImage, hoverImage=None, clickImage=None, function=None):

        self.oldIdle = self.idle = pygame.image.load(idleImage)
        if hoverImage is not None:
            self.hover = pygame.image.load(hoverImage)
        else:
            self.hover = self.idle

        if clickImage is not None:
            self.click = pygame.image.load(clickImage)
        else:
            self.click = self.idle

        self.oldRect , self.rect = self.click.get_rect(),self.idle.get_rect()
        self.oldRect.x,self.oldRect.y =pos
        self.rect.x, self.rect.y = pos
        self.oldPos = pos

        self.state = "Idle"
        self.hovering = False

        self.initImage = self.image = self.idle
        self.onclick = function
        self.hasParameter = False

        self.reverseIdle = self.reverse()
        
        self.oldWidth,self.oldHeight = self.image.get_width(),self.image.get_height()
        pass
  
    def update(self, mousepos):

        if self.state == "Idle":
            if self.rect.collidepoint(mousepos):
                self.image = self.hover
                self.hovering = True

            else:
                self.image = self.idle
                self.hovering = False

        if self.state == "Clicking":
            if self.rect.collidepoint(mousepos):
                self.image = self.click
            else:
                self.image = self.idle
                pass
            pass


    def setParameter(self, param):
        self.hasParameter = True
        self.parameter = param

    def clickStart(self, mousepos):
        if self.rect.collidepoint(mousepos):
            self.state = "Clicking"
            self.image = self.click

    def clickEnd(self, mousepos):
        ret = False
        if self.state == "Clicking":
            if self.rect.collidepoint(mousepos):

                self.image = self.idle
                if self.onclick is not None:
                    if self.hasParameter:
                        self.onclick(self.parameter)
                    else:
                        self.onclick()
                    ret = True
            self.state = "Idle"

        return ret

    pass

class ObjectThings(ObjectEvent):

    def __init__(self, pos, idleImage, name,hoverImage=None, clickImage=None, function=None):

        self.oldIdle = self.idle = pygame.image.load(idleImage)
        if hoverImage is not None:
            self.hover = pygame.image.load(hoverImage)
        else:
            self.hover = self.idle

        if clickImage is not None:
            self.click = pygame.image.load(clickImage)
        else:
            self.click = self.idle

        self.oldRect , self.rect = self.idle.get_rect(),self.idle.get_rect()
        self.oldRect.x,self.oldRect.y =pos
        self.rect.x, self.rect.y = pos
        self.oldPos = pos

        self.state = "Idle"
        self.hovering = False

        self.initImage = self.image = self.idle
        self.onclick = function
        self.hasParameter = False

        self.reverseIdle = self.reverse()
        
        self.oldWidth,self.oldHeight = self.image.get_width(),self.image.get_height()
        
        self.plugged = False
        self.name = name
        pass
    


class ObjectFicha(ObjectEvent):

    def __init__(self, pos, idleImage, hoverImage=None, clickImage=None, peso=None,colection=None,type=None,name=''):

        self.type = type        
        self.colection=colection
        self.oldPos = pos
        self.oldPosDeltaS = pos
        self.peso = peso
        
        self.oldIdle = self.idle = pygame.image.load(idleImage)
        
        self.name = name
        
        if hoverImage is not None:
            self.hover = pygame.image.load(hoverImage)
        else:
            self.hover = self.idle

        if clickImage is not None:
            self.click = pygame.image.load(clickImage)
        else:
            self.click = self.idle

        self.rect = self.idle.get_rect()

        self.rect.x, self.rect.y = pos
        

        self.state = "Idle"
        self.hovering = False
        
        self.onclick = None

        self.initImage = self.image = self.idle
        self.reverseIdle = self.reverse()
        
        self.newX = (self.hover.get_width()-self.idle.get_width())/2
        self.newY = (self.hover.get_height()-self.idle.get_height())/2 
            
        self.newPos = False 
        self.less = False
        
        self.plugged = False
        
        self.countOfClicked =0
        self.canCountClickt=True
        pass
    
    
    def update(self, mousepos):
        
        self.x,self.y = self.rect.x,self.rect.y
        
        if  self.plugged=='8768':
            if self.less:
                self.rect.x+=self.newX
                self.rect.y+=self.newY
                self.less = False
                pass

        if self.state == "Idle":
            if self.rect.collidepoint(mousepos):
                self.image = self.hover
                self.hovering = True
                self.newPos = True
                self.canCountClickt = True
                
            else:
                self.image = self.idle
                self.hovering = False

        if self.state == "Clicking":
            if self.rect.collidepoint(mousepos):
                if self.canCountClickt: 
                    self.countOfClicked +=1
                    self.canCountClickt = False
                    
                self.image = self.click
                self.rect = self.click.get_rect()
                self.rect.x,self.rect.y = self.x,self.y
            else:
                self.image = self.idle
                self.rect = self.idle.get_rect()
                self.rect.x,self.rect.y = self.x,self.y
                pass
            pass
        
        if  self.plugged=='675765':
            if self.newPos :            
                self.rect.x-=self.newX
                self.rect.y-=self.newY
                self.less = True
                self.newPos = False
                
        if self.plugged:
            self.image = self.click
            self.rect = self.click.get_rect()
            self.rect.x,self.rect.y = self.x,self.y
                
        
        #self.rectClick.x, self.rectClick.y = self.rect.x,self.rect.y
        '''
        if self.state == 'Idle':
            self.rect = self.rectIdle
        elif self.state == 'Clicking' or self.plugged:
            self.rect = self.rectClick
        '''
                
        '''
        if not self.plugged: 
            oldPos = self.rect.x,self.rect.y 
            self.rect = self.image.get_rect()
            self.rect.x,self.rect.y = oldPos
      
        '''
      
        #self.rectClick.x,self.rectClick.y = self.rectHover.x,self.rectHover.y = self.rectIdle.x,self.rectIdle.y = self.rect.x, self.rect.y 
        
        #print self.hovering,self.state,self.rect,self.rect.x,self.rect.y

class ObjectRadio(ObjectEvent):

    def __init__(self, pos, idleImage, hoverImage=None, clickImage=None,name = '', function=None):

        self.name = name
        
        self.oldPos = pos

        self.oldIdle = self.idle = pygame.image.load(idleImage)
        if hoverImage is not None:
            self.hover = pygame.image.load(hoverImage)
        else:
            self.hover = self.idle

        if clickImage is not None:
            self.click = pygame.image.load(clickImage)
        else:
            self.click = self.idle

        self.rect = self.idle.get_rect()
        self.rect.x, self.rect.y = pos

        self.state = "Idle"
        self.hovering = False

        self.initImage = self.image = self.idle
        self.onclick = function
        self.hasParameter = False

        self.reverseIdle = self.reverse()
        pass
    
    def updateState(self,state):
        
        if self.name == state:
            self.image = self.click
        else:
            self.image = self.idle    
        
        pass
    
    
class Text(Object):

        def __init__(self,text="", posx=0 ,posy=0, size= 20,italic=True,
                     negrito=False,cor=[255,255,255], fundoCor=[154,58,165],
                     fundo = False,nameFont="Comic Sans MS"):
            self.cor = cor
            self.fundoCor = fundoCor
            self.fonte = pygame.font.SysFont(nameFont,size,negrito,italic)
        
            if fundo:
                self.oldIdle = self.image = self.fonte.render(text,0,cor,fundoCor)
            else:
                self.oldIdle = self.image = self.fonte.render(text,0,cor)
            self.rect = self.image.get_rect()
            self.rect.x,self.rect.y = posx,posy
            pass
        
        def setText(self,txt):
            self.image = self.fonte.render(txt,0,self.cor,self.fundoCor)            
            pass


class Music():

    def __init__(self, path):
        self.path = path

    def play(self, loop = 0,vol = 0.4):
        '''
        pygame.mixer.music.load(self.path)
        pygame.mixer.music.set_volume(vol)
        pygame.mixer.music.play(loop)
        '''
        pass

    @staticmethod
    def pause():        
        #pygame.mixer.music.pause()
        pass

    @staticmethod
    def stop():
        pygame.mixer.music.stop()


class Sound():

    def __init__(self,path):
        self.sound = pygame.mixer.Sound(path)
        pass

    def play (self,loop = 0, vol = 1.0):
        #self.sound.set_volume(vol)
        #self.sound.play(loop)
        pass




class Animation (BaseMain):

    def __init__(self, currentState, nextState,telaCurrent,telaNext,effect=0):

        self.rand = Random()

        self.currentState, self.nextState = currentState, nextState
        self.telaCurrent,self.telaNext = telaCurrent,telaNext

        #self.effects = [[self.windowsUP,0,1], [self.windowsDOWN,0,-1],
        #                [self.windowsLEFT,1,0],[self.windowsRIGHT,-1,0]]
        #self.effectWindows = self.effects [self.rand.randrange(0,len(self.effects))]

        self.effects = [[self.windowsLEFT,1,0], [self.windowsRIGHT,-1,0],[self.windowsUP,0,1], [self.windowsDOWN,0,-1]]
        self.effectWindows = self.effects [effect]

        self.posCurrent, self.posNext = [0,0],[self.currentState.backGround.rect.width*self.effectWindows[1],self.nextState.backGround.rect.height*self.effectWindows[2]]

        self.speed = 4
        pass


    def drawEffect (self,baseSurface,dt):

        self.currentState.draw(self.telaCurrent)
        self.nextState.draw(self.telaNext)

        while True:

            if self.effectWindows[0](dt):
                self.nextState.draw(self.telaCurrent)
                return False
            else:

                baseSurface.blit(self.telaCurrent,self.posCurrent)
                baseSurface.blit(self.telaNext,self.posNext)

                pygame.display.flip()
                pass


    def windowsUP(self,dt):

        if not (self.posNext[1] < 0):

            self.posCurrent[1] += -self.speed+int(self.speed*dt)
            self.posNext[1] += -self.speed+int(self.speed*dt)

            return False
        else:
            return True

        pass

    def windowsDOWN(self,dt):

        if not (self.posNext[1] > 0):

            self.posCurrent[1] += self.speed+int(self.speed*dt)
            self.posNext[1] += self.speed+int(self.speed*dt)

            return False
        else:
            return True


        pass

    def windowsLEFT(self,dt):

        if not (self.posNext[0] < 0):

            self.posCurrent[0] += -self.speed+int(self.speed*dt)
            self.posNext[0] += -self.speed+int(self.speed*dt)

            return False
        else:
            return True

        pass

    def windowsRIGHT(self,dt):

        if not (self.posNext[0] > 0):

            self.posCurrent[0] += self.speed+int(self.speed*dt)
            self.posNext[0] += self.speed+int(self.speed*dt)

            return False
        else:
            return True

        pass

    pass




        
class Forms(pygame.Rect,object):

    def __init__(self,pos,width,height=None,font=None,fontsize=None,bg=(200,200,200),fgcolor=(0,0,0),curscolor=(0,0,0),hlcolor=(0xa0,0,0),maxlines=0):
        if not font: self.FONT = pygame.font.Font(pygame.font.get_default_font(),fontsize)
        elif type(font) == str: self.FONT = pygame.font.Font(font,fontsize)
        else: self.FONT = font
        if not height: pygame.Rect.__init__(self,pos,(width,self.FONT.get_height()))
        else: pygame.Rect.__init__(self,pos,(width,height))

        self.BG = bg
        self.FGCOLOR = fgcolor
        self.CURSCOLOR = curscolor
        self.CURSOR = True
        self.HLCOLOR = hlcolor
        self.MAXLINES = maxlines
        self.TAB = 4

        self.OUTPUT = ''
        self.CURSORINDEX = 0
        self.SELECTSTART = 0
        self._x,self._y = pos
        self.SRC = pygame.display.get_surface()

    def clear_selection(self):
        if self.SELECTSTART != self.CURSORINDEX:
            select1,select2 = sorted((self.SELECTSTART,self.CURSORINDEX))
            self.OUTPUT = self.OUTPUT[:select1]+self.OUTPUT[select2:]
            self.CURSORINDEX = select1
            return True
        return False

    def show(self):
        h = self.FONT.get_height()
        x,y = self._x,self._y
        r = pygame.Rect(x,y,0,h)
        for e,i in enumerate(self.OUTPUT+'\n'):
            if e == self.CURSORINDEX+1: break
            if i not in '\n\t':
                r = pygame.Rect(x,y,*self.FONT.size(i))
                x = r.right
            elif i == '\n':
                r = pygame.Rect(x,y,1,h)
                x = self._x
                y = r.bottom
            else:
                t = self.FONT.size(self.TAB*' ')[0]
                t = ((((x-self._x) / t) + 1) * t ) - (x-self._x)
                r = pygame.Rect(x,y,t,h)
                x = r.right

        rclamp = r.clamp(self)
        self._x += rclamp.x - r.x
        self._y += rclamp.y - r.y

        clip = self.SRC.get_clip()
        self.SRC.set_clip(self.clip(clip))
        try: self.SRC.fill(self.BG,self)
        except: self.SRC.blit(self.BG,self)
        x = self._x
        y = self._y
        select1,select2 = sorted((self.SELECTSTART,self.CURSORINDEX))
        self.C = []
        for e,i in enumerate(self.OUTPUT):
            if i not in '\n\t':
                self.C.append(pygame.Rect(x,y,*self.FONT.size(i)))
                if select1 <= e < select2:
                    self.SRC.blit(self.FONT.render(i,1,self.HLCOLOR),(x,y))
                else:
                    self.SRC.blit(self.FONT.render(i,1,self.FGCOLOR),(x,y))
                x = self.C[-1].right
            elif i == '\n':
                self.C.append(pygame.Rect(x,y,0,h))
                x=self._x
                y = self.C[-1].bottom
            else:
                t = self.FONT.size(self.TAB*' ')[0]
                t = ((((x-self._x) / t) + 1) * t ) - (x-self._x)
                self.C.append(pygame.Rect(x,y,t,h))
                x = self.C[-1].right
        self.C.append(pygame.Rect(x,y,0,h))
        if self.CURSOR:
            p = self.C[self.CURSORINDEX]
            pygame.draw.line(self.SRC,self.CURSCOLOR,p.topleft,(p.left,p.bottom),1)
        pygame.display.update(self)
        self.SRC.set_clip(clip)

    def place_cursor(self,pos):
            c = pygame.Rect(pos,(0,0)).collidelist(self.C)
            if c > -1: self.CURSORINDEX = c if pos[0] <= self.C[c].centerx else c + 1
            else:
                l = (pos[1] - self._y) / self.FONT.get_height()
                self.CURSORINDEX = sum([len(i) for i in self.OUTPUT.split('\n')][:l+1])+l
                if self.CURSORINDEX > len(self.OUTPUT): self.CURSORINDEX = len(self.OUTPUT)
                elif self.CURSORINDEX < 0: self.CURSORINDEX = 0

    def wakeup(self,ev):
        if ev.type == pygame.KEYDOWN:

            if ev.key == pygame.K_RIGHT:
                if self.SELECTSTART != self.CURSORINDEX: self.CURSORINDEX = max((self.SELECTSTART,self.CURSORINDEX))
                elif self.CURSORINDEX < len(self.OUTPUT): self.CURSORINDEX += 1

            elif ev.key == pygame.K_LEFT:
                if self.SELECTSTART != self.CURSORINDEX: self.CURSORINDEX = min((self.SELECTSTART,self.CURSORINDEX))
                elif self.CURSORINDEX > 0: self.CURSORINDEX -= 1

            elif ev.key == pygame.K_DELETE:
                if not self.clear_selection():
                    self.OUTPUT = self.OUTPUT[:self.CURSORINDEX]+self.OUTPUT[self.CURSORINDEX+1:]

            elif ev.key == pygame.K_END:
                try:
                    self.CURSORINDEX = self.OUTPUT[self.CURSORINDEX:].index('\n') + self.CURSORINDEX
                except:
                    self.CURSORINDEX = len(self.OUTPUT)

            elif ev.key == pygame.K_HOME:
                try:
                    self.CURSORINDEX = self.OUTPUT[:self.CURSORINDEX].rindex('\n') + 1
                except:
                    self.CURSORINDEX = 0

            elif ev.key == pygame.K_RETURN or ev.key == pygame.K_KP_ENTER:
                self.clear_selection()
                if not self.MAXLINES or self.OUTPUT.count('\n') < self.MAXLINES - 1:
                    self.OUTPUT = self.OUTPUT[:self.CURSORINDEX]+'\n'+self.OUTPUT[self.CURSORINDEX:]
                    self.CURSORINDEX += 1

            elif ev.key == pygame.K_BACKSPACE:
                if not self.clear_selection():
                    if self.CURSORINDEX > 0:
                        self.CURSORINDEX -= 1
                        self.OUTPUT = self.OUTPUT[:self.CURSORINDEX]+self.OUTPUT[self.CURSORINDEX+1:]

            elif ev.key == pygame.K_UP:
                c = self.C[self.CURSORINDEX]
                self.place_cursor((c.left,c.top-self.FONT.get_height()))

            elif ev.key == pygame.K_DOWN:
                c = self.C[self.CURSORINDEX]
                self.place_cursor((c.left,c.top+self.FONT.get_height()))

            elif ev.unicode:
                self.clear_selection()
                self.OUTPUT = self.OUTPUT[:self.CURSORINDEX]+ev.unicode+self.OUTPUT[self.CURSORINDEX:]
                self.CURSORINDEX += 1
            if ev.key not in (K_NUMLOCK,K_CAPSLOCK,K_SCROLLOCK,K_RSHIFT,K_LSHIFT,K_RCTRL,K_LCTRL,K_RALT,K_LALT,K_RMETA,K_LMETA,K_LSUPER,K_RSUPER,K_MODE,K_HELP,K_PRINT,K_SYSREQ,K_BREAK,K_MENU,K_POWER):
                self.SELECTSTART = self.CURSORINDEX
            self.show()

        elif (ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1) or (ev.type == pygame.MOUSEMOTION and ev.buttons[0]):
            self.place_cursor(ev.pos)
            if ev.type == pygame.MOUSEBUTTONDOWN:
                self.SELECTSTART = self.CURSORINDEX
            self.show()


class Reader(pygame.Rect,object):

    class ln(object):
        def __init__(self,string,nl,sp):
            self.string = string
            self.nl = nl
            self.sp = sp

    def __init__(self,text,pos,width,fontsize,height=None,font=None,bg=(250,250,250),fgcolor=(0,0,0),hlcolor=(180,180,200),split=True):
        self._original = text.expandtabs(4).split('\n')
        self.BG = bg
        self.FGCOLOR = fgcolor
        self._line = 0
        self._index = 0
        if not font:
            self._fontname = pygame.font.match_font('mono',1)
            self._font = pygame.font.Font(self._fontname,fontsize)
        elif type(font) == str:
            self._fontname = font
            self._font = pygame.font.Font(font,fontsize)
        self._w,self._h = self._font.size(' ')
        self._fontsize = fontsize
        if not height: pygame.Rect.__init__(self,pos,(width,self._font.get_height()))
        else: pygame.Rect.__init__(self,pos,(width,height))
        self.split = split
        self._splitted = self.splittext()
        self._x,self._y = pos
        self._src = pygame.display.get_surface()
        self._select = self._line,self._index
        self._hlc = hlcolor
        self.HLCOLOR = hlcolor

    def splittext(self):
        nc = self.width // self._w
        out = []
        for e,i in enumerate(self._original):
            a = Reader.ln('',e,0)
            if not i:
                out.append(a)
                continue
            for j in textwrap.wrap(i,nc,drop_whitespace=True) if self.split else [i]:
                out.append(Reader.ln(j,e,a.sp+len(a.string)))
                a = out[-1]
        return out

    @property
    def TEXT(self):
        return '\n'.join(self._original)
    @TEXT.setter
    def TEXT(self,text):
        self._original = text.expandtabs(4).split('\n')
        self._splitted = self.splittext()

    @property
    def LEN(self):
        return len(self._splitted)

    @property
    def HLCOLOR(self):
        return self._hlc
    @HLCOLOR.setter
    def HLCOLOR(self,color):
        self._hlsurface = pygame.Surface((self._w,self._h),pygame.SRCALPHA)
        self._hlsurface.fill(color)

    @property
    def POS(self):
        return self._line,self._index

    @property
    def NLINE(self):
        return self._splitted[self._line].nl

    @property
    def LINE(self):
        return self._original[self.NLINE]

    @property
    def WORD(self):
        try:
            s = self._splitted[self._line].sp+self.wrd
            p1 = self.LINE[:s].split(' ')[-1]
            p2 = self.LINE[s:].split(' ')[0]
            if p2: return p1+p2
        except: return None

    @property
    def SELECTION(self):
        p1,p2 = sorted(((self._line,self._index),self._select))
        if p1 != p2:
            selection = [len(i.string) for i in self._splitted[:p2[0]]]
            return '\n'.join(self._original)[sum(selection[:p1[0]]) + self._splitted[p1[0]].nl + p1[1]:sum(selection) + self._splitted[p2[0]].nl + p2[1]]
        return ''

    @property
    def FONTSIZE(self):
        return self._fontsize
    @FONTSIZE.setter
    def FONTSIZE(self,size):
        self._font = pygame.font.Font(self._fontname,size)
        self._fontsize = size
        self._w,self._h = self._font.size(' ')
        self._splitted = self.splittext()
        y = self._y
        h = len(self._splitted) * self._h
        if h > self.height:
            if self._y - self._h < self.bottom - h: self._y = self.bottom - h
        self._y += (self.top - self._y)%self._h
        self.HLCOLOR = self._hlc

    def screen(self):
        clip = self._src.get_clip()
        self._src.set_clip(self.clip(clip))
        try: self._src.fill(self.BG,self)
        except: self._src.blit(self.BG,self)

        start = (self.top - self._y) // self._h
        end = (self.bottom - self._y) // self._h + 1

        p1,p2 = sorted(((self._line,self._index),self._select))

        y = self._y + start * self._h
        for py,i in enumerate(self._splitted[start:end],start):
            x = self._x
            for px,j in enumerate(i.string):
                if p1<=(py,px)<p2:
                    self._src.blit(self._hlsurface,(x,y))
                    self._src.blit(self._font.render(j,1,self.FGCOLOR),(x,y))
                else:
                    self._src.blit(self._font.render(j,1,self.FGCOLOR),(x,y))
                x += self._w
            y += self._h
        self._src.set_clip(clip)

    def show(self):
        self.screen()
        pygame.display.update(self)

    def scrolldown(self,n):
        y = self._y
        if self._y + self._h * n > self.top: self._y = self.top
        else: self._y += self._h * n

    def scrollup(self,n):
        y = self._y
        h = len(self._splitted) * self._h
        if h > self.height:
            if self._y - self._h * n < self.bottom - h: self._y = self.bottom - h
            else: self._y -= self._h * n

    def update(self,ev):

        line,index = self._line,self._index
        ctrl = pygame.key.get_pressed()
        ctrl = ctrl[pygame.K_RCTRL]|ctrl[pygame.K_LCTRL]

        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_UP:
                self.scrolldown(1)
                return True

            elif ev.key == pygame.K_DOWN:
                self.scrollup(1)
                return True

            elif ctrl and ev.key == pygame.K_KP_PLUS:
                self.FONTSIZE += 1
                return True

            elif ctrl and ev.key == pygame.K_KP_MINUS and self._fontsize:
                self.FONTSIZE -= 1
                return True

        elif ev.type == pygame.MOUSEBUTTONDOWN and self.collidepoint(ev.pos):
            if ev.button == 1:
                self._line = (ev.pos[1] - self._y) // self._h
                self._index = (ev.pos[0] - self._x) // self._w
                self.wrd = self._index
                if ((ev.pos[0] - self._x) % self._w) > (self._w // 2): self._index += 1
                if self._line > len(self._splitted)-1:
                    self._line = len(self._splitted)-1
                    self._index = len(self._splitted[self._line].string)
                if self._index > len(self._splitted[self._line].string): self._index = len(self._splitted[self._line].string)
                self._select = self._line,self._index

        elif ev.type == pygame.MOUSEBUTTONUP and self.collidepoint(ev.pos):
            try:
                if ev.click[4]:
                    self.scrolldown(sum(range(1,ev.click[4]+1))//10+1)
                    return True
                elif ev.click[5]:
                    self.scrollup(sum(range(1,ev.click[5]+1))//10+1)
                    return True
            except:
                if ev.button == 4:
                    self.scrolldown(3)
                    return True

                elif ev.button == 5:
                    self.scrollup(3)
                    return True

        elif ev.type == pygame.MOUSEMOTION and ev.buttons[0] and self.collidepoint(ev.pos):
            self._line = (ev.pos[1] - self._y) // self._h
            self._index = (ev.pos[0] - self._x) // self._w
            if ((ev.pos[0] - self._x) % self._w) > (self._w // 2): self._index += 1
            if self._line > len(self._splitted)-1:
                self._line = len(self._splitted)-1
                self._index = len(self._splitted[self._line].string)
            if self._index > len(self._splitted[self._line].string): self._index = len(self._splitted[self._line].string)
            return True

class Lister(Reader):

    def __init__(self,liste,pos,size,fontsize,font=None,fgcolor=(0,0,0),hlcolor=(120,18,250)):
        self.font = font
        self.text = ' %s\n'%'\n '.join(liste)
        self.fontsize = fontsize
        self.fgcolor = fgcolor
        self.hlcolor = hlcolor
        self.foo = -1
        self.pack(pos,size)
        self.scr = pygame.display.get_surface()

    def pack(self,pos,size):
        width,height = size
        Reader.__init__(self,self.text,pos,width,self.fontsize,None,self.font,fgcolor=self.fgcolor,hlcolor=self.hlcolor,split=False)
        self._line = self.foo
        h = self.height
        self.height = height//self.height*self.height
        self.BG = pygame.Surface(self.size)
        for i in range(self.height//h): self.BG.fill(0xffffff if i&1 else 0xf0f0f0,(0,i*h,width,h))

    def update(self,ev):
        nline = self.NLINE
        ret = super(Lister,self).update(ev)
        if nline == self.NLINE: ret = False
        if ev.type == pygame.MOUSEBUTTONUP and self.collidepoint(ev.pos):
            self.foo = self.NLINE
            return True
        elif ev.type == pygame.MOUSEMOTION and ev.buttons[0] and not self.collidepoint(ev.pos):
            self._line = self.foo
            return False
        elif ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1 and self.collidepoint(ev.pos):
            return True
        return ret


    @property
    def OUTPUT(self): return None
    @OUTPUT.setter
    def OUTPUT(self,liste):
        self.text = ' %s\n'%'\n '.join(liste)
        Reader.__init__(self,self.text,self.topleft,self.width,self.fontsize,self.height,self.font,bg=self.BG,fgcolor=self.fgcolor,split=False,hlcolor=self.hlcolor)
        self._line = self.foo = -1


    def screen(self):
        #super(Lister,self).screen()
        clip = self._src.get_clip()
        self._src.set_clip(self.clip(clip))
        try: self._src.fill(self.BG,self)
        except: self._src.blit(self.BG,self)

        start = (self.top - self._y) // self._h
        end = (self.bottom - self._y) // self._h + 1

        p1,p2 = sorted(((self._line,self._index),self._select))

        y = self._y + start * self._h
        for py,i in enumerate(self._splitted[start:end],start):
            x = self._x
            for px,j in enumerate(i.string):
                if py != self.NLINE:
                    self._src.blit(self._font.render(j,1,self.FGCOLOR),(x,y))
                else:
                    self._font.set_italic(1)
                    self._src.blit(self._font.render(j,1,self.HLCOLOR),(x,y))
                    self._font.set_italic(0)
                x += self._w
            y += self._h
        self._src.set_clip(clip)


class Form(pygame.Rect,object):

    def __init__(self,pos,width,fontsize,height=None,font=None,bg=(250,250,250),fgcolor=None,hlcolor=(180,180,200),curscolor=(0xff0000),maxlen=0,maxlines=0,maxWordsOnLne = 103):
        pygame.scrap.init()
        if not font: self.FONT = pygame.font.Font(pygame.font.match_font('mono',1),fontsize)
        elif type(font) == str: self.FONT = pygame.font.Font(font,fontsize)
        else: self.FONT = font
        try: self.BG = pygame.Color(*bg)
        except:self.BG = bg
        if not fgcolor:
            self.FGCOLOR = (255,255,255) if (self.BG.r*299 + self.BG.g*587 + self.BG.b*114) / 1000 < 125 else (0,0,0)
            try: self.FGCOLOR = (255,255,255) if (self.BG.r*299 + self.BG.g*587 + self.BG.b*114) / 1000 < 125 else (0,0,0)
            except: self.FGCOLOR = (0,0,0)
        else: self.FGCOLOR = fgcolor
        self.HLCOLOR = hlcolor
        self.CURSCOLOR = curscolor
        self._line = 0
        self._index = 0
        self.maxWordsOnLne = maxWordsOnLne
        self.MAXLINES = maxlines
        self.MAXLEN = maxlen
        self._splitted = ['']
        if not height: pygame.Rect.__init__(self,pos,(width,self.FONT.get_height()))
        else: pygame.Rect.__init__(self,pos,(width,height))
        self._x,self._y = pos
        self._src = pygame.display.get_surface()
        self._select = self._line,self._index
        self.TAB = 4
        self._adjust()
        self._cursor = True

    @property
    def INDEX(self):
        return self._line,self._index
    @INDEX.setter
    def INDEX(self,value):
        line,colum = value
        self._line,self._index = self._select = line,colum
        self._adjust()

    @property
    def CURSOR(self):
        return self._cursor
    @CURSOR.setter
    def CURSOR(self,value):
        self._cursor = value

    @property
    def HLCOLOR(self):
        return None
    @HLCOLOR.setter
    def HLCOLOR(self,color):
        self._hlsurface = pygame.Surface((self._w,self._h),pygame.SRCALPHA)
        self._hlsurface.fill(color)

    @property
    def OUTPUT(self):
        return '\n'.join(self._splitted)
    @OUTPUT.setter
    def OUTPUT(self,string):
        self._splitted = string.split('\n')


    @property
    def FONT(self):
        return self._font
    @FONT.setter
    def FONT(self,font):
        self._font = font
        self._w,self._h = self._font.size(' ')

    @property
    def SELECTION(self):
        p1,p2 = sorted(((self._line,self._index),self._select))
        if p1 != p2:
            selection = [len(i) for i in self._splitted[:p2[0]]]
            return self.OUTPUT[sum(selection[:p1[0]]) + p1[0] + p1[1]:sum(selection) + p2[0] + p2[1]:]
        return ''

    def _adjust(self):
        if self._index < len(self._splitted[self._line]):
            rcurs = pygame.Rect(self._x+self._index*self._w,self._y+self._line*self._h,self._w,self._h)
        else:
            rcurs = pygame.Rect(self._x+len(self._splitted[self._line])*self._w,self._y+self._line*self._h,1,self._h)

        self._rcursor = rcurs.clamp(self)
        self._x += self._rcursor.x - rcurs.x
        self._y += self._rcursor.y - rcurs.y

    def screen(self):
        clip = self._src.get_clip()
        self._src.set_clip(self.clip(clip))
        try: self._src.fill(self.BG,self)
        except: self._src.blit(self.BG,self)

        start = (self.top - self._y) // self._h
        end = (self.bottom - self._y) // self._h + 1

        p1,p2 = sorted(((self._line,self._index),self._select))

        y = self._y + start * self._h
        for py,i in enumerate(self._splitted[start:end],start):
            x = self._x
            for px,j in enumerate(i):
                if p1<=(py,px)<p2:
                    self._src.blit(self._hlsurface,(x,y))
                    self._src.blit(self._font.render(j,1,self.FGCOLOR),(x,y))
                else:
                    self._src.blit(self._font.render(j,1,self.FGCOLOR),(x,y))
                x += self._w
            y += self._h
        if self._cursor:
            pygame.draw.line(self._src,self.CURSCOLOR,self._rcursor.topleft,self._rcursor.bottomleft,1)
        self._src.set_clip(clip)

    def show(self):
        self.screen()
        pygame.display.update(self)

    def wakeup(self,ev):
        if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1: pyca.focus(self)
        self.update(ev)

    def clear(self):
        p1,p2 = sorted(((self._line,self._index),self._select))
        if p1 != p2:
            selection = [len(i) for i in self._splitted[:p2[0]]]
            self.OUTPUT = self.OUTPUT[:sum(selection[:p1[0]]) + p1[0] + p1[1]] + self.OUTPUT[sum(selection[:p2[0]]) + p2[0] + p2[1]:]
            self._select = self._line,self._index = p1
            return True

    def enter(self):
        self.clear()
        if not self.MAXLINES or self.OUTPUT.count('\n') < self.MAXLINES - 1:
            self._splitted[self._line] = self._splitted[self._line][:self._index] + '\n' + self._splitted[self._line][self._index:]
            self.OUTPUT = self.OUTPUT
            self._line += 1
            self._index = 0
            self._select = self._line,self._index

    def update(self,ev):

        line,index = self._line,self._index
        shift = pygame.key.get_pressed()
        shift = shift[pygame.K_RSHIFT]|shift[pygame.K_LSHIFT]
        ret = False

        if ev.type == pygame.KEYDOWN:

            if self._index >= self.maxWordsOnLne:
                self.enter()

            ret = True
            if ev.key == pygame.K_ESCAPE: ret = False
            elif ev.key == pygame.K_RIGHT:
                if self._index < len(self._splitted[self._line]):
                    self._index += 1
                elif self._line < len(self._splitted)-1:
                    self._index = 0
                    self._line += 1
                if not pygame.mouse.get_pressed()[0] and not shift: self._select = self._line,self._index

            elif ev.key == pygame.K_LEFT:
                if self._index > len(self._splitted[self._line]):
                    self._index = len(self._splitted[self._line])
                if self._index:
                    self._index -= 1
                elif self._line:
                    self._line -= 1
                    self._index = len(self._splitted[self._line])
                if not pygame.mouse.get_pressed()[0] and not shift: self._select = self._line,self._index

            elif ev.key == pygame.K_UP:
                if self._line: self._line -= 1
                if not pygame.mouse.get_pressed()[0] and not shift: self._select = self._line,self._index

            elif ev.key == pygame.K_DOWN:
                if self._line < len(self._splitted)-1: self._line += 1
                if not pygame.mouse.get_pressed()[0] and not shift: self._select = self._line,self._index

            elif ev.key == pygame.K_DELETE:
                if self._select == (self._line,self._index):
                    if self._index > len(self._splitted[self._line]):
                        self._index = len(self._splitted[self._line])
                        self._select = self._line + 1,0
                    else:
                        self._select = self._line,self._index + 1
                self.clear()

            elif ev.key == pygame.K_END:
                self._index = len(self._splitted[self._line])
                if not pygame.mouse.get_pressed()[0] and not shift: self._select = self._line,self._index

            elif ev.key == pygame.K_HOME:
                self._index = 0
                if not pygame.mouse.get_pressed()[0] and not shift and not shift: self._select = self._line,self._index

            elif ev.key == pygame.K_BACKSPACE:
                if self._select == (self._line,self._index):
                    
                    if self._index == 0:
                        if self._line:
                            self._select = self._line - 1,len(self._splitted[self._line - 1])
                            if self._line >=1:
                                self._line -= 1
                                self._index = self.maxWordsOnLne-1
                    else: self._select = self._line,self._index - 1
                    
                    if self._index > len(self._splitted[self._line]): 
                        self._index = len(self._splitted[self._line])
                    
                    #print self._select, self._index,self._line
                    
                self.clear()

            elif ev.key == pygame.K_TAB:
                self.clear()
                sp = self.TAB-self._index%self.TAB
                self._splitted[self._line] = self._splitted[self._line][:self._index] + ' '*sp + self._splitted[self._line][self._index:]
                self._index += sp
                self._select = self._line,self._index

            elif ev.key == pygame.K_RETURN or ev.key == pygame.K_KP_ENTER or ev.unicode == '\n':
                self.enter()

            elif ev.unicode and (not self.MAXLEN or len(self.OUTPUT) < self.MAXLEN):
                self.clear()
                self._splitted[self._line] = self._splitted[self._line][:self._index] + ev.unicode + self._splitted[self._line][self._index:]
                self._index += 1
                self._select = self._line,self._index

        elif ev.type == pygame.MOUSEBUTTONDOWN and self.collidepoint(ev.pos):
            if ev.button < 3:
                self._line = (ev.pos[1] - self._y) // self._h
                self._index = (ev.pos[0] - self._x) // self._w
                if ((ev.pos[0] - self._x) % self._w) > (self._w // 2): self._index += 1
                if self._line > len(self._splitted)-1:
                    self._line = len(self._splitted)-1
                    self._index = len(self._splitted[self._line])
                if self._index > len(self._splitted[self._line]): self._index = len(self._splitted[self._line])
                if self._index < 0: self._index = 0
                if ev.button == 2:
                    pygame.scrap.set_mode(pygame.SCRAP_SELECTION)
                    if not pygame.scrap.contains('UTF8_STRING'):
                        pygame.scrap.set_mode(pygame.SCRAP_CLIPBOARD)
                        if pygame.scrap.contains('UTF8_STRING'):
                            txt = pygame.scrap.get('UTF8_STRING')
                        else: txt = ''
                    else: txt = pygame.scrap.get('UTF8_STRING')
                    self._splitted[self._line] = self._splitted[self._line][:self._index] + txt + self._splitted[self._line][self._index:]
                    self.OUTPUT = self.OUTPUT
                    self._index += len(self.SELECTION)

                if self._select != (self._line,self._index): ret = True
                self._select = self._line,self._index

            elif ev.button == 4:
                y = self._y
                if self._y + self._h*3 > self.top: self._y = self.top
                else: self._y += self._h*3
                self._rcursor.move_ip(0,self._y-y)
                ret = True

            elif ev.button == 5:
                y = self._y
                h = len(self._splitted) * self._h
                if h > self.height:
                    if self._y - self._h*3 < self.bottom - h: self._y = self.bottom - h
                    else: self._y -= self._h*3
                    self._rcursor.move_ip(0,self._y-y)
                ret = True

        elif ev.type == pygame.MOUSEMOTION and ev.buttons[0] and self.collidepoint(ev.pos):
            self._line = (ev.pos[1] - self._y) // self._h
            self._index = ((ev.pos[0] - self._x) // self._w)
            if ((ev.pos[0] - self._x) % self._w) > (self._w // 2): self._index += 1
            if self._line > len(self._splitted)-1:
                self._line = len(self._splitted)-1
                self._index = len(self._splitted[self._line])
            if self._index > len(self._splitted[self._line]): self._index = len(self._splitted[self._line])
            if self._index < 0: self._index = 0
            pygame.scrap.put('UTF8_STRING',self.SELECTION)

        if (line,index) != (self._line,self._index):
            self._adjust()
            ret = True

        return ret

class NumForm(Form):
    def __init__(self,pos,fontsize,digit=1,font=None):
        Form.__init__(self,pos,0,fontsize,maxlines=1,maxlen=digit+2,bg=(255,255,255),font=font)
        self.width = self._w * (digit + 2)
        self._x = self.right
        self.CURSOR = 1
        self.OUTPUT = '0'
        self.digit = digit
        self.INDEX = 0,len(self.OUTPUT)

    def update(self,ev):
        if ev.type == pygame.KEYDOWN:
            if ev.key in (pygame.K_SPACE,pygame.K_TAB): return False
            if ev.key == pygame.K_ESCAPE: self.OUTPUT = ''
            if ev.unicode.isdigit() and len(self.OUTPUT)-('-'in self.OUTPUT)-('.'in self.OUTPUT) == self.digit and not self.SELECTION: return False
            elif ev.unicode == '-':
                if self.OUTPUT.startswith('-'): self.OUTPUT = self.OUTPUT[1:]
                else: self.OUTPUT = '-' + self.OUTPUT
                return True
            rem = self.OUTPUT
            super(NumForm,self).update(ev)
            try:
                float(self.OUTPUT)
                if ev.key != pygame.K_BACKSPACE:
                    if self.OUTPUT.startswith('0') and self.OUTPUT[1] != '.': self.OUTPUT = ev.unicode
                    elif self.OUTPUT.startswith('-0') and self.OUTPUT[2] != '.': self.OUTPUT = '-' + ev.unicode
                    self.OUTPUT = self.OUTPUT
                return True
            except:
                if not self.OUTPUT:
                    self.OUTPUT = '0'
                    self.INDEX = 0,len(self.OUTPUT)
                    return True
                elif self.OUTPUT == '-':
                    self.OUTPUT = '-0'
                    return True
                elif self.OUTPUT == '.':
                    self.OUTPUT = '0.'
                    return True
                self.OUTPUT = rem
                return False
        elif super(NumForm,self).update(ev): return True

    @property
    def OUTPUT(self):
        return '\n'.join(self._splitted)
    @OUTPUT.setter
    def OUTPUT(self,string):
        self._splitted = string.split('\n')
        self._x = self.right-len(self.OUTPUT)*self._w
        self._adjust()

class MenuForm(Form):

    def __init__(self,pos,width,fontsize,nblines,fontname=None,bg=(250,250,250),fgcolor=None,hlcolor=(180,180,200),curscolor=(0xff0000),maxlen=0,menu=[],label=''):
        Form.__init__(self,pos,width,fontsize,height=None,font=fontname,bg=bg,fgcolor=fgcolor,hlcolor=hlcolor,curscolor=curscolor,maxlen=maxlen,maxlines=1)
        self.OUTPUT = label
        self._index = len(label)
        self.scr = pygame.display.get_surface()
        self.box = Lister(menu,self.bottomleft,(self.width,self._h*nblines),fontsize,font=fontname)
        self.openbox = 0
        self.just_now = 0

    def update(self,ev):
        self.just_now = 0
        ret = super(MenuForm,self).update(ev)
        if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
            if self.openbox and not self.box.collidepoint(ev.pos):
                self.openbox = 0
                self.just_now = 1
                return True
            elif self.collidepoint(ev.pos):
                self.openbox = 1
                self.just_now = 1
                return True
        if self.openbox:
            if self.box.update(ev):
                self.OUTPUT = self.box.LINE[1:]
                self.INDEX = 0,len(self.OUTPUT)
                ret = True
            if ev.type == pygame.MOUSEBUTTONUP and ev.button == 1 and self.box.collidepoint(ev.pos):
                self.openbox = 0
                self.just_now = 1
                ret = True
        return ret

    def close(self):
        self.openbox = 0
        self.just_now = 1

    def screen(self):
        super(MenuForm,self).screen()
        if self.openbox:
            if self.just_now:
                self._bg = self.scr.subsurface(self.box).copy()
            self.box.screen()
            pygame.draw.rect(self.scr,(0,0,0),self.box,1)
        elif self.just_now:
            self.scr.blit(self._bg,self.box)

    def show(self):
        self.screen()
        if self.openbox or self.just_now: pygame.display.update((self,self.box))
        else: pygame.display.update(self)

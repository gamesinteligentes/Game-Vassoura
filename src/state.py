# coding: latin-1 
'''
Created on Jan 26, 2013

@author: fabiofilho
'''
from lib import Timer,BD,Text,Object,BaseMain,ObjectEvent,Animation,GameState,Text,Forms,Music,Sound,MenuForm,Form,ObjectRadio,ObjectThings,ObjectPoint
from objects import Actions,Fichas, DrawVector, Vassoura,Balance
from EmailConnection import Email
import pygame, os,sys
from pygame.locals import *
import time


pygame.init()


class Game(object):

    faseCur = 'IntroState'
    nextFase = ''
    beforeFase=''

    def __init__(self):

        pygame.init()

        #Chamada do construtor da classe base
        self.main = BaseMain()

        #Rodando Game
        self.runGame = True
        
        self.State = []
        self.loadMode = True
        
        #Set primeira tela
        self.fase = Game.faseCur
        pass

    def event(self):
        #Inicia a verificacao de enventos da classe
            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.runGame = False

                if event.type == pygame.QUIT:
                    self.runGame = False
                else:
                    #try:
                    self.CurrentState.event(event)
                    #except:pass


            if self.CurrentState.updateState:
                self.nextState()
                pass
            pass
        

    
    def load(self):
        
        self.s = pygame.time.get_ticks()/1000
        
        if self.loadMode and self.s >= 1:
                if not self.CurrentState.warm:
                    self.State = Load.load()   
                    self.State["Out"].faseCur = self.fase
                    self.State["Help"].faseCur = self.fase 
                    self.CurrentState.updateState = True        
                    self.loadMode = False
           
        pass        


    def play(self):
        
        self.CurrentState = Load()       
                
        #try:

        #Loop Principal
        while self.runGame and not self.CurrentState == False :
            
            self.dt = self.main.deltaTime()

            self.event()
            
            if not self.CurrentState or self.CurrentState == 'End':
                break
            
            #Atualiza os objetos da classe
            self.CurrentState.update(self.dt)
            
            #Pinta na tela
            self.main.draw(self.CurrentState)

            #Atualiza a tela
            self.main.updateScreen()
            
            #Carregando
            self.load()



        #except:
        #    if BD.testConnection():
        #        BD.send()
        #    print "Um erro inesperado....."

        pass

    def nextState(self):
        
       
        if self.CurrentState.NextCurrentState == "EndGame":
            self.CurrentState = self.State[self.CurrentState.NextCurrentState]
            return
     
        if not self.State[self.CurrentState.NextCurrentState]:
            self.CurrentState = self.State[self.CurrentState.NextCurrentState]
            return
        else:
            self.State[self.CurrentState.NextCurrentState].draw(self.main.tela)
            
            
            if not self.CurrentState.effect == None:
                self.CurrentState.updateState = Animation(self.CurrentState, self.State[self.CurrentState.NextCurrentState],self.main.telaCurrent,self.main.telaNext,self.CurrentState.effect).drawEffect(self.main.baseSurface,self.dt)
                
            else:
                self.CurrentState = self.State[self.CurrentState.NextCurrentState] 
                self.CurrentState.updateState = False
                try:
                    self.CurrentState.quest.updateState = False           
                except:
                    pass
                
                return

        self.CurrentState = self.State[self.CurrentState.NextCurrentState]
        
        try:
            self.CurrentState.NextCurrentState = self.CurrentState.StateTemp[1]
            self.CurrentState.updateState = False            
        except:
            pass
        try:
            self.CurrentState.quest.NextCurrentState = self.CurrentState.quest.StateTemp[0]
            self.CurrentState.quest.updateState = False           
        except:
            pass
        try :
            if not self.State["Out"] == self.CurrentState and not self.CurrentState.NextCurrentState == "Out":
                self.State["Out"].faseCur = self.CurrentState.CurrentState            
            if not self.State["Help"] == self.CurrentState and not self.CurrentState.NextCurrentState == "Out":
                self.State["Help"].faseCur = self.CurrentState.CurrentState
        except:
            pass
        
        pass




class Load(GameState):
    
    @staticmethod
    def load():
        return {"IntroState" : IntroState(),
                             "MainState" : MainState(),
                             "Final" : Final(),'Help':Help(),
                             "Fase1": Fase1(),"Fase3": Fase3(),
                             "Fase4": Fase4(),"Fase6": Fase6(),
                             "Fase8": Fase8(),"Fase10": Fase10(),
                             "Out": Out(), "Quit": False, "EndGame":'End'}

    
    def __init__(self):
        self.backGround = Object("src/Fases/Intro/fundo.png")
        self.updateState = False
        self.effect =None
        
        self.NextCurrentState = Game.faseCur
        
        self.text1 = Text("N�o h� conex�o com a internet! Se continuar, os registros ter�o de ser salvos manualmente.", 50, 70, 30, False, True,(255,0,0),(255,255,255),True)
        self.text2 = Text("Pressione Esc para sair. Caso contr�rio o jogo come�ar� em ", 150, 100, 30, False, True,(255,0,0),(255,255,255),True)  
        self.number = 5
        self.txtNumber = Text('5', 750, 100, 30, False, True,(255,0,0),(144,154,144),True)
        self.warm = False  
        self.testConn = True
        pass
    
    def draw(self,tela):
        self.backGround.draw(tela)
        if self.warm:
            self.text1.draw(tela)
            self.text2.draw(tela)
            self.txtNumber.draw(tela)
        pass
        
    def event(self,event):
        pass
    
    def update(self,dt):
        self.s = pygame.time.get_ticks()/1000
        
        if self.testConn:
            if not BD.testConnection():
                self.warm = False
                self.testConn = False
        
        self.number-=self.s
        
        self.txtNumber.setText(str(self.number))
        
        if self.number <= 0:
            self.warm = False
            pygame.time.wait(5000)
        
        pass    
    

class Out():

    def next(self):
        Sound("src/Fases/Botoes/btnSair.ogg").play()
        pygame.time.wait(200)
        self.updateState = True
        self.NextCurrentState = self.faseCur
        self.onePrintBackGround = True
        

    def out (self,stateOut):
        self.updateState = True
        self.NextCurrentState = "Quit"
        Sound("src/Fases/Botoes/btnSair.ogg").play()
        pygame.time.wait(100)
        BD.setText('O jogador saiu do jogo admitindo a seguinte frase: '+stateOut, self.faseCur) 
        #BD.send()
        
        
      
    def __init__(self):

        self.faseCur = ''
        self.updateState = False              
        self.effect =None

        self.backGround = Object("src/Fases/Sair/window2.png",200,100)
        self.window = Object("src/Fases/Sair/window.png",200,100)
        
        
        self.MainObjects = [ObjectEvent((295,195), "src/Fases/Sair/btnVoltar.png",
                                    "src/Fases/Sair/btnVoltar_move.png",None,self.next),
                            ObjectEvent((295,255), "src/Fases/Sair/btnSairNaoQuero.png",
                                        "src/Fases/Sair/btnSairNaoQuero_move.png",None,self.out),
                            ObjectEvent((295,315),"src/Fases/Sair/btnSairErrado.png",
                                        "src/Fases/Sair/btnSairErrado_move.png",None,self.out),
                            ObjectEvent((295,375), "src/Fases/Sair/btnSairCerto.png",
                                        "src/Fases/Sair/btnSairCerto_move.png",None,self.out),
                            ObjectEvent((295,435), "src/Fases/Sair/btnSairDesisto.png",
                                        "src/Fases/Sair/btnSairDesisto_move.png",None,self.out) ]
        
        
        self.MainObjects[1].setParameter('Não Quero mais jogar;')
        self.MainObjects[2].setParameter('Terminei mas acho que está errado.')
        self.MainObjects[3].setParameter('Terminei mas acho que está certo.')
        self.MainObjects[4].setParameter('Desisto.')
        
        self.onePrintBackGround = True
        
        pass
    

    def draw(self,tela):
        if self.onePrintBackGround:
            self.backGround.draw(tela)
            self.onePrintBackGround = False
            
        self.window.draw(tela)
        DrawVector(self.MainObjects,tela)
        pass
     

    def event(self,event):
        if event.type == pygame.MOUSEMOTION:
            for q in self.MainObjects:
                q.update(pygame.mouse.get_pos())

        if event.type == pygame.MOUSEBUTTONDOWN:
            for q in self.MainObjects:
                q.clickStart(pygame.mouse.get_pos())

        if event.type == pygame.MOUSEBUTTONUP:
            for q in self.MainObjects:
                if q.clickEnd(pygame.mouse.get_pos()):
                    return

        pass

    def update(self,dt):
        
        pass
    
    pass


class Help(GameState):

    state = 0


    def out (self):
        self.updateState = True
        #Sound("src/Fases/Botoes/btnSair.ogg").play()
        pygame.time.wait(100)
        self.NextCurrentState = self.faseCur
        self.onePrintBackGround = True

    def __init__(self):

        self.NextCurrentState = ''
        self.faseCur = ''
        self.updateState = False
        self.effect =None

        self.backGround = Object("src/Fases/Help/window2.png",100,50)
        
        self.window = Object("src/Fases/Help/window.png",100,50)
        
        self.asks = []
        
        for i in range(1,23):
            self.asks.append(Object('src/Fases/Help/txt/txt'+str(i)+'.png', 137 ,242))           
            pass
            
        
        self.MainObjects = ObjectEvent((820,80),"src/Fases/Help/btnFechar.png",
                                    "src/Fases/Help/btnFechar_move.png",None,self.out)
        
        self.onePrintBackGround = True
        pass

    def draw(self,tela):
        
        if self.onePrintBackGround:
            self.backGround.draw(tela)
            self.onePrintBackGround = False
            
        self.window.draw(tela)
        
        self.asks[Help.state].draw(tela)
        
        self.MainObjects.draw(tela)
                
        pass

    def event(self,event):
        if event.type == pygame.MOUSEMOTION:
            self.MainObjects.update(pygame.mouse.get_pos())

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.MainObjects.clickStart(pygame.mouse.get_pos())

        if event.type == pygame.MOUSEBUTTONUP:
            if self.MainObjects.clickEnd(pygame.mouse.get_pos()):
                return

        pass

    def update(self,dt):
        
        self.asks[Help.state].rect.x = (self.window.rect.x + self.window.image.get_width()/2)-self.asks[Help.state].image.get_width()/2
    
        pass
    
    pass



class IntroState(GameState):

    def __init__(self):
        self.backGround = Object("src/Fases/Intro/fundo.png")
        #self.backGround = Object("src/Fases/Fase1/fundo.png")
        Music("src/Fases/Intro/fundo.ogg").play()

        self.NextCurrentState = "MainState"
        self.updateState = False
        self.effect =2

        self.text = Text("  Aperte para iniciar o jogo!  ", BaseMain.size[0]/2-437/2, 490, 35, False, True,(255,255,255),(255,255,255))
        self.point = 1.0
        self.speed = 0.02
        #Email().send('binhor006@gmail.com', ['binhor009@yahoo.com.br','myriamkitz@gmail.com'], 'Testando o Envio do Jogo da Vassoura', 'Este email esta sendo enviando do jogo da vassoura', ['src/bd/form.txt'])
      
        pass

    def draw(self,tela):
        self.backGround.draw(tela)
        self.text.draw(tela)
        pass

    def event (self,event):
        if event.type == pygame.MOUSEBUTTONUP or event.type == pygame.MOUSEBUTTONDOWN:                        
            self.updateState = True
            pass


    def update(self,dt):
        
        if self.point > 1.3 or self.point < 1.0:
            self.speed *= -1
        
        self.point += self.speed    
        
        self.text.tranform(self.point)
        
        self.text.rect.x = BaseMain.size[0]/2-self.text.image.get_width()/2
        
        pass


class MainState(GameState):


    def next(self):
        
        if not self.FormNome.OUTPUT == '' and not self.ComboAnoEscolar.OUTPUT == ''and not self.ComboIdade.OUTPUT == '' and not self.school == '':
        
            Music.stop()
            Sound("src/Fases/Botoes/btnJogar.ogg").play()
            pygame.time.wait(200)
            self.updateState = True
            self.NextCurrentState = "Fase1"
            self.effect =2
            Music("src/Fases/Fase1/fundo.ogg").play(-1)
            self.warmming = False
            
            BD.formCadastro.append(self.FormNome.OUTPUT)            
            BD.formCadastro.append(self.ComboAnoEscolar.OUTPUT)
            BD.formCadastro.append(self.ComboIdade.OUTPUT)
            BD.formCadastro.append(self.school)
            BD.setDataForms()
                                   
            pass
        
        else:
            self.warmming = True            
            pass
            

    def out (self):
        self.updateState = True
        self.NextCurrentState = "Out"
        Sound("src/Fases/Botoes/btnSair.ogg").play()
        pygame.time.wait(200)
        self.effect =None

    def escolaParticular(self):
        self.school = "Particular"
                

    def escolaPublica (self):
        self.school = "Publica"
        

    def __init__(self):

        #Comandos referidos ao Forms e MenuForms
        self.cols = [' 8 anos',
                  ' 9 anos',
                  ' 10 anos',
                  ' 11 anos',
                  ' 12 anos',
                  ' 13 anos',
                  ' 14 anos',
                  ' 15 anos']

        self.cols2 = [' 1 Ano',
                    ' 2 Ano',
                    ' 3 Ano',
                    ' 4 Ano',
                    ' 5 Ano',
                    ' 6 Ano']

        self.font = os.path.join('src/Fonts/MonospaceTypewriter.ttf')

        self.Surface = pygame.Surface ((100,100))
        self.Surface2 = pygame.Surface ((500,500))
        self.Surface3 = pygame.Surface ((300,300))

        #Desenhando Forms

        #self.FormNome = Forms((490,233),195,fontsize=15,bg=(255,255,255),hlcolor=((90,40,40)),maxlines=1)
        #self.FormNome.CURSOR = False
        #self.Nome = "nome"

        self.FormNome = Form((490,235),195,12,font=self.font,hlcolor=(150,150,150),curscolor =(0,0,0),bg=(255,255,255))
        self.ComboIdade = MenuForm((483,273),208,12,8,fontname=self.font,menu=self.cols,hlcolor=(255,255,255),curscolor = (255,255,255),bg=(255,255,255))
        self.ComboAnoEscolar = MenuForm((483,312),208,12,6,fontname=self.font,menu=self.cols2,hlcolor=(255,255,255),curscolor = (255,255,255),bg=(255,255,255))

        #Carregando o vetor da fase pelo construtor
        self.backGround = Object("src/Fases/Main/fundo.png")

        self.MainObjects = [ObjectEvent((21,500), "src/Fases/Main/btnSair.png",
                                    "src/Fases/Main/btnSair_move.png",
                                    "src/Fases/Main/btnSair_click.png",self.out),
                            ObjectEvent((875,470),"src/Fases/Main/btnJogar.png",
                                    "src/Fases/Main/btnJogar_move.png",
                                    "src/Fases/Main/btnJogar_click.png",self.next),
                            ObjectRadio((330,355),"src/Fases/Main/btnEscolaPublica.png",
                                    "src/Fases/Main/btnEscolaPublica_click.png",
                                    "src/Fases/Main/btnEscolaPublica_click.png","Publica",self.escolaPublica),
                            ObjectRadio((505,355),"src/Fases/Main/btnEscolaParticular.png",
                                    "src/Fases/Main/btnEscolaParticular_click.png",
                                    "src/Fases/Main/btnEscolaParticular_click.png","Particular",self.escolaParticular)]


        self.CurrentState = "MainState"
        self.NextCurrentState = "Fase1"
        self.updateState = False
        self.effect = 0
        
        self.school = ""
        self.warmming = False
        self.text = Text("  Preencha todos os campos!  ", 240, 70, 38, False, True,(255,0,0),(255,255,255))
    
        pass


    def draw(self,tela):


        #Desenhando Forms
        #self.FormNome.show()

        self.FormNome.screen()

        self.ComboAnoEscolar.screen()
        self.ComboIdade.screen()

        #Pintando o vetor da fase
        self.backGround.draw(tela)
        DrawVector(self.MainObjects,tela)
        
        if self.warmming:
            self.text.draw(tela)
            pass

        pass


    def event (self,event):
            if event.type == pygame.MOUSEMOTION:
                for q in self.MainObjects:
                    q.update(pygame.mouse.get_pos())

            if event.type == pygame.MOUSEBUTTONDOWN:
                for q in self.MainObjects:
                    q.clickStart(pygame.mouse.get_pos())

            if event.type == pygame.MOUSEBUTTONUP:
                for q in self.MainObjects:
                    if q.clickEnd(pygame.mouse.get_pos()):
                        return

            '''item = self.FormNome
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if self.FormNome.collidepoint(event.pos):
                    item = self.FormNome
                item.CURSOR = True
                item.FGCOLOR = 0,0,0
                item.wakeup(event)
            else:
                item.wakeup(event)
                '''

            if self.FormNome.update(event):
                #print (self.FormNome.OUTPUT)
                pygame.draw.rect(self.Surface,(255,255,255)  if (0,0,0) else (0,0,0),self.FormNome, 1)
                self.FormNome.screen()

            elif self.ComboIdade.update(event):
                #print (self.ComboIdade.OUTPUT)
                pygame.draw.rect(self.Surface2,(255,255,255)  if (0,0,0) else (0,0,0),self.ComboIdade, 1)
                self.ComboIdade.screen()
                self.FormNome.CURSOR = False

            elif self.ComboAnoEscolar.update(event):
                #print (self.ComboAnoEscolar.OUTPUT)
                pygame.draw.rect(self.Surface3,(255,255,255)  if (0,0,0) else (0,0,0) ,self.ComboAnoEscolar,1)
                self.ComboAnoEscolar.screen()
                self.FormNome.CURSOR = False

     



    def update(self,dt):
              
        
        self.MainObjects[2].updateState(self.school)
        self.MainObjects[3].updateState(self.school)
        
        pass

    pass


class Fase1(GameState):

    def out (self):
        self.updateState = True
        
        self.NextCurrentState = "Out"
        Sound("src/Fases/Botoes/btnSair.ogg").play()
        pygame.time.wait(200)
        self.effect =None
        pass

    def next(self):
        self.NextCurrentState = "Fase3"
        self.updateState = True
        self.effect = 0
        Music.stop()
        Music("src/Fases/TellMe/fundo3.ogg").play(0)
        
        BD.setDataFases(self.CurrentState,self.actions, self.ficha,self.time.get_time())
        
    
    def help (self):
        self.NextCurrentState = 'Help'
        self.updateState = True
        Sound("src/Fases/Botoes/btnAjuda.ogg").play()
        self.effect =None
        pass

    def __init__(self):
       
        self.effect = 0

        #Carregando o vetor da fase pelo construtor

        self.backGround = Object("src/Fases/Fase1/fundo.png")

        self.MainObjects = [ObjectEvent((925,100), "src/Fases/Botoes/btnSetaDireita.png",
                                    "src/Fases/Botoes/btnSetaDireita_move.png",
                                    "src/Fases/Botoes/btnSetaDireita_click.png",self.next),
                            ObjectEvent((870,15),"src/Fases/Botoes/btnAjuda.png",
                                    "src/Fases/Botoes/btnAjuda_move.png",
                                    "src/Fases/Botoes/btnAjuda_click.png",self.help),
                            ObjectEvent((955,15),"src/Fases/Botoes/btnSair.png",
                                    "src/Fases/Botoes/btnSair_move.png",
                                    "src/Fases/Botoes/btnSair_click.png",self.out)]


        #========Vassoura
        self.base = Object("src/Fases/Vassoura/base.png",385,352)

        self.vas = Vassoura("Fase1")
        
        self.stateRotation = 'Center'

        self.balance = Balance(False)

        self.ficha = Fichas(faseCur="Fase1", vas=self.vas, base=self.base)

        self.CurrentState = "Fase1"
        self.NextCurrentState = "Fase3"
        self.updateState = False
        self.time = Timer()
        self.actions= Actions(BD.fase1Register,Help.state)
             

        pass

    def draw(self,tela):

        #Pintando o vetor da fase
        self.backGround.draw(tela)
        DrawVector(self.MainObjects,tela)
        
        #==========================VASSOURA===============================

        self.vas.draw(tela)
        self.balance.draw(tela,self.ficha.eixosLeft, self.ficha.eixosRight)
        self.base.draw(tela)
        self.ficha.draw(tela)

        pass

    def event (self,event):

        self.actions.event(event,self.time.get_time())

        self.ficha.event(event)

        if event.type == pygame.MOUSEMOTION:
            for q in self.MainObjects:
                q.update(pygame.mouse.get_pos())

        if event.type == pygame.MOUSEBUTTONDOWN:

            for q in self.MainObjects:
                q.clickStart(pygame.mouse.get_pos())

        if event.type == pygame.MOUSEBUTTONUP:
            for q in self.MainObjects:
                if q.clickEnd(pygame.mouse.get_pos()):
                    return
                pass
            pass


    def update(self,dt):
        
        self.time.updateTime()        
        
        Help.state = self.actions.state      
        
        #Setting State Rotate
        Vassoura.stateRotation = self.stateRotation

        self.ficha.update(dt,self.actions)
        self.vas.update(self.ficha,self.base,dt)



        print BD.fase1Register

        pass

    pass



class Fase3(GameState):

    def __init__(self):

        self.CurrentState = "Fase3"
        self.backGround = Object("src/Fases/TellMe/fundo3.png")
        self.quest = TellMe("Fase3","Fase4","Fase1",self.backGround)
        self.NextCurrentState = "Fase4"
        self.updateState = False
        self.effect = 0
        pass

    def draw(self,tela):
        self.quest.draw(tela)
        pass

    def event(self,event):

        self.quest.event(event)
        pass

    def update(self,dt):
        self.NextCurrentState = self.quest.NextCurrentState
        self.updateState = self.quest.updateState
        self.effect = self.quest.effect

        pass

    pass


class Fase4(GameState):

    def out (self):
        self.updateState = True
        self.NextCurrentState = "Out"
        Sound("src/Fases/Botoes/btnSair.ogg").play()
        pygame.time.wait(500)
        self.effect = None

    def back (self):
        self.updateState = True
        self.NextCurrentState = self.StateTemp[2]
        self.effect =1
        Music.stop()

    def next(self):
        self.updateState = True
        self.effect = 0
        Music.stop()
        Music("src/Fases/TellMe/fundo6.ogg").play(0)
        
        BD.setDataFases(self.CurrentState,self.actions, self.ficha,self.time.get_time())
        pass

    def help (self):
        self.NextCurrentState = 'Help'
        self.updateState = True
        Sound("src/Fases/Botoes/btnAjuda.ogg").play()
        pass

    
    def base(self):
        
        #Vass and Base

        base = self.base.rect.x + self.base.image.get_width()/2

        if self.base.rect.colliderect(self.stickBroom.rect):

            if self.stickBroom.rect.y > 332 and self.stickBroom.rect.y < 371 :
                self.plugged = True
                self.stickBroom.rect.y = 350



                if base < self.stickBroom.rect.x+(self.stickBroom.image.get_width()/5)*2:

                    self.ficha.eixosLeft,self.ficha.eixosRight = self.balance.setLeft(self.stickBroom,self.ficha.eixosLeft,self.ficha.eixosRight)
                    self.ficha.weightLeft,self.ficha.weightRight = self.balance.setLeft(self.stickBroom, self.ficha.weightLeft,self.ficha.weightRight, False)
                    self.base.rect.x = Balance.posBase-self.base.image.get_width()/2                    
                    self.modeBalance = True
                    Sound("src/Fases/Fase4/vassLeft.ogg").play()                                        
                    pass

                if base >= self.stickBroom.rect.x+(self.stickBroom.image.get_width()/5)*2 and base <= self.stickBroom.rect.x+(self.stickBroom.image.get_width()/5)*3:
                    
                    self.ficha.eixosLeft,self.ficha.eixosRight = self.balance.setCenter(self.stickBroom,self.ficha.eixosLeft,self.ficha.eixosRight)
                    self.ficha.weightLeft,self.ficha.weightRight = self.balance.setCenter(self.stickBroom, self.ficha.weightLeft,self.ficha.weightRight, False)
                    self.base.rect.x = Balance.posBase-self.base.image.get_width()/2
                    self.modeBalance = True
                    Sound("src/Fases/Fase4/vassLeft.ogg").play()
                    pass

                if base > self.stickBroom.rect.x+(self.stickBroom.image.get_width()/5)*3:
                    
                    self.ficha.eixosLeft,self.ficha.eixosRight = self.balance.setRight(self.stickBroom,self.ficha.eixosLeft,self.ficha.eixosRight)
                    self.ficha.weightLeft,self.ficha.weightRight = self.balance.setRight(self.stickBroom, self.ficha.weightLeft,self.ficha.weightRight, False)
                    self.base.rect.x = Balance.posBase-self.base.image.get_width()/2
                    self.modeBalance = True
                    Sound("src/Fases/Fase4/vassLeft.ogg").play()
                    pass
                
                self.stateRotation = Vassoura.stateRotation
                self.ficha.rotate = True
                self.base.oldPos = self.base.rect.x,self.base.rect.y
                pass
            pass
        
    def resetStateOfBroom(self):
        self.stickBroom.image = self.stickBroom.oldIdle
        self.stickBroom.rect = self.stickBroom.oldRect
        self.modeBalance = False
        self.stateRotation = ''
        self.ficha.rotate = False                
        pass
    
    def newPosOtherObjects(self,obj):
        
        for i in self.things:
                
            if obj.rect.colliderect(i): 
                                   
                if i.enable and not i.plugged:
                    i.enable = False
                    i.plugged = True
                    i.objectPlugged = obj
                    obj.plugged = True
  
            else:
                
                if obj.plugged:
                    
                    obj.plugged = False
                    i.plugged = False
                    i.enable = True
                    i.objectPlugged = None     
                    
                    
                    if not self.things[0].plugged:
                        self.things[1].plugged = False
                        self.things[1].enable = False
                        self.things[1].objectPlugged = None
                        
                    if not self.things[3].plugged:
                        self.things[2].plugged = False
                        self.things[2].objectPlugged = None
                        self.things[2].enable = False
                        
                
        pass    
    
    def adorno(self):
                
        self.newPosOtherObjects(self.OthersObjects[0])
        
        pass  
    
    def varrer(self):
        self.newPosOtherObjects(self.OthersObjects[1])
        pass
    
     


    def __init__(self):

        #Carregando o vetor da fase pelo construtor

        self.backGround = Object("src/Fases/Fase4/fundo.png")


        self.StateTemp = ["Fase4","Fase6","Fase3"]
        self.CurrentState = self.StateTemp[0]
        self.NextCurrentState = self.StateTemp[1]
        self.updateState = False
        self.effect = 0

        self.modeBalance = False
        self.plugged = False

        self.OthersObjects = [ObjectThings([50,450], "src/Fases/Fase4/adorno.png",
                                           'Adorno',None, None,self.adorno),
                              ObjectThings([300,450], "src/Fases/Fase4/varrer.png",
                                           'Varrer',None, None,self.varrer)]



        self.MainObjects = [ObjectEvent((925,100), "src/Fases/Botoes/btnSetaDireita.png",
                                    "src/Fases/Botoes/btnSetaDireita_move.png",
                                    "src/Fases/Botoes/btnSetaDireita_click.png",self.next),
                            ObjectEvent((15,100), "src/Fases/Botoes/btnSetaEsquerda.png",
                                    "src/Fases/Botoes/btnSetaEsquerda_move.png",
                                    "src/Fases/Botoes/btnSetaEsquerda_click.png",self.back),
                            ObjectEvent((870,15),"src/Fases/Botoes/btnAjuda.png",
                                    "src/Fases/Botoes/btnAjuda_move.png",
                                    "src/Fases/Botoes/btnAjuda_click.png",self.help),
                            ObjectEvent((955,15),"src/Fases/Botoes/btnSair.png",
                                    "src/Fases/Botoes/btnSair_move.png",
                                    "src/Fases/Botoes/btnSair_click.png",self.out)]


        #========Vassoura

        #self.base = ObjectEvent((740,350),"src/Fases/Vassoura/base.png",None,None,self.base)
        self.base = ObjectEvent((500,350),"src/Fases/Vassoura/base.png",None,None,self.base)

        self.vas = Vassoura("Fase4",True)

        self.stateRotation = ''

        #self.stickBroom = ObjectEvent([10,550],
        self.stickBroom = self.vas.vas
        
        self.objects = self.MainObjects

        for i in self.OthersObjects:
            self.objects.append(i)

        self.objects.append(self.base)

        self.balance = Balance(True)

        self.ficha = Fichas("Fase4",self.vas,self.objects,self.base)

        srcThings = 'src/Fases/Fase4/point.png'
        self.things = [ObjectPoint(srcThings,self.stickBroom.rect.x-12,
                                       self.stickBroom.rect.y),
                       
                       ObjectPoint(srcThings,self.stickBroom.rect.x-12,
                                   self.stickBroom.rect.y-17),
                       
                       ObjectPoint(srcThings,
                                   self.stickBroom.rect.x+self.stickBroom.image.get_width(),
                                          self.stickBroom.rect.y),
                       
                       ObjectPoint(srcThings,
                                   self.stickBroom.rect.x+self.stickBroom.image.get_width(),
                                        self.stickBroom.rect.y-self.stickBroom.image.get_height()),]
            
            
            
        self.time = Timer()
        self.actions = Actions(BD.fase4Register, Help.state)    
        pass


    def draw(self,tela):

        #Pintando o vetor da fase
        self.backGround.draw(tela)

        self.stickBroom.draw(tela)

        #DrawVector(self.things,tela)

        DrawVector(self.MainObjects,tela)
        
        self.balance.draw(tela, self.ficha.eixosLeft,self.ficha.eixosRight)

        DrawVector(self.OthersObjects, tela)

        self.base.draw(tela)

        self.ficha.draw(tela)


        pass

    def event (self,event):

        self.ficha.event(event)
        self.vas.event(event)
        
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_w:
                self.updateState = True
                self.NextCurrentState = 'EndGame'
                self.effect = 0
                return
        
        if event.type == pygame.MOUSEMOTION:
            for q in self.MainObjects:
                q.update(pygame.mouse.get_pos())

        if event.type == pygame.MOUSEBUTTONDOWN:
                        
            for ob in self.OthersObjects:
                ob.clickStart(pygame.mouse.get_pos())

            self.base.clickStart(pygame.mouse.get_pos())
            self.stickBroom.clickStart(pygame.mouse.get_pos())

            for q in self.MainObjects:
                q.clickStart(pygame.mouse.get_pos())

        if event.type == pygame.MOUSEBUTTONUP:
            
            for ob in self.OthersObjects:
                ob.clickEnd(pygame.mouse.get_pos())

            self.base.clickEnd(pygame.mouse.get_pos())
            self.stickBroom.clickEnd(pygame.mouse.get_pos())

            for q in self.MainObjects:
                if q.clickEnd(pygame.mouse.get_pos()):
                    return
                pass
            pass


    def update(self,dt):
        
        #Setting State Rotate
        Vassoura.stateRotation = self.stateRotation
        

        if self.modeBalance:
            self.vas.update(self.ficha,self.base,dt)
        
        self.ficha.update(dt,self.actions,self.stickBroom)
        
        self.time.updateTime()        
        
        Help.state = self.actions.state   
        
        #Outros Objetos
        
        for ob in self.OthersObjects:
            #if ob.rect.x > self.stickBroom.rect.x+self.stickBroom.image.get_width()/2:
            if ob.rect.x > self.base.rect.x+self.base.image.get_width()/2:
                ob.oldIdle = ob.image = ob.reverseIdle
            else :
                ob.oldIdle = ob.image = ob.idle
            
            ob.plugged = False
                
        
        for i in self.things:
            i.enable = False
            i.plugged = False
            i.objectPlugged = None
        
        self.things[0].enable = True
        self.things[2].enable = True           

        self.things[0].rect.x,self.things[0].rect.y =  self.stickBroom.rect.x-self.things[0].image.get_width(),self.stickBroom.rect.y
        self.things[1].rect.x,self.things[1].rect.y = self.stickBroom.rect.x-self.things[1].image.get_width(),self.stickBroom.rect.y-self.things[1].image.get_height()
        self.things[3].rect.x,self.things[3].rect.y =self.stickBroom.rect.x+self.stickBroom.image.get_width(),self.stickBroom.rect.y-self.stickBroom.image.get_height()
        self.things[2].rect.x,self.things[2].rect.y =self.stickBroom.rect.x+self.stickBroom.image.get_width(),self.stickBroom.rect.y 

            
        
        for things in self.things:
            for others in self.OthersObjects:
                
                if others.rect.colliderect(things) and things.enable :
                    
                    others.rect.x,others.rect.y = things.rect.x,things.rect.y
                    things.enable = False
                    things.plugged = True
                    things.objectPlugged = others
                    
                    nameAux = 'Adorno'
                    
                    
                    #Left Down
                    if self.things[0]== things:
                        
                        self.things[1].enable = True    
                            
                        
                        if others.name == nameAux:
                            self.things[1].rect.y -= self.OthersObjects[1].image.get_height()-15
                            others.rect.y -= others.image.get_height()/5-3
                        else:
                            self.things[1].rect.y -= self.OthersObjects[0].image.get_height()
                            others.rect.y -=(others.image.get_height()/3)*1.1
                            
                            
                        others.rect.x += 15
                        #others.rect.x += things.image.get_width()
                        
                       
                        #others.rect.y -= others.image.get_height()/2

                    
                    #Right Down
                    if self.things[2]== things:
                        
                        self.things[3].enable = True
                                                
                        if others.name == nameAux:                             
                            self.things[3].rect.y -= self.OthersObjects[1].image.get_height()-15
                            others.rect.y -= others.image.get_height()/5
                        else:
                            self.things[3].rect.y -= self.OthersObjects[0].image.get_height()
                            others.rect.y-=(others.image.get_height()/3)*1.1
                            
                        others.rect.x -= 18
                         
                    
                    #Left UP
                    if self.things[1]== things:                        
                        others.rect.x +=20                                           
                        pass
                    
                    #Right UP
                    if self.things[3]== things:                        
                        others.rect.x -=20                                           
                        pass
                          
                        
                        
        #testes     
        '''
        print self.things[2].enable,self.things[2].plugged
                        
        a = -1
        for t in self.things:
            a+=1            
            if t.objectPlugged is not None and t.objectPlugged.name == 'Adorno':
                print a
        '''
                    

        for things in self.things:
            
            for b in range(2):
                if things.plugged and things.objectPlugged.name == self.OthersObjects[b].name:
                    index = b
                else:
                    index = None
                    
            if self.stateRotation == 'Center':
                things.rotate(self.vas.angle)
                if things.plugged :                      
                    self.OthersObjects[index].rotate(self.vas.angle)
                    
                    
            elif self.stateRotation == 'Left':
                things.rotateLeft(self.vas.angle,self.vas.MAXangle,self.vas.MINangle,things.image.get_width())
                if things.plugged :
                    self.OthersObjects[index].rotateLeft(self.vas.angle,self.vas.MAXangle,self.vas.MINangle,self.OthersObjects[index].image.get_width())
                    
                    
            elif self.stateRotation == 'Right':
                things.rotateRight(self.vas.angle,self.vas.MAXangle,self.vas.MINangle,things.image.get_width())
                if things.plugged :
                    self.OthersObjects[index].rotateRight(self.vas.angle,self.vas.MAXangle,self.vas.MINangle,self.OthersObjects[index].image.get_width())

      
            
        can = True
        for i in self.ficha.objectFichas:
            if i.state == 'Clicking':
                can = False

        if can:
            
            for ob in self.OthersObjects:
                if ob.state == "Clicking":
                    x,y = pygame.mouse.get_pos()
                    ob.rect.x ,ob.rect.y =   x -ob.rect.width/2, y -ob.rect.height/2
    
    
                #Verificacao de positicao do adorno e da base
    
            #Base da Vassoura
    
            if self.base.state == "Clicking" and not self.OthersObjects[0].state == "Clicking" and not self.OthersObjects[1].state == "Clicking" and not self.stickBroom.state == "Clicking" :
                x,y = pygame.mouse.get_pos()
                self.base.rect.x  = x - self.base.rect.width/2
    
            #Vassoura
            if self.modeBalance and can:
                if self.stickBroom.state == 'Clicking' or self.base.oldPos != (self.base.rect.x,self.base.rect.y):
                    self.resetStateOfBroom()
                
            if self.stickBroom.state == "Clicking" and self.OthersObjects[0].state == "Idle" and self.OthersObjects[1].state == "Idle":
                x,y = pygame.mouse.get_pos()
                self.stickBroom.rect.x ,self.stickBroom.rect.y =   x -self.stickBroom.rect.width/2, y -self.stickBroom.rect.height/2
                self.base.state = "Idle"
            
            if self.stickBroom.rect.y > 332 and self.stickBroom.rect.y < 371 :
                self.plugged = True
            else:
                self.plugged = False
                #self.modeBalance = False
            
            #print self.plugged,self.modeBalance
        

        if self.stickBroom.state == "Idle":

            loop = True
            while loop:
                if self.stickBroom.rect.y <= 160:
                    self.stickBroom.rect.y +=1
                else: loop = False

            if self.stickBroom.rect.x < 0 :
                self.stickBroom.rect.x = 0
            elif self.stickBroom.rect.x+self.stickBroom.image.get_width() > 1024:
                self.stickBroom.rect.x = 1024-self.stickBroom.image.get_width()
                pass
            pass

        
        
            
class Fase6(GameState):

    def __init__(self):

        self.CurrentState = "Fase6"
        self.backGround = Object("src/Fases/TellMe/fundo6.png")
        self.quest = TellMe("Fase6","Fase8","Fase4",self.backGround)
        self.NextCurrentState = "Fase7"
        self.updateState = False
        self.effect =0
        pass

    def draw(self,tela):
        self.quest.draw(tela)
       
        pass

    def event(self,event):

        self.quest.event(event)

        pass

    def update(self,dt):
        self.NextCurrentState = self.quest.NextCurrentState
        self.updateState = self.quest.updateState
        self.effect = self.quest.effect
        pass

    pass

class Fase8(GameState):

    def out (self):
        self.updateState = True
        self.NextCurrentState = "Out"
        Sound("src/Fases/Botoes/btnSair.ogg").play()
        pygame.time.wait(500)
        self.effect =None
        pass

    def next(self):
        self.NextCurrentState = "Fase10"
        self.updateState = True
        self.effect = 0
        Music.stop()
        Music("src/Fases/TellMe/fundo10.ogg").play(0)
        BD.setDataFases(self.CurrentState,self.actions, self.ficha,self.time.get_time())
        pass

    def back (self):
        self.updateState = True
        self.NextCurrentState = self.StateTemp[2]
        self.effect =1
        Music.stop()


    def help (self):
        self.NextCurrentState = 'Help'
        self.updateState = True
        self.effect =None
        Sound("src/Fases/Botoes/btnAjuda.ogg").play()
        pass

    def __init__(self):

        self.effect = 0

        #Carregando o vetor da fase pelo construtor


        self.backGround = Object("src/Fases/Fase8/fundo.png")
        self.StateTemp = ["Fase8","Fase10","Fase6"]

        self.CurrentState  = self.NextCurrentState = self.StateTemp[0]
        self.updateState = False
        self.effect = 0

        self.MainObjects = [ObjectEvent((925,100), "src/Fases/Botoes/btnSetaDireita.png",
                                    "src/Fases/Botoes/btnSetaDireita_move.png",
                                    "src/Fases/Botoes/btnSetaDireita_click.png",self.next),
                            ObjectEvent((15,100), "src/Fases/Botoes/btnSetaEsquerda.png",
                                    "src/Fases/Botoes/btnSetaEsquerda_move.png",
                                    "src/Fases/Botoes/btnSetaEsquerda_click.png",self.back),
                            ObjectEvent((870,15),"src/Fases/Botoes/btnAjuda.png",
                                    "src/Fases/Botoes/btnAjuda_move.png",
                                    "src/Fases/Botoes/btnAjuda_click.png",self.help),
                            ObjectEvent((955,15),"src/Fases/Botoes/btnSair.png",
                                    "src/Fases/Botoes/btnSair_move.png",
                                    "src/Fases/Botoes/btnSair_click.png",self.out)]

        
        #========Vassoura
        self.vas = Vassoura('Fase8')

        self.base = Object("src/Fases/Vassoura/base.png",577,350)

        self.balance = Balance(False)
        
        self.stateRotation = 'Right'
        
        self.ficha = Fichas(faseCur="Fase8",vas=self.vas, base=self.base)
        
        self.ficha.eixosLeft,self.ficha.eixosRight = self.balance.setRight(self.vas.vas, self.ficha.eixosLeft,self.ficha.eixosRight)
        self.ficha.weightLeft,self.ficha.weightRight = self.balance.setRight(self.vas.vas, self.ficha.weightLeft,self.ficha.weightRight, False)
        
        print len(self.ficha.eixosLeft),len(self.ficha.eixosRight)
        
        self.CurrentState = "Fase8"
        self.NextCurrentState = "Fase10"
        self.updateState = False
        
        self.time = Timer()
        self.actions = Actions(BD.fase8Register, Help.state)
                
        pass

    def draw(self,tela):

        #Pintando o vetor da fase
        self.backGround.draw(tela)
        DrawVector(self.MainObjects,tela)

        self.base.draw(tela)

        #==========================VASSOURA===============================

        self.vas.draw(tela)
        self.balance.draw(tela,self.ficha.eixosLeft, self.ficha.eixosRight)
        self.base.draw(tela)
        self.ficha.draw(tela)
        
        pass

    def event (self,event):

        self.ficha.event(event)
   
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.ficha.resultWeigth2+=10
            if event.key == pygame.K_RIGHT:
                self.ficha.resultWeigth2-=10
            print self.ficha.resultWeigth2
   
        if event.type == pygame.MOUSEMOTION:
            for q in self.MainObjects:
                q.update(pygame.mouse.get_pos())

        if event.type == pygame.MOUSEBUTTONDOWN:            
            for q in self.MainObjects:
                q.clickStart(pygame.mouse.get_pos())

        if event.type == pygame.MOUSEBUTTONUP:
            for q in self.MainObjects:
                if q.clickEnd(pygame.mouse.get_pos()):
                    return
                pass
            pass


    def update(self,dt):

        self.time.updateTime()        
        
        Help.state = self.actions.state   

        #Setting State Rotate
        Vassoura.stateRotation = self.stateRotation

        self.ficha.update(dt,self.actions)

        self.vas.update(self.ficha,self.base,dt)
                                    
        #print self.ficha.weightLeftPlugged [0][0],self.ficha.resultWeigth
        
        
        pass

    pass


class Fase10(GameState):

    def __init__(self):

        self.CurrentState  = "Fase10"
        self.backGround = Object("src/Fases/TellMe/fundo10.png")
        self.quest = TellMe("Fase10","Final","Fase8",self.backGround)
        self.updateState = False
        self.NextCurrentState = "Final"
        self.effect =0
        pass

    def draw(self,tela):
        self.quest.draw(tela)
        pass

    def event(self,event):

        self.quest.event(event)
        pass

    def update(self,dt):
        self.NextCurrentState = self.quest.NextCurrentState
        self.updateState = self.quest.updateState
        self.effect = self.quest.effect
        pass

    pass




class Final:

    def __init__(self):

        self.backGround = Object("src/Fases/Final/fundo.png")

        self.NextCurrentState = "EndGame"
        self.updateState = False
        self.effect =0
        self.send = True
                
        pass

    def draw(self,tela):
        self.backGround.draw(tela)
        pass

    def event(self,event):
        if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            self.updateState = True

        pass

    def update(self,dt):
        
        if self.send:
            BD.send()
            send = False
        pass

    pass



class TellMe:

    def out (self):
        self.updateState = True
        self.NextCurrentState = "Out"
        Sound("src/Fases/Botoes/btnSair.ogg").play()
        pygame.time.wait(500)
        self.effect =None
        
    def set_Music(self):
        Music.stop()
        if self.NextCurrentState == "Fase1":
            Music("src/Fases/Fase1/fundo.ogg").play(-1)
        elif self.NextCurrentState == "Fase4":
            Music("src/Fases/Fase4/fundo.ogg").play(-1)
        elif self.NextCurrentState == "Fase8":
            Music("src/Fases/Fase8/fundo.ogg").play(-1)

        pass

    def next(self):
        self.updateState = True
        self.NextCurrentState = self.StateTemp[1]
        self.effect =0
        self.set_Music()
        
        
        if self.StateTemp[0]== 'Fase3':
            BD.fase3Register=self.FormFase.OUTPUT
            BD.setDataFase3()
            pass
        
        if self.StateTemp[0]== 'Fase6':
            BD.fase6Register=self.FormFase.OUTPUT
            BD.setDataFase6()
            pass
        
        if self.StateTemp[0]== 'Fase10':
            BD.fase10Register=self.FormFase.OUTPUT
            BD.setDataFase10()
            pass
        
        pass

    def back (self):
        self.updateState = True
        self.NextCurrentState = self.StateTemp[2]
        self.effect =1
        self.set_Music()
        pass

    def __init__(self,faseCurrent,faseNext,faseBack,backGround):

        #Carregando o vetor da fase pelo construtor
        self.backGround = backGround

        self.MainObjects = [ObjectEvent((925,535), "src/Fases/Botoes/btnSetaDireita.png",
                                    "src/Fases/Botoes/btnSetaDireita_move.png",
                                    "src/Fases/Botoes/btnSetaDireita_click.png",self.next),
                            ObjectEvent((15,535),"src/Fases/Botoes/btnSetaEsquerda.png",
                                    "src/Fases/Botoes/btnSetaEsquerda_move.png",
                                    "src/Fases/Botoes/btnSetaEsquerda_click.png",self.back),
                            ObjectEvent((955,15),"src/Fases/Botoes/btnSair.png",
                                    "src/Fases/Botoes/btnSair_move.png",
                                    "src/Fases/Botoes/btnSair_click.png",self.out)]

        self.StateTemp = [faseCurrent,faseNext,faseBack]
        self.NextCurrentState = self.StateTemp[0]
        self.updateState = False
        self.effect =0
        
        
        #Comandos para o Forms
        self.font = os.path.join('src/Fonts/MonospaceTypewriter.ttf')
        self.Surface = pygame.Surface ((100,100))
        self.FormFase = Form((146,213),730,12,300,font=self.font,hlcolor=(150,150,150),curscolor =(0,0,0),bg=(255,255,255))

        pass



    def draw(self,tela):

        self.backGround.draw(tela)
        DrawVector(self.MainObjects,tela)
        self.FormFase.screen()
        pass

    def event(self,event):
        
            if event.type == pygame.MOUSEMOTION:
                for q in self.MainObjects:
                    q.update(pygame.mouse.get_pos())

            if event.type == pygame.MOUSEBUTTONDOWN:
                for q in self.MainObjects:
                    q.clickStart(pygame.mouse.get_pos())

            if event.type == pygame.MOUSEBUTTONUP:
                for q in self.MainObjects:
                    q.clickEnd(pygame.mouse.get_pos())
        
            if self.FormFase.update(event):
                pygame.draw.rect(self.Surface,(255,255,255)  if (0,0,0) else (0,0,0),self.FormFase, 1)
                self.FormFase.screen()



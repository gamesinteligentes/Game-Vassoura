# coding: latin-1 
'''
Created on Jan 22, 2013

@author: fabiofilho
'''
import pygame
from state import Game

while True:
    
    if __name__ == "__main__":
        game = Game()
        
        game.play()
        
        if game.runGame == False or game.CurrentState == False:
            break            
    
    
pygame.quit()
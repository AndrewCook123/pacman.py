#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 18:13:58 2023

@author: corydragun
"""
import pygame
from pauseGUI import Pause
import saveGUI

class VictoryGui(object):
    def __init__(self, screen,font,level,lives,date,score):
        self.lives=lives
        self.level=level
        self.date=date
        self.score=score
        self.clicked_next=False
        self.screen=screen
        self.font=font
        self.timer=0
        self.check=False
        self.clicked=False
        self.new=saveGUI.SaveGui(self.screen, self.font,self.level,self.lives,self.date,self.score)
        
    def victory(self):
        self.new.set_level(self.level)
        self.new.set_lives(self.lives)
        self.new.set_score(self.score)
        pos = pygame.mouse.get_pos()
        pygame.draw.rect(self.screen, 'white', [50, 200, 800, 300],0, 10)
        pygame.draw.rect(self.screen, 'dark gray', [70, 220, 760, 260], 0, 10)
        top=pygame.draw.rect(self.screen, 'blue', [350, 350, 150, 50], 0, 10)
        start_text = self.font.render(f'Next Level->', True, 'white')
        self.screen.blit(start_text, (365, 370))
        if top.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked_next = True
                #self.clicked=True
        if self.clicked_next:
                if self.timer<180:
                    self.timer+=1
                else:
                    if not self.new.display_save():
                        self.new.display_save()
                    else:
                        self.clicked=True
                        
        
                
        
        if pygame.mouse.get_pressed()[0] == 0:
            pass
        return self.clicked
    def set_level(self,level):
        self.level = level
    def set_lives(self,lives):
        self.lives = lives
    def set_score(self,score):
        self.score = score

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 18:46:04 2023

@author: corydragun
"""

import pygame
import LoadGUI


class StartGui(object):
    def __init__(self, screen,font)->None:
        self.clicked_start=False
        self.clicked_load=False
        self.screen=screen
        self.font=font
        self.timer=0
        self.new=LoadGUI.LoadGui(self.screen,self.font)
        self.Mainfont=pygame.font.Font('freesansbold.ttf', 40)
        self.score = 0
        self.lives = 0
        self.level = 0
        
        
        
        
    def start(self):
        self.score = self.new.get_score()
        self.lives = self.new.get_lives()
        self.level = self.new.get_level()
        pos = pygame.mouse.get_pos()
        pygame.draw.rect(self.screen, 'white', [50, 200, 800, 300],0, 10)
        pygame.draw.rect(self.screen, 'dark gray', [70, 220, 760, 260], 0, 10)
        start=pygame.draw.rect(self.screen, 'Blue', [275, 400, 150, 50], 0, 10)
        start_text = self.font.render(f'START->', True, 'white')
        self.screen.blit(start_text, (305, 420))
        load=pygame.draw.rect(self.screen, 'Blue', [475, 400, 150, 50], 0, 10)
        start_text = self.font.render(f'Load->', True, 'white')
        self.screen.blit(start_text, (515, 420))
        MainMenu_text = self.Mainfont.render(f'Pac-Man', True, 'white')
        self.screen.blit(MainMenu_text, (350, 300))
        self.check=False
        
        if start.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked_start = True
                self.status=True
        if self.clicked_load:
            self.status=False
        if pygame.mouse.get_pressed()[0] == 0:
            pass
        if load.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked_load=True
        if self.clicked_load:
            if self.timer<180:
                self.timer+=1
            else:
                clicked = self.new.load()
                if not self.check:
                    if not clicked:
                        self.clicked_start=False
                        self.new.load()
                else:
                    self.clicked_start=self.clicked_start
                    self.check=True
                    
            
            
                
       
        
            
        
            
        
        if pygame.mouse.get_pressed()[0] == 0:
            pass
        
        return self.clicked_start
    def set_status(self, status):
        self.status = status
    def set_load(self, clickedLoad):
        self.clicked_load = clickedLoad
    def get_score(self):
        self.score = self.new.get_score()
        return self.score
    def get_lives(self):
        self.lives = self.new.get_lives()
        return self.lives
    def get_level(self):
        self.level = self.new.get_level()
        return self.level
    def set_score(self,score):
        self.score = score
    def set_lives(self,lives):
        self.lives = lives
    def set_level(self,level):
        self.level = level

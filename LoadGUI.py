#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 01:06:22 2023

@author: corydragun
"""

import pygame
import startGUI
import sqlite3



class LoadGui(object):
    def __init__(self, screen:list,font:str)->None:
        self.screen=screen
        self.font=font
        self.check=False
        self.timer=0
        self.clicked_back=False
        self.connection=sqlite3.connect("pacman.db")
        self.clicked_load=False
        self.Mainfont=pygame.font.Font('freesansbold.ttf', 40)
        self.clicked = False
        self.score = 0
        self.lives = 0
        self.level = 0
        
        
        
        
        
    def load(self)-> bool:
        ''' This function will display the saved games and when a player has 
        selected a saved game then that saved game will begin'''
        index=0
        lyst = []
        self.connection.execute(''' CREATE TABLE IF NOT EXISTS PACMANGAMES
                          (SAVENAME TEXT PRIMARY KEY NOT NULL,
                        LEVEL INT NOT NULL,
                        LIVES INT NOT NULL,
                        DATESAVE TEXT NOT NULL,
                        SCORE INT NOT NULL);''')
        s=''
        s1=''
        s2=''
        font=pygame.font.Font('freesansbold.ttf', 13)
        selector2=self.connection.execute("SELECT SAVENAME,LEVEL, LIVES, DATESAVE, SCORE from PACMANGAMES")
        for row in selector2:
            lyst.append(row)
            index += 1
        if lyst !=[]:
            if index>=1:
                self.new1=lyst[0]
                s+= "save name: "+str(self.new1[0])+"  "+"level: "+str(self.new1[1])+"   "+"lives: "+str(self.new1[2])+"   "+"date of save: "+str(self.new1[3])+"   "+"score: "+str(self.new1[4])
            if index>=2:
                self.new2=lyst[1]
                s1+= "save name: "+str(self.new2[0])+"  "+"level: "+str(self.new2[1])+"   "+"lives: "+str(self.new2[2])+"   "+"date of save: "+str(self.new2[3])+"   "+"score: "+str(self.new2[4])
            if index==3:
                self.new3=lyst[2]
                s2+= "save name: "+str(self.new3[0])+"  "+"level: "+str(self.new3[1])+"   "+"lives: "+str(self.new3[2])+"   "+"date of save: "+str(self.new3[3])+"   "+"score: "+str(self.new3[4])
        pos = pygame.mouse.get_pos()
        pygame.draw.rect(self.screen, 'white', [50, 200, 800, 300],0, 10)
        pygame.draw.rect(self.screen, 'dark gray', [70, 220, 760, 260], 0, 10)
        back=pygame.draw.rect(self.screen, 'Blue', [100, 225, 150, 50], 0, 10)
        load1=pygame.draw.rect(self.screen, 'Blue', [150, 300, 600, 35], 0, 10)
        load2=pygame.draw.rect(self.screen, 'Blue', [150, 350, 600, 35], 0, 10)
        load3=pygame.draw.rect(self.screen, 'Blue', [150, 400, 600, 35], 0, 10)
        back_text = self.font.render(f'BACK<-', True, 'white')
        self.screen.blit(back_text, (130, 250))
        LoadMenu_text = self.Mainfont.render(f'Load Menu', True, 'white')
        self.screen.blit(LoadMenu_text, (350, 250))
        self.check=False
        delete_text = self.font.render("Delete",True,'white')
        firstsave_text = font.render(f'{s}', True, 'white')
        self.screen.blit(firstsave_text, (180, 310))
        secondsave_text = font.render(f'{s1}', True, 'white')
        self.screen.blit(secondsave_text, (180, 360))
        thirdsave_text = font.render(f'{s2}', True, 'white')
        self.screen.blit(thirdsave_text, (180, 410))
        delete1=pygame.draw.rect(self.screen, 'red', [650, 300, 100, 35], 0, 10)
        delete2=pygame.draw.rect(self.screen, 'red', [650, 350, 100, 35], 0, 10)
        delete3=pygame.draw.rect(self.screen, 'red', [650, 400, 100, 35], 0, 10)
        self.screen.blit(delete_text, (665, 308))
        self.screen.blit(delete_text, (665, 358))
        self.screen.blit(delete_text, (665, 408))

        
        
       
        
        if back.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked_back = True
                self.new=startGUI.StartGUI(self.screen, self.font)
        
        if self.clicked_back:
            if self.timer<180:
                self.timer+=1
            else:
                if not self.check:
                    if not self.new.start():
                        self.new.start()
                        
                else:
                    self.check=True
        
        if delete1.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and len(lyst) >= 1 and self.clicked == False:
                sql = 'DELETE FROM PACMANGAMES WHERE SAVENAME=?'
                self.connection.execute(sql, (self.new1[0],))
                self.connection.commit()
                self.clicked = True
        if delete2.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and len(lyst) >= 2 and self.clicked == False:
                sql = 'DELETE FROM PACMANGAMES WHERE SAVENAME=?'
                self.connection.execute(sql, (self.new2[0],))
                self.connection.commit()
                self.clicked = True
        if delete3.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and len(lyst) >= 3 and self.clicked == False:
                sql = 'DELETE FROM PACMANGAMES WHERE SAVENAME=?'
                self.connection.execute(sql, (self.new3[0],))
                self.connection.commit()
                self.clicked = True
        if load1.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and len(lyst) >= 1 and self.clicked == False:
                self.score = self.new1[4]
                self.lives = self.new1[2]
                self.level = self.new1[1]
                self.clicked = True
        if load2.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and len(lyst) >= 2 and self.clicked == False:
                self.score = self.new2[4]
                self.lives = self.new2[2]
                self.level = self.new2[1]
                self.clicked = True
        if load3.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and len(lyst) >= 3 and self.clicked == False:
                self.score = self.new3[4]
                self.lives = self.new3[2]
                self.level = self.new3[1]
                self.clicked = True
        if self.clicked == True and not pygame.mouse.get_pressed()[0] == 1:
            self.clicked = False
        
        
        

        
       
        
        
        
        if pygame.mouse.get_pressed()[0] == 0:
            pass
        
        
        return self.clicked_back
    def set_status(self, status:bool)->None:
        ''' This function will set the status variable to the value that is passed by the status perameter'''
        self.status = status
    def set_score(self,score:int)->None:
        ''' This function will set the score variable to the value that is passed by the score perameter'''
        self.score = score
    def set_lives(self,lives:int)->None:
        ''' This function will set the lives variable to the value that is passed by the lives perameter'''
        self.lives = lives
    def set_level(self,level:int)->None:
        ''' This function will set the level variable to the value that is passed by the level perameter'''
        self.level = level
    def get_score(self)->int:
        '''Thsi function will return the value of score'''
        return self.score
    def get_lives(self)->int:
        '''Thsi function will return the value of lives'''
        return self.lives
    def get_level(self)->int:
        '''Thsi function will return the value of level'''
        return self.level
    
    
    
    

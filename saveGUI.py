#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 19:19:59 2023

@author: corydragun
"""
import database
import pygame
import sqlite3
class SaveGui(object):
    def __init__(self,screen:list,font:str,level:int,lives:int,date:str,score:int)->None:
        self.lives=lives
        self.level=level
        self.date=date
        self.score=score
        self.clicked=False
        self.wordentered=False
        self.usertext=''
        self.connection=sqlite3.connect("pacman.db")
        self.screen=screen
        self.font=font
    def display_save(self)->None:
        ''' This function will display the users save name on screen and when 
        the save button is pressed it will send the save name along with level, lives, date, and score'''
        self.data=database.Database(self.usertext,self.level,self.lives,self.date,self.score)
        self.connection.execute(''' CREATE TABLE IF NOT EXISTS PACMANGAMES
                          (SAVENAME TEXT PRIMARY KEY NOT NULL,
                        LEVEL INT NOT NULL,
                        LIVES INT NOT NULL,
                        DATESAVE TEXT NOT NULL,
                        SCORE INT NOT NULL);''')
        pos = pygame.mouse.get_pos()
        pygame.draw.rect(self.screen, 'white', [50, 200, 800, 300],0, 10)
        pygame.draw.rect(self.screen, 'dark gray', [70, 220, 760, 260], 0, 10)
        top=pygame.draw.rect(self.screen, 'blue', [250, 350, 500, 50], 0, 10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_BACKSPACE:
                    self.usertext=self.usertext[:-1]
                else:
                    self.usertext+=event.unicode
                    self.usertext=self.usertext
        user_text = self.font.render(f'save name: {self.usertext}', True, 'white')
        error_text = self.font.render("Please enter a save name, cannot be left empty",True, 'red')
        self.screen.blit(error_text, (250, 330))
        self.screen.blit(user_text, (250, 350))
        if top.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.usertext == "":
                    pass
                elif pygame.mouse.get_pressed()[0] == 1 and self.usertext != "":
                    self.clicked = True
                    self.data.database_setter()
        return self.clicked
                
    def set_level(self,level:int)->None:
        ''' This function will set the level variable to the value that is passed by the level perameter'''
        self.level = level
    def set_lives(self,lives:int)->None:
        ''' This function will set the lives variable to the value that is passed by the lives perameter'''
        self.lives = lives
    def set_score(self,score:int)->None:
        ''' This function will set the score variable to the value that is passed by the score perameter'''
        self.score = score

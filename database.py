#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 17:55:05 2023

@author: corydragun
"""

import sqlite3
import LoadGUI
class Database(object):
    def __init__(self,savename:str,level:int,lives:int,date:str,score:int)->None:
        self.name=savename
        self.lives=lives
        self.level=level
        self.date=date
        self.score=score
        self.connection=sqlite3.connect("pacman.db")
        self.new1=[()]
    def database_setter(self)->None:
        '''This function will create the save database and save the records of the saved games'''
        count =0

        
        
        selector=self.connection.execute("SELECT SAVENAME,LEVEL, LIVES, DATESAVE, SCORE from PACMANGAMES")
        for row in selector:
            count += 1
        if count<3:
            self.connection.execute("INSERT OR IGNORE INTO PACMANGAMES(SAVENAME,LEVEL,LIVES,DATESAVE,SCORE)\
                                        VALUES(?,?,?,?,?)",(self.name,self.level,self.lives,self.date,self.score));
            self.connection.commit()
        else:
            print("no no")
        
        
      
        self.connection.close()
        

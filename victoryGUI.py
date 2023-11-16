import pygame
from pauseGUI import pause
import saveGUI

class VictoryGUI(object):
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
        self.new=saveGUI.saveGUI(self.screen, self.font,self.level,self.lives,self.date,self.score)
    def victory(self):
        self.new.setlevel(self.level)
        self.new.setlives(self.lives)
        self.new.setscore(self.score)
        pos = pygame.mouse.get_pos()
        pygame.draw.rect(self.screen, 'white', [50, 200, 800, 300],0, 10)
        pygame.draw.rect(self.screen, 'dark gray', [70, 220, 760, 260], 0, 10)
        top=pygame.draw.rect(self.screen, 'blue', [350, 350, 150, 50], 0, 10)
        start_text = self.font.render(f'Next Level->', True, 'white')
        self.screen.blit(start_text, (365, 370))
        if top.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked_next = True
        if self.clicked_next:
                if self.timer<180:
                    self.timer+=1
                else:
                    if not self.check:
                        if not self.new.displaySave():
                            self.new.displaySave()
                    else:
                        self.check=True
                
    
        if pygame.mouse.get_pressed()[0] == 0:
            pass
        return self.clicked
    def setlevel(self,level):
        self.level = level
    def setlives(self,lives):
        self.lives = lives
    def setscore(self,score):
        self.score = score

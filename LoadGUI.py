import pygame
import startGUI
from pauseGUI import pause


class loadGUI(object):
    def __init__(self, screen,font):
        self.screen=screen
        self.font=font
        self.check=False
        self.timer=0
        self.clicked_back=False
        self.clicked_load=False
        
        
        
        
        
    def load(self):
        pos = pygame.mouse.get_pos()
        pygame.draw.rect(self.screen, 'white', [50, 200, 800, 300],0, 10)
        pygame.draw.rect(self.screen, 'dark gray', [70, 220, 760, 260], 0, 10)
        back=pygame.draw.rect(self.screen, 'Blue', [200, 300, 150, 50], 0, 10)
        start_text = self.font.render(f'BACK<-', True, 'white')
        self.screen.blit(start_text, (230, 320))
        load=pygame.draw.rect(self.screen, 'Blue', [400, 400, 150, 50], 0, 10)
        load_text = self.font.render(f'Load->', True, 'white')
        self.screen.blit(load_text, (430, 420))
        self.check=False
        
        
        
        
       
        
        if back.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked_back = True
                self.new=startGUI.StartGUI(self.screen, self.font,False)
        if load.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked_load=True
        if self.clicked_back:
            if self.timer<180:
                self.timer+=1
            else:
                if not self.check:
                    if not self.new.start():
                        self.new.start()
                        
                else:
                    self.check=True
                    self.new.setStatus(False)
                    
        print(self.clicked_back)
        if self.clicked_load:
            pass
        
        
        
        if pygame.mouse.get_pressed()[0] == 0:
            pass
        
        
        return self.clicked_back
    def setStatus(self, status):
        self.status = status

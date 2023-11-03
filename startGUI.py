import pygame
import LoadGUI



class StartGUI(object):
    def __init__(self, screen,font,status):
        self.clicked_start=False
        self.clicked_load=False
        self.screen=screen
        self.font=font
        self.timer=0
        self.status=False
        self.new=LoadGUI.loadGUI(self.screen,self.font)
        self.Mainfont=pygame.font.Font('freesansbold.ttf', 40)
        
        
        
    def start(self):
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
        if pygame.mouse.get_pressed()[0] == 0:
            pass
        if load.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked_load=True
        if self.clicked_load:
            if self.timer<180:
                self.timer+=1
            else:
                if not self.check:
                    if not self.new.load():
                        self.new.load()
                else:
                    self.check=True
            
            
                
       
        
            
        
            
        
        if pygame.mouse.get_pressed()[0] == 0:
            pass
        
        return self.status
    def setStatus(self, status):
        self.status = status
    def setLoad(self, clickedLoad):
        self.clicked_load = clickedLoad
                
        
        

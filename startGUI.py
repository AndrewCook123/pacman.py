import pygame
import LoadGUI




class StartGUI(object):
    def __init__(self, screen:list, font:str, status:bool):
        self.clicked_start = False
        self.clicked_load = False
        self.screen = screen
        self.font = font
        self.timer = 0
        self.status = False
        self.new = LoadGUI.loadGUI(self.screen,self.font)
        self.Mainfont = pygame.font.Font('freesansbold.ttf', 40)
        self.score = 0
        self.lives = 0
        self.level = 0
        

    def start(self) -> bool:
        ''' This function draw the start menu on screen with start and load buttons. '''
        self.score = self.new.getScore()
        self.lives = self.new.getLives()
        self.level = self.new.getLevel()
        pos = pygame.mouse.get_pos()
        pygame.draw.rect(self.screen, 'white', [50, 200, 800, 300],0, 10)
        pygame.draw.rect(self.screen, 'dark gray', [70, 220, 760, 260], 0, 10)
        start = pygame.draw.rect(self.screen, 'Blue', [275, 400, 150, 50], 0, 10)
        start_text = self.font.render(f'START->', True, 'white')
        self.screen.blit(start_text, (305, 420))
        load = pygame.draw.rect(self.screen, 'Blue', [475, 400, 150, 50], 0, 10)
        start_text = self.font.render(f'Load->', True, 'white')
        self.screen.blit(start_text, (515, 420))
        MainMenu_text = self.Mainfont.render(f'Pac-Man', True, 'white')
        self.screen.blit(MainMenu_text, (350, 300))
        self.check = False
        
        if start.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked_start = True
                self.status = True
        if self.clicked_load:
            self.status = False
        if pygame.mouse.get_pressed()[0] == 0:
            pass
        if load.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked_load = True
        if self.clicked_load:
            if self.timer<180:
                self.timer += 1
            else:
                clicked = self.new.load()
                if not self.check:
                    if not clicked:
                        self.clicked_start = False
                        self.new.load()
                else:
                    self.clicked_start = self.clicked_start
                    self.check = True
        
        if pygame.mouse.get_pressed()[0] == 0:
            pass
        
        return self.clicked_start
    
    def setLoad(self, clickedLoad:bool) -> None:
        ''' This function sets the clicked_load variable. '''
        self.clicked_load = clickedLoad
        
    def getScore(self) -> int:
        ''' This function returns the value of the score variable. '''
        self.score = self.new.getScore()
        return self.score
    
    def getLives(self) -> int:
        ''' This function returns the value of the lives variable. '''
        self.lives = self.new.getLives()
        return self.lives
    
    def getLevel(self) -> int:
        ''' This function returns the value of the level variable. '''
        self.level = self.new.getLevel()
        return self.level
    
                
        
        

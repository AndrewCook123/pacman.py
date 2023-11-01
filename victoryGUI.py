import pygame
from pauseGUI import pause


class VictoryGUI(object):
    def __init__(self, screen,font):
        self.clicked=False
        self.screen=screen
        self.font=font
    def victory(self):
        pos = pygame.mouse.get_pos()
        pygame.draw.rect(self.screen, 'white', [50, 200, 800, 300],0, 10)
        pygame.draw.rect(self.screen, 'dark gray', [70, 220, 760, 260], 0, 10)
        top=pygame.draw.rect(self.screen, 'red', [300, 250, 200, 200], 0, 10)
        if top.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked = True
                print("Clicked")
        if self.clicked:
            new=pause(self.screen)
            new.PauseMenu()
                
    
        if pygame.mouse.get_pressed()[0] == 0:
            pass
        return self.clicked

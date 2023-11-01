import pygame
class pause(object):
    def __init__(self,screen):
        self.screen=screen
    def shower(self):
        pause_text = self.font.render('II', True, 'white')
        self.screen.blit(pause_text, (50, 50))
    def PauseMenu(self):
        pygame.draw.rect(self.screen, 'red', [50, 200, 800, 300],0, 10)
        pygame.draw.rect(self.screen, 'blue', [70, 220, 760, 260], 0, 10)

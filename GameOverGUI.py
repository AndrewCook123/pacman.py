import pygame
class gameOver(object):
    def __init__(self,screen,font):
        self.screen=screen
        self.font=font
    def Gover(self):
        pygame.draw.rect(self.screen, 'white', [50, 200, 800, 300],0, 10)
        pygame.draw.rect(self.screen, 'dark gray', [70, 220, 760, 260], 0, 10)
        gameover_text = self.font.render('Game over! Space bar to restart!', True, 'red')
        self.screen.blit(gameover_text, (100, 300))

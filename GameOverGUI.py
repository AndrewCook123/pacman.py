import pygame
class gameOver(object):
    def __init__(self,screen,font,status):
        self.screen=screen
        self.font=font
        self.clicked_over=False
        self.status=status
    def Gover(self):
        pos = pygame.mouse.get_pos()
        pygame.draw.rect(self.screen, 'white', [50, 200, 800, 300],0, 10)
        pygame.draw.rect(self.screen, 'dark gray', [70, 220, 760, 260], 0, 10)
        gameoverbox=pygame.draw.rect(self.screen, 'Blue', [200, 400, 150, 50], 0, 10)
        gameover_text = self.font.render('Game over! Space bar to restart!', True, 'red')
        self.screen.blit(gameover_text, (100, 300))
        if gameoverbox.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.status = True
        return self.status
    def setStatus(self, status):
        self.status = status

import pygame

class Pause(object):
    def __init__(self,screen,font,status):
        self.status=False
        self.font=font
        self.screen=screen
        self.clicked_pause=False
        self.clicked_resume=False
        self.clicked_quit=False
        self.clicked = False
        self.Mainfont=pygame.font.Font('freesansbold.ttf', 40)
    def show(self):
        self.clicked_resume=False
        pos = pygame.mouse.get_pos()
        p=pygame.draw.rect(self.screen, 'black', [50, 50, 20, 20], 0, 10)
        pause_text = self.font.render('II', True, 'white')
        self.screen.blit(pause_text, (50, 50))
        if p.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked_pause=True
        return self.clicked_pause
    def PauseMenu(self):
        pos = pygame.mouse.get_pos()
        pygame.draw.rect(self.screen, 'white', [50, 200, 800, 300],0, 10)
        pygame.draw.rect(self.screen, 'dark grey', [70, 220, 760, 260], 0, 10)
        resume = pygame.draw.rect(self.screen, 'Blue', [270, 335, 150, 50], 0, 10)
        resume_text = self.font.render(f'Resume', True, 'white')
        self.screen.blit(resume_text, (320, 355))
        quits = pygame.draw.rect(self.screen, 'Blue', [470, 335, 150, 50], 0, 10)
        quit_text = self.font.render(f'Quit', True, 'white')
        self.screen.blit(quit_text, (490, 355))
        pauseMenu_text = self.Mainfont.render(f'Pause Menu', True, 'white')
        if resume.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked_resume=True
                self.clicked_pause=False
        return self.clicked_resume
    def quit_button(self):
        pos = pygame.mouse.get_pos()
        quits = pygame.draw.rect(self.screen, 'Blue', [470, 335, 150, 50], 0, 10)
        quit_text = self.font.render(f'Quit', True, 'white')
        self.screen.blit(quit_text, (380, 395))
        pauseMenu_text = self.Mainfont.render(f'Pause Menu', True, 'white')
        if quits.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked_quit=True
                self.clicked_pause=False
        return self.clicked_quit
    def start_over(self):
        self.clicked_quit=False
    def setStatus(self, status):
        self.status = status

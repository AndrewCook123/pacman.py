import database
import pygame
class saveGUI(object):
    def __init__(self,screen,font,level,lives,date,score):
        self.lives=lives
        self.level=level
        self.date=date
        self.score=score
        self.clicked=False
        self.usertext=''
        self.screen=screen
        self.font=font
    def displaySave(self):
        self.data=database.Database(self.usertext,self.level,self.lives,self.date,self.score)
        pos = pygame.mouse.get_pos()
        pygame.draw.rect(self.screen, 'white', [50, 200, 800, 300],0, 10)
        pygame.draw.rect(self.screen, 'dark gray', [70, 220, 760, 260], 0, 10)
        top=pygame.draw.rect(self.screen, 'blue', [350, 350, 150, 50], 0, 10)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_BACKSPACE:
                    self.usertext=self.usertext[:-1]
                else:
                    self.usertext+=event.unicode
                    self.usertext=self.usertext
        user_text = self.font.render(f'save name: {self.usertext}', True, 'white')
        error_text = self.font.render("Please enter a save name, cannot be left empty",True, 'red')
        self.screen.blit(error_text, (250, 330))
        self.screen.blit(user_text, (350, 350))
        if top.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.usertext == "":
                    pass
                elif pygame.mouse.get_pressed()[0] == 1 and self.usertext != "":
                    self.clicked = True
                    self.data.databasesetter()
                    print("pressed")
                
        return self.clicked
    def setlevel(self,level):
        self.level = level
    def setlives(self,lives):
        self.lives = lives
    def setscore(self,score):
        self.score = score

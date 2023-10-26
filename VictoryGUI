import pygame

class VictoryGUI(object):
    def victory(screen,font):
        pos = pygame.mouse.get_pos()
        clicked = False
        pygame.draw.rect(screen, 'white', [50, 200, 800, 300],0, 10)
        pygame.draw.rect(screen, 'dark gray', [70, 220, 760, 260], 0, 10)
        top=pygame.draw.rect(screen, 'red', [300, 250, 200, 200], 0, 10)
        action = False
        if top.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and clicked == False:
                clicked = True
                action = True
                print("Clicked")
                
    
        if pygame.mouse.get_pressed()[0] == 0:
            clicked = False
        return action

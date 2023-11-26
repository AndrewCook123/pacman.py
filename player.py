# -*- coding: utf-8 -*-
import pygame

class Player(object):
    def __init__(self):
        self.WIDTH = 900
        self.HEIGHT = 950
    
    def move_player(self, play_x:str, play_y:str, turns_allowed:list, direction:int, player_speed:int) -> int | int:
        ''' This function is responsible for moving the player. '''
        # right = 0, left = 1, up = 2, down = 3
        if direction == 0 and turns_allowed[0]:
            play_x += player_speed
        elif direction == 1 and turns_allowed[1]:
            play_x -= player_speed
        if direction == 2 and turns_allowed[2]:
            play_y -= player_speed
        elif direction == 3 and turns_allowed[3]:
            play_y += player_speed
        return play_x, play_y
    
    def draw_player(self, direction:int, player_x:int, player_y:int, counter:int, screen:list, player_images:str) -> None:
        ''' This function draw the player on screen. '''
        # 0-RIGHT, 1-LEFT, 2-UP, 3-DOWN
        if direction == 0:
            screen.blit(player_images[counter // 5], (player_x, player_y))
        elif direction == 1:
            screen.blit(pygame.transform.flip(player_images[counter // 5], True, False), (player_x, player_y))
        elif direction == 2:
            screen.blit(pygame.transform.rotate(player_images[counter // 5], 90), (player_x, player_y))
        elif direction == 3:
            screen.blit(pygame.transform.rotate(player_images[counter // 5], 270), (player_x, player_y))
                
    def check_position(self, centerx:int, centery:int, direction:int, level:list) -> list:
        ''' This function checks the players location on the board. '''
        turns = [False, False, False, False]
        num1 = (self.HEIGHT - 50) // 32
        num2 = (self.WIDTH // 30)
        num3 = 15
        # check collisions based on center x and center y of player +/- fudge number
        if centerx // 30 < 29:
            if direction == 0:
                if level[centery // num1][(centerx - num3) // num2] < 3:
                    turns[1] = True
            if direction == 1:
                if level[centery // num1][(centerx + num3) // num2] < 3:
                    turns[0] = True
            if direction == 2:
                if level[(centery + num3) // num1][centerx // num2] < 3:
                    turns[3] = True
            if direction == 3:
                if level[(centery - num3) // num1][centerx // num2] < 3:
                    turns[2] = True

            if direction == 2 or direction == 3:
                if 12 <= centerx % num2 <= 18:
                    if level[(centery + num3) // num1][centerx // num2] < 3:
                        turns[3] = True
                    if level[(centery - num3) // num1][centerx // num2] < 3:
                        turns[2] = True
                if 12 <= centery % num1 <= 18:
                    if level[centery // num1][(centerx - num2) // num2] < 3:
                        turns[1] = True
                    if level[centery // num1][(centerx + num2) // num2] < 3:
                        turns[0] = True
            if direction == 0 or direction == 1:
                if 12 <= centerx % num2 <= 18:
                    if level[(centery + num1) // num1][centerx // num2] < 3:
                            turns[3] = True
                    if level[(centery - num1) // num1][centerx // num2] < 3:
                        turns[2] = True
                if 12 <= centery % num1 <= 18:
                    if level[centery // num1][(centerx - num3) // num2] < 3:
                        turns[1] = True
                    if level[centery // num1][(centerx + num3) // num2] < 3:
                        turns[0] = True
            if direction == 0 or direction == 1:
                if 12 <= centerx % num2 <= 18:
                    if level[(centery + num1) // num1][centerx // num2] == 10:
                            turns[3] = True
                    if level[(centery - num1) // num1][centerx // num2] == 10:
                        turns[2] = True
                if 12 <= centery % num1 <= 18:
                    if level[centery // num1][(centerx - num3) // num2] == 10:
                        turns[1] = True
                    if level[centery // num1][(centerx + num3) // num2] == 10:
                        turns[0] = True
        else:
            turns[0] = True
            turns[1] = True

        return turns

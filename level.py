from testing_board import boards
from Ghost import Ghost
from player import Player
from victoryGUI import VictoryGUI
from GameOverGUI import gameOver
from startGUI import StartGUI
from pauseGUI import pause
import pygame
import copy
import math
from datetime import date
class Level(object):
    def __init__(self):
        self.WIDTH = 900
        self.HEIGHT = 950
        self.screen = pygame.display.set_mode([self.WIDTH, self.HEIGHT])
        self.timer = pygame.time.Clock()
        self.fps = 60
        self.font = pygame.font.Font('freesansbold.ttf', 20)
        self.level = copy.deepcopy(boards)
        self.level_num=1
        self.color = 'blue'
        self.PI = math.pi
        self.player_images = []
        self.today = date.today()
        self.date = self.today.strftime("%m/%d/%y")
        for i in range(1, 5):
            self.player_images.append(pygame.transform.scale(pygame.image.load(f'assets/player_images/{i}.png'), (45, 45)))
        self.blinky_img = pygame.transform.scale(pygame.image.load(f'assets/ghost_images/red.png'), (45, 45))
        self.pinky_img = pygame.transform.scale(pygame.image.load(f'assets/ghost_images/pink.png'), (45, 45))
        self.inky_img = pygame.transform.scale(pygame.image.load(f'assets/ghost_images/blue.png'), (45, 45))
        self.clyde_img = pygame.transform.scale(pygame.image.load(f'assets/ghost_images/orange.png'), (45, 45))
        self.spooked_img = pygame.transform.scale(pygame.image.load(f'assets/ghost_images/powerup.png'), (45, 45))
        self.dead_img = pygame.transform.scale(pygame.image.load(f'assets/ghost_images/dead.png'), (45, 45))
        self.player_x = 450
        self.player_y = 663
        self.direction = 0
        self.blinky_x = 56
        self.blinky_y = 58
        self.blinky_direction = 0
        self.inky_x = 440
        self.inky_y = 388
        self.inky_direction = 2
        self.pinky_x = 440
        self.pinky_y = 438
        self.pinky_direction = 2
        self.clyde_x = 440
        self.clyde_y = 438
        self.clyde_direction = 2
        self.counter = 0
        self.flicker = False
        # R, L, U, D
        self.turns_allowed = [False, False, False, False]
        self.direction_command = 0
        self.player_speed = 2
        self.score = 0
        self.powerup = False
        self.power_counter = 0
        self.eaten_ghost = [False, False, False, False]
        self.targets = [(self.player_x, self.player_y), (self.player_x, self.player_y), (self.player_x, self.player_y), (self.player_x, self.player_y)]
        self.blinky_dead = False
        self.inky_dead = False
        self.clyde_dead = False
        self.pinky_dead = False
        self.blinky_box = False
        self.inky_box = False
        self.clyde_box = False
        self.pinky_box = False
        self.moving = False
        self.ghost_speeds = [2, 2, 2, 2]
        self.startup_counter = 0
        self.lives = 3
        self.game_over = False
        self.game_won = False
        self.quitter=False
        self.time=7200
        self.over=gameOver(self.screen, self.font,False)
        self.won=VictoryGUI(self.screen, self.font,self.level_num,self.lives,self.date,self.score)
        self.happy=StartGUI(self.screen, self.font,False)
        self.pauseMenu=pause(self.screen,self.font, False)
        self.check=False
       
    def draw_misc(self, game_won, game_over, lives):
        score_text = self.font.render(f'Score: {self.score}', True, 'white')
        self.screen.blit(score_text, (700, 75))
        lives_text = self.font.render(f'Lives: {self.lives}', True, 'white')
        self.screen.blit(lives_text, (700, 50))
        if self.powerup:
            pygame.draw.circle(self.screen, 'blue', (140, 930), 15)
        for i in range(lives):
            self.screen.blit(pygame.transform.scale(self.player_images[0], (30, 30)), (650 + i * 40, 915))
        if game_over:
            self.over.Gover()
        if game_won:
            self.won.setlevel(self.level_num)
            self.won.setlives(self.lives)
            self.won.setscore(self.score)

            self.won.victory()
       
       
    def check_collisions(self, scor, power, power_count, eaten_ghosts, center_x, center_y, player_x, level):
        num1 = (self.HEIGHT - 50) // 32
        num2 = self.WIDTH // 30
        if 0 < player_x < 870:
            if level[center_y // num1][center_x // num2] == 1:
                level[center_y // num1][center_x // num2] = 0
                scor += 10
            if level[center_y // num1][center_x // num2] == 2:
                level[center_y // num1][center_x // num2] = 0
                scor += 50
                power = True
                power_count = 0
                eaten_ghosts = [False, False, False, False]
        return scor, power, power_count, eaten_ghosts
       
    def draw_board(self, level):
        num1 = ((self.HEIGHT - 50) // 32)
        num2 = (self.WIDTH // 30)
        for i in range(len(level)):
            for j in range(len(level[i])):
                if level[i][j] == 1:
                    pygame.draw.circle(self.screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 4)
                if level[i][j] == 2 and not self.flicker:
                    pygame.draw.circle(self.screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 10)
                if level[i][j] == 3:
                    pygame.draw.line(self.screen, self.color, (j * num2 + (0.5 * num2), i * num1),
                                    (j * num2 + (0.5 * num2), i * num1 + num1), 3)
                if level[i][j] == 4:
                    pygame.draw.line(self.screen, self.color, (j * num2, i * num1 + (0.5 * num1)),
                                        (j * num2 + num2, i * num1 + (0.5 * num1)), 3)
                if level[i][j] == 5:
                    pygame.draw.arc(self.screen, self.color, [(j * num2 - (num2 * 0.4)) - 2, (i * num1 + (0.5 * num1)), num2, num1],
                                        0, self.PI / 2, 3)
                if level[i][j] == 6:
                    pygame.draw.arc(self.screen, self.color,
                                        [(j * num2 + (num2 * 0.5)), (i * num1 + (0.5 * num1)), num2, num1], self.PI / 2, self.PI, 3)
                if level[i][j] == 7:
                    pygame.draw.arc(self.screen, self.color, [(j * num2 + (num2 * 0.5)), (i * num1 - (0.4 * num1)), num2, num1], self.PI,
                                        3 * self.PI / 2, 3)
                if level[i][j] == 8:
                    pygame.draw.arc(self.screen, self.color,
                                        [(j * num2 - (num2 * 0.4)) - 2, (i * num1 - (0.4 * num1)), num2, num1], 3 * self.PI / 2,
                                        2 * self.PI, 3)
                if level[i][j] == 9:
                    pygame.draw.line(self.screen, 'white', (j * num2, i * num1 + (0.5 * num1)),
                                         (j * num2 + num2, i * num1 + (0.5 * num1)), 3)
                       
   
       
   
       
    def get_targets(self, blink_x, blink_y, ink_x, ink_y, pink_x, pink_y, clyd_x, clyd_y, blinky, pinky, inky, clyde, player_x, player_y, powerup):
        if player_x < 450:
            runaway_x = 900
        else:
            runaway_x = 0
        if player_y < 450:
            runaway_y = 900
        else:
            runaway_y = 0
        return_target = (380, 400)
        if powerup:
            if not blinky.dead and not self.eaten_ghost[0]:
                blink_target = (runaway_x, runaway_y)
            elif not blinky.dead and self.eaten_ghost[0]:
                if 340 < blink_x < 560 and 340 < blink_y < 500:
                    blink_target = (400, 100)
                else:
                    blink_target = (player_x, player_y)
            else:
                blink_target = return_target
            if not inky.dead and not self.eaten_ghost[1]:
                ink_target = (runaway_x, player_y)
            elif not inky.dead and self.eaten_ghost[1]:
                if 340 < ink_x < 560 and 340 < ink_y < 500:
                    ink_target = (400, 100)
                else:
                    ink_target = (player_x, player_y)
            else:
                ink_target = return_target
            if not pinky.dead:
                pink_target = (player_x, runaway_y)
            elif not pinky.dead and self.eaten_ghost[2]:
                if 340 < pink_x < 560 and 340 < pink_y < 500:
                    pink_target = (400, 100)
                else:
                    pink_target = (player_x, player_y)
            else:
                pink_target = return_target
            if not clyde.dead and not self.eaten_ghost[3]:
                clyd_target = (450, 450)
            elif not clyde.dead and self.eaten_ghost[3]:
                if 340 < clyd_x < 560 and 340 < clyd_y < 500:
                    clyd_target = (400, 100)
                else:
                    clyd_target = (player_x, player_y)
            else:
                clyd_target = return_target
        else:
            if not blinky.dead:
                if 340 < blink_x < 560 and 340 < blink_y < 500:
                    blink_target = (400, 100)
                else:
                    blink_target = (player_x, player_y)
            else:
                blink_target = return_target
            if not inky.dead:
                if 340 < ink_x < 560 and 340 < ink_y < 500:
                    ink_target = (400, 100)
                else:
                    ink_target = (player_x, player_y)
            else:
                ink_target = return_target
            if not pinky.dead:
                if 340 < pink_x < 560 and 340 < pink_y < 500:
                    pink_target = (400, 100)
                else:
                    pink_target = (player_x, player_y)
            else:
                pink_target = return_target
            if not clyde.dead:
                if 340 < clyd_x < 560 and 340 < clyd_y < 500:
                    clyd_target = (400, 100)
                else:
                    clyd_target = (player_x, player_y)
            else:
                clyd_target = return_target
        return [blink_target, ink_target, pink_target, clyd_target]
   
    def reset_positions(self, player_circle, blinky, inky, pinky, clyde):
        if not self.powerup:
            if (player_circle.colliderect(blinky.rect) and not blinky.dead) or \
                    (player_circle.colliderect(inky.rect) and not inky.dead) or \
                    (player_circle.colliderect(pinky.rect) and not pinky.dead) or \
                    (player_circle.colliderect(clyde.rect) and not clyde.dead):
                if self.lives > 0:
                    self.lives -= 1
                    self.startup_counter = 0
                    self.powerup = False
                    self.power_counter = 0
                    self.player_x = 450
                    self.player_y = 663
                    self.direction = 0
                    self.direction_command = 0
                    self.blinky_x = 56
                    self.blinky_y = 58
                    self.blinky_direction = 0
                    self.inky_x = 440
                    self.inky_y = 388
                    self.inky_direction = 2
                    self.pinky_x = 440
                    self.pinky_y = 438
                    self.pinky_direction = 2
                    self.clyde_x = 440
                    self.clyde_y = 438
                    self.clyde_direction = 2
                    self.eaten_ghost = [False, False, False, False]
                    self.blinky_dead = False
                    self.inky_dead = False
                    self.clyde_dead = False
                    self.pinky_dead = False
                else:
                    self.game_over = True
                    self.moving = False
                    self.startup_counter = 0
        if self.powerup and player_circle.colliderect(blinky.rect) and self.eaten_ghost[0] and not blinky.dead:
            if self.lives > 0:
                self.powerup = False
                self.power_counter = 0
                self.lives -= 1
                self.startup_counter = 0
                self.player_x = 450
                self.player_y = 663
                self.direction = 0
                self.direction_command = 0
                self.blinky_x = 56
                self.blinky_y = 58
                self.blinky_direction = 0
                self.inky_x = 440
                self.inky_y = 388
                self.inky_direction = 2
                self.pinky_x = 440
                self.pinky_y = 438
                self.pinky_direction = 2
                self.clyde_x = 440
                self.clyde_y = 438
                self.clyde_direction = 2
                self.eaten_ghost = [False, False, False, False]
                self.blinky_dead = False
                self.inky_dead = False
                self.clyde_dead = False
                self.pinky_dead = False
            else:
                self.game_over = True
                self.moving = False
                self.startup_counter = 0
        if self.powerup and player_circle.colliderect(inky.rect) and self.eaten_ghost[1] and not inky.dead:
            if self.lives > 0:
                self.powerup = False
                self.power_counter = 0
                self.lives -= 1
                self.startup_counter = 0
                self.player_x = 450
                self.player_y = 663
                self.direction = 0
                self.direction_command = 0
                self.blinky_x = 56
                self.blinky_y = 58
                self.blinky_direction = 0
                self.inky_x = 440
                self.inky_y = 388
                self.inky_direction = 2
                self.pinky_x = 440
                self.pinky_y = 438
                self.pinky_direction = 2
                self.clyde_x = 440
                self.clyde_y = 438
                self.clyde_direction = 2
                self.eaten_ghost = [False, False, False, False]
                self.blinky_dead = False
                self.inky_dead = False
                self.clyde_dead = False
                self.pinky_dead = False
            else:
                self.game_over = True
                self.moving = False
                self.startup_counter = 0
        if self.powerup and player_circle.colliderect(pinky.rect) and self.eaten_ghost[2] and not pinky.dead:
            if self.lives > 0:
                self.powerup = False
                self.power_counter = 0
                self.lives -= 1
                self.startup_counter = 0
                self.player_x = 450
                self.player_y = 663
                self.direction = 0
                self.direction_command = 0
                self.blinky_x = 56
                self.blinky_y = 58
                self.blinky_direction = 0
                self.inky_x = 440
                self.inky_y = 388
                self.inky_direction = 2
                self.pinky_x = 440
                self.pinky_y = 438
                self.pinky_direction = 2
                self.clyde_x = 440
                self.clyde_y = 438
                self.clyde_direction = 2
                self.eaten_ghost = [False, False, False, False]
                self.blinky_dead = False
                self.inky_dead = False
                self.clyde_dead = False
                self.pinky_dead = False
            else:
                self.game_over = True
                self.moving = False
                self.startup_counter = 0
        if self.powerup and player_circle.colliderect(clyde.rect) and self.eaten_ghost[3] and not clyde.dead:
            if self.lives > 0:
                self.powerup = False
                self.power_counter = 0
                self.lives -= 1
                self.startup_counter = 0
                self.player_x = 450
                self.player_y = 663
                self.direction = 0
                self.direction_command = 0
                self.blinky_x = 56
                self.blinky_y = 58
                self.blinky_direction = 0
                self.inky_x = 440
                self.inky_y = 388
                self.inky_direction = 2
                self.pinky_x = 440
                self.pinky_y = 438
                self.pinky_direction = 2
                self.clyde_x = 440
                self.clyde_y = 438
                self.clyde_direction = 2
                self.eaten_ghost = [False, False, False, False]
                self.blinky_dead = False
                self.inky_dead = False
                self.clyde_dead = False
                self.pinky_dead = False
            else:
                self.game_over = True
                self.moving = False
        if self.game_over and self.over.Gover():
            self.powerup = False
            self.power_counter = 0
            self.lives -= 1
            self.startup_counter = 0
            self.player_x = 450
            self.player_y = 663
            self.direction = 0
            self.direction_command = 0
            self.blinky_x = 56
            self.blinky_y = 58
            self.blinky_direction = 0
            self.inky_x = 440
            self.inky_y = 388
            self.inky_direction = 2
            self.pinky_x = 440
            self.pinky_y = 438
            self.pinky_direction = 2
            self.clyde_x = 440
            self.clyde_y = 438
            self.clyde_direction = 2
            self.eaten_ghost = [False, False, False, False]
            self.blinky_dead = False
            self.inky_dead = False
            self.clyde_dead = False
            self.pinky_dead = False
            self.score = 0
            self.lives = 3
            self.time=3600
            self.level = copy.deepcopy(boards)
            self.game_over = False
            self.game_won = False
            self.startup_counter = 0
        if self.quitter:
              self.powerup = False
              self.power_counter = 0
              self.lives -= 1
              self.startup_counter = 0
              self.player_x = 450
              self.player_y = 663
              self.direction = 0
              self.direction_command = 0
              self.blinky_x = 56
              self.blinky_y = 58
              self.blinky_direction = 0
              self.inky_x = 440
              self.inky_y = 388
              self.inky_direction = 2
              self.pinky_x = 440
              self.pinky_y = 438
              self.pinky_direction = 2
              self.clyde_x = 440
              self.clyde_y = 438
              self.clyde_direction = 2
              self.eaten_ghost = [False, False, False, False]
              self.blinky_dead = False
              self.inky_dead = False
              self.clyde_dead = False
              self.pinky_dead = False
              self.score = 0
              self.lives = 3
              self.time=7200
              self.level = copy.deepcopy(boards)
              self.game_over = False
              self.game_won = False
              self.check=False
              self.startup_counter = 0
              self.over.setStatus(False)
              self.pauseMenu.start_over()
        if self.powerup and player_circle.colliderect(blinky.rect) and not blinky.dead and not self.eaten_ghost[0]:
            self.blinky_dead = True
            self.eaten_ghost[0] = True
            self.score += (2 ** self.eaten_ghost.count(True)) * 100
        if self.powerup and player_circle.colliderect(inky.rect) and not inky.dead and not self.eaten_ghost[1]:
            self.inky_dead = True
            self.eaten_ghost[1] = True
            self.score += (2 ** self.eaten_ghost.count(True)) * 100
        if self.powerup and player_circle.colliderect(pinky.rect) and not pinky.dead and not self.eaten_ghost[2]:
            self.pinky_dead = True
            self.eaten_ghost[2] = True
            self.score += (2 ** self.eaten_ghost.count(True)) * 100
        if self.powerup and player_circle.colliderect(clyde.rect) and not clyde.dead and not self.eaten_ghost[3]:
            self.clyde_dead = True
            self.eaten_ghost[3] = True
            self.score += (2 ** self.eaten_ghost.count(True)) * 100
       
       
   
    def gameLoop(self):
       
        player = Player()
        run = True
        while run:
            self.timer.tick(self.fps)
            if self.counter < 19:
                self.counter += 1
                if self.counter > 3:
                    self.flicker = False
            else:
                self.counter = 0
                self.flicker = True
            if self.powerup and self.power_counter < 600:
                self.power_counter += 1
            elif self.powerup and self.power_counter >= 600:
                self.power_counter = 0
                self.powerup = False
                self.eaten_ghost = [False, False, False, False]
            if self.startup_counter < 180 and not self.game_over and not self.game_won:
                self.moving = False
                self.startup_counter += 1
            else:
                self.moving = True

            self.screen.fill('black')
            self.draw_board(self.level)
            self.center_x = self.player_x + 23
            self.center_y = self.player_y + 24
            if self.powerup:
                self.ghost_speeds = [1, 1, 1, 1]
            else:
                self.ghost_speeds = [2,2,2,2]
                self.player_speed=2
            if self.eaten_ghost[0]:
                self.ghost_speeds[0] = 2
            if self.eaten_ghost[1]:
                self.ghost_speeds[1] = 2
            if self.eaten_ghost[2]:
                self.ghost_speeds[2] = 2
            if self.eaten_ghost[3]:
                self.ghost_speeds[3] = 2
            if self.blinky_dead:
                self.ghost_speeds[0] = 4
            if self.inky_dead:
                self.ghost_speeds[1] = 4
            if self.pinky_dead:
                self.ghost_speeds[2] = 4
            if self.clyde_dead:
                self.ghost_speeds[3] = 4
            

            self.game_won = True
            for i in range(len(self.level)):
                if 1 in self.level[i] or 2 in self.level[i]:
                    self.game_won = False
            if self.time<=0:
                self.game_over=True
            
       

            player_circle = pygame.draw.circle(self.screen, 'black', (self.center_x, self.center_y), 20, 2)
            player.draw_player(self.direction, self.player_x, self.player_y, self.counter, self.screen, self.player_images)
            blinky = Ghost(self.blinky_x, self.blinky_y, self.targets[0], self.ghost_speeds[0], self.blinky_img, self.blinky_direction, self.blinky_dead,
                           self.blinky_box, self.powerup, 0)
            inky = Ghost(self.inky_x, self.inky_y, self.targets[1], self.ghost_speeds[1], self.inky_img, self.inky_direction, self.inky_dead,
                         self.inky_box, self.powerup, 1)
            pinky = Ghost(self.pinky_x, self.pinky_y, self.targets[2], self.ghost_speeds[2], self.pinky_img, self.pinky_direction, self.pinky_dead,
                          self.pinky_box, self.powerup, 2)
            clyde = Ghost(self.clyde_x, self.clyde_y, self.targets[3], self.ghost_speeds[3], self.clyde_img, self.clyde_direction, self.clyde_dead,
                          self.clyde_box, self.powerup, 3)
            self.draw_misc(self.game_won, self.game_over, self.lives)
            self.targets = self.get_targets(self.blinky_x, self.blinky_y, self.inky_x, self.inky_y, self.pinky_x, self.pinky_y, self.clyde_x,
                                        self.clyde_y, blinky, pinky, inky, clyde, self.player_x, self.player_y, self.powerup)
            self.moving=True
            if not self.check:
                if not self.happy.start():
                    self.happy.start()
                    self.moving=False
                else:
                    self.check=True
                    self.quitter=False
            if self.game_won:
                self.moving=False
           
               

            self.turns_allowed = player.check_position(self.center_x, self.center_y, self.direction, self.level)
           
            time_text = self.font.render(f'Time: {self.time//60}', True, 'white')
            self.screen.blit(time_text, (350, 45))
            if self.pauseMenu.show():
                self.pauseMenu.PauseMenu()
                if self.pauseMenu.quit_button():
                    self.quitter=True
                    self.happy.clicked_start=False
                self.moving=False
                if self.pauseMenu.PauseMenu():
                    self.moving=True
               
            if self.moving:
                if self.time>0:
                    self.time-=1
                self.player_x, self.player_y = player.move_player(self.player_x, self.player_y, self.turns_allowed, self.direction, self.player_speed)
                if not self.blinky_dead and not blinky.in_box:
                    self.blinky_x, self.blinky_y, self.blinky_direction = blinky.move_blinky()
                else:
                    self.blinky_x, self.blinky_y, self.blinky_direction = blinky.move_clyde()
                if not self.pinky_dead and not pinky.in_box:
                    self.pinky_x, self.pinky_y, self.pinky_direction = pinky.move_pinky()
                else:
                    self.pinky_x, self.pinky_y, self.pinky_direction = pinky.move_clyde()
                if not self.inky_dead and not inky.in_box:
                    self.inky_x, self.inky_y, self.inky_direction = inky.move_inky()
                else:
                    self.inky_x, self.inky_y, self.inky_direction = inky.move_clyde()
                self.clyde_x, self.clyde_y, self.clyde_direction = clyde.move_clyde()
            self.score, self.powerup, self.power_counter, self.eaten_ghost = self.check_collisions(self.score, self.powerup, self.power_counter, self.eaten_ghost, self.center_x, self.center_y, self.player_x, self.level)
            # add to if not powerup to check if eaten ghosts
            self.reset_positions(player_circle, blinky, inky, pinky, clyde)
           

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.direction_command = 0
                    if event.key == pygame.K_LEFT:
                        self.direction_command = 1
                    if event.key == pygame.K_UP:
                        self.direction_command = 2
                    if event.key == pygame.K_DOWN:
                        self.direction_command = 3
                   
                   

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT and self.direction_command == 0:
                        self.direction_command = self.direction
                    if event.key == pygame.K_LEFT and self.direction_command == 1:
                        self.direction_command = self.direction
                    if event.key == pygame.K_UP and self.direction_command == 2:
                        self.direction_command = self.direction
                    if event.key == pygame.K_DOWN and self.direction_command == 3:
                        self.direction_command = self.direction

            if self.direction_command == 0 and self.turns_allowed[0]:
                self.direction = 0
            if self.direction_command == 1 and self.turns_allowed[1]:
                self.direction = 1
            if self.direction_command == 2 and self.turns_allowed[2]:
                self.direction = 2
            if self.direction_command == 3 and self.turns_allowed[3]:
                self.direction = 3

            if self.player_x > 900:
                self.player_x = -47
            elif self.player_x < -50:
                self.player_x = 897

            if blinky.in_box and self.blinky_dead:
                self.blinky_dead = False
            if inky.in_box and self.inky_dead:
                self.inky_dead = False
            if pinky.in_box and self.pinky_dead:
                self.pinky_dead = False
            if clyde.in_box and self.clyde_dead:
                self.clyde_dead = False
            
           
           

            pygame.display.flip()
        pygame.quit()

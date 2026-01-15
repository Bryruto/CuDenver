import pygame
import random 
import math 



pygame.init()
height,width = 720,720#make so people can change this in game
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

fps = 240 
game_state = "main"

alien_img = pygame.image.load('alien.png').convert_alpha()
background = pygame.image.load('background.png').convert()
background = pygame.transform.scale(background,(width,height))
player_img = pygame.image.load('ship.png').convert_alpha()
bullet_img = pygame.image.load('bullet.png').convert_alpha()
buy_img = pygame.image.load('menu.png').convert_alpha()
pistol = pygame.image.load('pistol.png').convert_alpha()

# all classes will be here and can take from any of the above 
# variable well be in the class that they are being used in 
# all children classes will be right after 

class Player:
    def __init__(self,x,y):
        self.img = player_img.get_rect(center=(x,y))
        self.x = x
        self.y = y
        self.coins = 0
        
        


class Alien:
    def __init__(self):
        pass

class Guns:
    def __init__(self,name,damage,fire_rate):
        self.name = name
        self.damage = damage 
        self.fire_rate = fire_rate




        

    

#this is where the game states will be
running = True
while running: 
    if game_state == "main":
        background.blit(background,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    elif game_state == "game_loop":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    elif game_state == "buy_menu":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    elif game_state == "settings":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
import pygame
import random

pygame.init()
height,width =720,1200
screen = pygame.display.set_mode((width, height))

alien_img = pygame.image.load('alien.png').convert_alpha()
background = pygame.image.load('background.png').convert()
background = pygame.transform.scale(background,(width,height))
player_img = pygame.image.load('ship.png').convert_alpha()
blue_bullet_img = pygame.image.load('blue.png').convert_alpha()#where im at making a bullet to shoot aliens


bue_bullet_img = pygame.transform.scale(blue_bullet_img,(5,5))

clock = pygame.time.Clock()

timer = pygame.time.get_ticks()

SPAWN_ALIEN = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_ALIEN,5000)

class normal_alien:
    def __init__(self,x,y):
        self.alien = alien_img.get_rect(center=(x,y))
        self.x = x
        self.y = y
        self.forword = True

    def move_alien(self):
        if self.x >= width - 70:
            self.forword = False
        elif self.x <= 15:
            self.forword = True

        if self.forword == True:
            self.x += 1
        else:
            self.x -=1
        self.y += 0.3



class player_sprite:
    def __init__(self,x,y):
        self.player = player_img.get_rect(center=(x,y))
        self.x = x
        self.y = y

class bullet(player_sprite):
    def __init__(self,x,y):
        super.__init__(x,y)
        self.bullet = blue_bullet_img.get_rect(center=(x,y))
        self.x = x 
        self.y = y

    

player = player_sprite(int(width/2),height-80)
aliens = [normal_alien(random.randint(0,1100),10)]
active_bullets = []


running = True
while running:
    screen.blit(background,(0,0))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= 1
    if keys[pygame.K_RIGHT]:
        player.x +=1
    if keys[pygame.K_SPACE]:
        active_bullets.append(bullet(player.x,player.y))

    for b in active_bullets:
        b.y-= 1
        screen.blit(blue_bullet_img,(b.x,b.y))

    screen.blit(player_img,(player.x,player.y))

    for a in aliens:
        a.move_alien()
        screen.blit(alien_img,(a.x,a.y))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == SPAWN_ALIEN:
            aliens.append(normal_alien(random.randint(0,1100),10))


    pygame.display.flip()

    clock.tick(60)

    

import pygame
import random
#setting the core elements of the game 
pygame.init()
height,width =720,720
screen = pygame.display.set_mode((width, height))

#adding all the sprites as surfacesies
alien_img = pygame.image.load('alien.png').convert_alpha()
background = pygame.image.load('background.png').convert()
background = pygame.transform.scale(background,(width,height))#fixing the size of backgroud to fit any size
player_img = pygame.image.load('ship.png').convert_alpha()
bullet_img = pygame.image.load('bullet.png').convert_alpha()

#game clock how much stuff happens in a sec fps 
clock = pygame.time.Clock()

#custom event to make a alien spawn every 5sec
SPAWN_ALIEN = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_ALIEN,5000)


#alien class give each alien a hitbox and position
class normal_alien:
    def __init__(self,x,y):
        self.alien = alien_img.get_rect(center=(x,y))
        self.x = x
        self.y = y
        self.forword = True
#how the alien is moving
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
    
    def update(self):
        self.alien.center = (self.x,self.y)


#player class gives a hitbox and position
class player_sprite:
    def __init__(self,x,y):
        self.player = player_img.get_rect(center=(x,y))
        self.x = x
        self.y = y

    def update(self):
        self.player.center = (self.x,self.y)

#bullet class gives a hitbox and position
class bullet():
    def __init__(self,x,y):
        self.bullet = bullet_img.get_rect(center=(x,y))
        self.x = x 
        self.y = y


    def update(self):
        self.bullet.center = (self.x,self.y)


#the player will be in the middle at the bottom
player = player_sprite(int(width/2),height-80)
aliens = []
active_bullets = []

#gun delay want to add a lot of different goes and add health for the aliens 
fire_delay = 200
last_fire = 0

#this is the game loop
running = True
while running:
    screen.blit(background,(0,0))#blit just puts the surface on your screen

    #checks if key press and delays 
    keys = pygame.key.get_pressed()

    now = pygame.time.get_ticks()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.x -= 1
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.x +=1
    if keys[pygame.K_SPACE] and now - last_fire >= fire_delay:
        active_bullets.append(bullet(player.x,player.y))
        last_fire = now


    screen.blit(player_img,(player.x,player.y))

    #put all the aliens on the screen 
    if aliens:
        for a in aliens:
            a.move_alien()
            screen.blit(alien_img,(a.x,a.y))
        aliens = [a for a in aliens if a.y < height - 50]

    #add the bullets and check if they hit anything 
    if active_bullets:
        for b in active_bullets:
            b.y-= 8
            screen.blit(bullet_img,(b.x,b.y))
        

        tmp_a = aliens[:]
        tmp_b = active_bullets[:]
        for a in tmp_a:
            a.update()
            for b in tmp_b:
                b.update()
                if a.alien.colliderect(b.bullet):
                    if a in aliens: aliens.remove(a)
                    if b in active_bullets:active_bullets.remove(b)

        active_bullets = [b for b in active_bullets if b.y > 0]

    #end the game with the x in the top left and spawner event 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == SPAWN_ALIEN:
            aliens.append(normal_alien(random.randint(0,width),10))

    #display to the sceen everything done above and set fps
    pygame.display.flip()

    clock.tick(60)

    

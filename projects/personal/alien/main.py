import pygame
import random
import math


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
buy_img = pygame.image.load('menu.png').convert_alpha()

#the point counter font and font render
font = pygame.font.Font(None, 36)
white = (255,255,255)
class points:
    def __init__(self,x,y):
        self.points = font.render("Points:0",True,white)
        self.count = 0
        self.x = x
        self.y = y
    
    def update(self):
        self.count += 1
        self.points = font.render(f"Points:{self.count}",True,(255,255,255))

point_tracker = points(10,10)

#game clock how much stuff happens in a sec fps 
clock = pygame.time.Clock()

#custom event to make a alien spawn every 5sec
SPAWN_ALIEN = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_ALIEN,5000)
level1 = False

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
class bullet:
    def __init__(self,x,y,to_x,to_y,speed=8):
        self.bullet = bullet_img.get_rect(center=(x,y))

        self.x = x 
        self.y = y
        self.to_x = to_x 
        self.to_y = to_y
        self.speed = speed


        dx = self.to_x - self.x
        dy = self.to_y - self.y
        angle = math.hypot(dx,dy)

        if angle == 0:
            self.angle_x = 0
            self.angle_y = 0
        else:
            self.angle_x = dx / angle * speed
            self.angle_y = dy / angle * speed


    def hitbox(self):
        self.bullet.center = (self.x,self.y)

    def update(self):
        self.x += self.angle_x
        self.y += self.angle_y

#working on this one as of now 
class button:
    def __init__(self,text,color,x,y):
        self.text = font.render(text,True,color)
        self.color = color
        self.rect = self.text.get_rect(center=(x,y))
        self.x = x 
        self.y = y

class buy_menu:
    def __init__(self,img,x,y):
        self.img = buy_img.get_rect(center=(x,y))
        self.x = x
        self.y = y

    def clicked(self):
        pass

#the player will be in the middle at the bottom
player = player_sprite(int(width/2),height-80)
aliens = []
active_bullets = []

#gun delay want to add a lot of different goes and add health for the aliens 
fire_delay = 1000
last_fire = 0

upgrade_menu = button("Buy",)
def game_loop():
    #this is the game loop
    global aliens, active_bullets, last_fire, level1
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
        """if keys[pygame.K_SPACE] and now - last_fire >= fire_delay:
            active_bullets.append(bullet(player.x,player.y,to_x,to_y)) #this is shooting with the space bar
            last_fire = now"""


        screen.blit(player_img,(player.x,player.y))

        #put all the aliens on the screen 
        if aliens:
            for a in aliens:
                a.move_alien()
                screen.blit(alien_img,(a.x,a.y))
            aliens[:] = [a for a in aliens if a.y < height - 50]

        #add the bullets and check if they hit anything 
        if active_bullets:
            for b in active_bullets:
                b.update()
                screen.blit(bullet_img,(b.x,b.y))
            

            tmp_a = aliens[:]
            tmp_b = active_bullets[:]
            for a in tmp_a:
                a.update()
                for b in tmp_b:
                    b.hitbox()
                    if a.alien.colliderect(b.bullet):
                        if a in aliens:
                            aliens.remove(a)
                            point_tracker.update()
                        if b in active_bullets:
                            active_bullets.remove(b)

            active_bullets[:] = [b for b in active_bullets if b.y > 0]

        screen.blit(point_tracker.points,(point_tracker.x,point_tracker.y))
            
        

        #end the game with the x in the top left and spawner event 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


            if event.type == SPAWN_ALIEN:
                aliens.append(normal_alien(random.randint(0,width),10))


            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and now - last_fire >= fire_delay:
                    to_x, to_y = event.pos
                    active_bullets.append(bullet(player.x,player.y,to_x,to_y))
                    last_fire = now

        if point_tracker.count >= 2 and not level1:
            level1 = True
            pygame.time.set_timer(SPAWN_ALIEN,1000)
            

        #display to the sceen everything done above and set fps
        pygame.display.flip()

        clock.tick(60)


start = button("Start",white,width/2, height/2)

#making the main menu
def main_menu():
    running = True
    while running:
        screen.blit(background,(0,0))
        screen.blit(start.text,start.rect)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start.rect.collidepoint(event.pos):
                    running = False
                    game_loop()

        pygame.display.flip()
        clock.tick(60)

main_menu()
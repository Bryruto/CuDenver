import pygame# pygame runs on cpu 

pygame.init()
screen = pygame.display.set_mode((1200, 720))

potato_img = pygame.image.load('potato.png').convert()#this makes a surface think of a window on top a window but its not ontop till blit

#use .convert_alpha() if the image has a transparent background
#use potato_img.set_colorkey((0, 0, 0)) this is saying ignore black


potato_img = pygame.transform.scale(potato_img,
                                    (potato_img.get_width() * 2,
                                     potato_img.get_height() * 2)) #this is just changing the size of the image

#this is a group of an images that move together
# potatoes= pygame.Surface((64,64), pygame.SRCALPHA)
# potatoes.blit(potato_img, (0, 0))
# potatoes.blit(potato_img, (20, 0))
# potatoes.blit(potato_img, (10, 10))


font = pygame.font.Font(None, size= 30)

running = True 

delta_time = 0.1 #this is used to messure time between frames this is just the vairaible tho 

x = 0 
clock = pygame.time.Clock()#need this to slow the game down or just control the speed

moving = False # this is how you make key based movement
while running: #this is a game play loop if you click x and the top left you will quit 
    screen.fill((255,255,255)) #rgb values for the backround of window

    #to make how visable an image is potato_img.set_alpha(0,255 - x) this will make it disapear over time

    #y is going down and x is going right starts on the top left corner thats why(0,0) 
    screen.blit(potato_img, (x,30)) #so we have an image on the screen now surface on our window surface
    if moving:
        x+= 50 * delta_time #this is how you make movement delta_time makes it the same with all frame rates 

    text= font.render('Hello World!',True, (0,0,0))
    screen.blit(text,(300, 100))#this is how you make text


    hitbox= pygame.Rect(x, 30, potato_img.get_width(),potato_img.get_height())#hitbox what other surfaces with a hit box can touch

    mpos = pygame.mouse.get_pos() #ask where the mouse is so you have the position

    target = pygame.Rect(300, 0, 160, 280) #this is a surface that hitbox can touch and make somthing happen
    collision = hitbox.collidedict(target) #this is a if its touching hitbox
    m_collision = target.collidepoint(mpos)#checks if its touching target
    pygame.draw.rect(screen, (255 * collision ,255  * m_collision,0), target) #make a image for the target hitbox and when it hits change red value


    for event in pygame.event.get():#this is checking for events so someone clicks something and then something happens 
        if event.type == pygame.QUIT: #if you click x on the top left 
            running = False #this is just a break so you leave the loop 
            #you can make movement like 
            if event.type == pygame.KEYDOWN: #if you press down key then move  
                if event.key == pygame.K_d:
                    moving = True

    pygame.display.flip()#this is refresh rate

    #clock.tick(60)always just 60 this way

    delta_time = clock.tick(60)/ 1000 #frames per secound
    delta_time = max(0.001, min(0.1 , delta_time)) #becuase its moving surfaces this will make it not go off screen

pygame.quit()#this will close the window


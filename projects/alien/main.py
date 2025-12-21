import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 720))

desired_size = (100, 75)

aliens_img = pygame.image.load('alien.png').convert_alpha()
ship_img = pygame.image.load('ship.png').convert_alpha()

aliens_img = pygame.transform.scale(aliens_img, desired_size)

clock = pygame.time.Clock()

running = True
while running:
    screen.fill((255,255,255))

    screen.blit(aliens_img, (10, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    clock.tick(60)
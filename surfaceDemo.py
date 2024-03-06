import pygame
pygame.init()

screen = pygame.display.set_mode((500, 500))

bat = pygame.image.load("/home/boog/workspace/pygameTest/tongue.png")

# screen.blit(bat, (250,250))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bat, (250,250))

    pygame.display.flip()
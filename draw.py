import pygame

pygame.init() # Initialize Pygame
screen = pygame.display.set_mode((640, 480)) # Create a window of 640x480 pixels
screen.fill((255, 255, 255)) # Fill the screen with white

# Sky
pygame.draw.rect(screen, (66, 215, 245), pygame.Rect(0,0,640,480))

# Grass
pygame.draw.rect(screen, (0,255,0), pygame.Rect(-100,350,1000,1000))

# House Foundation
pygame.draw.rect(screen, (89, 23, 31), pygame.Rect(100,180,441,200))

# House Door
pygame.draw.rect(screen, (255,255,255), pygame.Rect(400,300,40,80))

# House Roof
pygame.draw.polygon(screen, (41, 13, 16), ((100,180),(540,180),(320,100)))

# Window
pygame.draw.rect(screen, (124, 119, 224), pygame.Rect(200,250,60,60))


# Make sure the window stays open until the user closes it
run_flag = True
while run_flag is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False
    pygame.display.flip() # Refresh the screen so drawing appears
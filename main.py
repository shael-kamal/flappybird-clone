"""
Created with pygame module. Based on and used assets from YouTube channel Clear Code.

Pygame documentation: https://www.pygame.org/docs/
Clear Code Channel: https://www.youtube.com/channel/UCznj32AM2r98hZfTxrRo9bQ
Assets: https://github.com/samuelcust/flappy-bird-assets
Audio: https://www.sounds-resource.com/mobile/flappybird/sound/5309/

"""

import pygame, sys

pygame.init()  # Initializes pyGame

# Variables
frames = 120  # How many frames refreshed per second
s_dimensions = (576, 1024)  # Tuple with dimensions of the screen variable (width, height)
# Images - Imported images are surfaces stored inside variables (similar to display surface - screen)
bg_surface = pygame.image.load('assets/sprites/background-day.png').convert()  # background image
bg_surface = pygame.transform.scale2x(bg_surface)  # transform: module that lets you do geometric transformations

# Create a surface to display game, normally called a screen, arguments are the dimensions in a tuple (width,height).
screen = pygame.display.set_mode(s_dimensions)

# time: a pygame module that monitors time
clock = pygame.time.Clock()

# Start the game loop
while True:  # This runs until loop is broken from the inside
    # Create event loop to listen for events every iteration of the while loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Checks type of event
            pygame.quit()  # This is the opposite of pygame.init()
            sys.exit()  # Allows us to completely exit window. Uses sys module
    # Put images on the screen, Must be inside game loop. surface1.blit(surface2,(x,y))
    screen.blit(bg_surface, (0, 0))  # blit: method used to put one surface on another one.

    pygame.display.update()  # Refresh everything above it while the loop runs
    clock.tick(frames)  # Sets target FPS to the one specified (can run slower but will not run faster).

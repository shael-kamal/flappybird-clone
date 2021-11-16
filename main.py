"""
Created with pygame module. Based on and used assets from YouTube channel Clear Code.
Pygame documentation: https://www.pygame.org/docs/
Clear Code Channel: https://www.youtube.com/channel/UCznj32AM2r98hZfTxrRo9bQ
Assets: https://github.com/samuelcust/flappy-bird-assets
Audio: https://www.sounds-resource.com/mobile/flappybird/sound/5309/
"""

import pygame, sys


def draw_floor():
    screen.blit(floor_surface, (floor_x_position, 400))
    screen.blit(floor_surface, (floor_x_position + s_dimensions[0], 400))


pygame.init()  # Initializes pyGame

# Create a surface to display game, normally called a screen, arguments are the dimensions in a tuple (width,height).
screen = pygame.display.set_mode((288, 576))

# time: a pygame module that monitors time
clock = pygame.time.Clock()

# Variables
gravity = 0.25  # will be applied on bird_movement
bird_movement = 0  # will move the rect

frames = 120  # How many frames refreshed per second
s_dimensions = (288, 576)  # Tuple with dimensions of the screen variable (width, height)

# Images - Imported images are surfaces stored inside variables (similar to display surface - screen)
bg_surface = pygame.image.load('assets/sprites/background-day.png').convert()  # background image
# bg_surface = pygame.transform.scale2x(bg_surface)  # transform: module that lets you do geometric transformations

floor_surface = pygame.image.load('assets/sprites/base.png').convert()  # floor image (looks like constantly in motion)
# floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_position = 0  # x-coordinate of floor

bird_surface = pygame.image.load('assets/sprites/bluebird-midflap.png').convert()  # initial bird image
# bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center=(50, 256))  # rect: will be used for collisions

# Start the game loop
while True:  # This runs until loop is broken from the inside
    # Create event loop to listen for events every iteration of the while loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Checks type of event
            pygame.quit()  # This is the opposite of pygame.init()
            sys.exit()  # Allows us to completely exit window. Uses sys module

        if event.type == pygame.KEYDOWN:  # checks if any type of key has been pressed
            if event.key == pygame.K_SPACE:
                bird_movement = 0  # Nullifies effect of gravity
                bird_movement -= 6  # Modifies bird movement

    # Put images on the screen, Must be inside game loop. surface1.blit(surface2,(x,y))
    screen.blit(bg_surface, (0, 0))  # blit: method used to put one surface on another one.

    bird_movement += gravity
    bird_rect.centery += bird_movement  # changes y axis of center by bird_movement variable
    screen.blit(bird_surface, bird_rect)  # draws bird on the main surface

    floor_x_position -= 1  # X position of floor_surface is updated every iteration (creates moving floor)
    draw_floor()  # Function for drawing floor
    if floor_x_position <= -288:  # Conditional to create endless floor
        floor_x_position = 0

    pygame.display.update()  # Refresh everything above it while the loop runs
    clock.tick(frames)  # Sets target FPS to the one specified (can run slower but will not run faster).

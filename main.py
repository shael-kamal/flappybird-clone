"""
Created with pygame module. Based on and used assets from YouTube channel Clear Code.
Pygame documentation: https://www.pygame.org/docs/
Clear Code Channel: https://www.youtube.com/channel/UCznj32AM2r98hZfTxrRo9bQ
Assets: https://github.com/samuelcust/flappy-bird-assets
Audio: https://www.sounds-resource.com/mobile/flappybird/sound/5309/
"""

import pygame, sys, random

# Functions
def draw_floor():
    screen.blit(floor_surface, (floor_x_position, 400))
    screen.blit(floor_surface, (floor_x_position + s_dimensions[0], 400))

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (350,random_pipe_pos))  #creates new pipes
    top_pipe = pipe_surface.get_rect(midbottom = (350,random_pipe_pos-100))
    return bottom_pipe,top_pipe

def move_pipes(pipes):  #takes list of pipes as an argument
    for pipe in pipes:
        pipe.centerx -= 2  #Changes center x coordinated of each pipe in list
    return pipes

def draw_pipes(pipes): #takes list of pipes as arg
    for pipe in pipes:
        if pipe.bottom>512:
            screen.blit(pipe_surface,pipe)
        else:
            screen.blit(pygame.transform.rotate(pipe_surface,180), pipe)
pygame.init()  # Initializes pyGame

# Create a surface to display game, normally called a screen, arguments are the dimensions in a tuple (width,height).
screen = pygame.display.set_mode((288, 512))

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

pipe_surface = pygame.image.load('assets/sprites/pipe-green.png').convert()  #pipe image
pipe_list = []  #will be addind rectangles to the list
SPAWNPIPE = pygame.USEREVENT  # new event that will be used as a timer
pygame.time.set_timer(SPAWNPIPE,1200)  #event that will be triggered every 1.2 seconds
pipe_height = [200,250,300,350,400]  # list of possible heights of pipes

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

        if event.type == SPAWNPIPE:  # Creating a listener to spawn pipes at every interval
            pipe_list.extend(create_pipe())
    # Put images on the screen, Must be inside game loop. surface1.blit(surface2,(x,y))
    screen.blit(bg_surface, (0, 0))  # blit: method used to put one surface on another one.

    #BIRD
    bird_movement += gravity
    bird_rect.centery += bird_movement  # changes y axis of center by bird_movement variable
    screen.blit(bird_surface, bird_rect)  # draws bird on the main surface

    #PIPE
    move_pipes(pipe_list)
    draw_pipes(pipe_list)

    #FLOOR
    floor_x_position -= 1  # X position of floor_surface is updated every iteration (creates moving floor)
    draw_floor()  # Function for drawing floor
    if floor_x_position <= -288:  # Conditional to create endless floor
        floor_x_position = 0

    pygame.display.update()  # Refresh everything above it while the loop runs
    clock.tick(frames)  # Sets target FPS to the one specified (can run slower but will not run faster).

import pygame

FPS = 60 # frames per second to update the screen
WINWIDTH = 1200 # width of the program's window, in pixels
WINHEIGHT = 800 # height in pixels
HALF_WINWIDTH = int(WINWIDTH / 2)
HALF_WINHEIGHT = int(WINHEIGHT / 2)

# The total width and height of each tile in pixels.
TILEWIDTH = 50
TILEHEIGHT = 50
TILEFLOORHEIGHT = 50

CAM_MOVE_SPEED = 5 # how many pixels per frame the camera moves

# The percentage of outdoor tiles that have additional
# decoration on them, such as a tree or rock.
OUTSIDE_DECORATION_PCT = 20

# BRIGHTBLUE = (  0, 170, 255)
BLACKCOLOR = (22, 22, 22)

WHITE      = (255, 255, 255)
BGCOLOR = BLACKCOLOR
TEXTCOLOR = WHITE

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'


# click_sounds = pygame.mixer.Sound('assets/mp3/click.wav')
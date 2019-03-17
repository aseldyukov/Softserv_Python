import pygame
pygame.init()
screen=pygame.display.set_mode((400,300))
pygame.display.set_caption("My first game")
clock=pygame.time.Clock()
crashed = False
ORANGE = (255, 150, 100)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
PI = 3.14


# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# -------- Main Program Loop -----------
# while not crashed:
#     for event in pygame.event.get():
        # if event.type == pygame.QUIT:
        #     print("User asked to quit.")
        # elif event.type == pygame.KEYDOWN:
        #     print("User pressed a key.")
        # elif event.type == pygame.KEYUP:
        #     print("User let go of a key.")
        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     print("User pressed a mouse button")

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    #pygame.draw.line(screen, (255,255,255), [10, 30], [290, 15], 3)
    # pygame.draw.line(screen, WHITE, [10, 30], [290, 15], 3)
    # pygame.draw.line(screen, WHITE, [10, 50], [290, 35])
    
    # #aaline згладжена лінія, товщина в цьому
    # # випадку не задається
    # pygame.draw.aaline(screen, WHITE, [10, 70], [290, 55])
    # pygame.draw.circle(screen, YELLOW, (100, 100), 50)
    # pygame.draw.circle(screen, PINK, (200, 100), 50, 10)

    # pygame.draw.ellipse(screen, GREEN, (10, 50, 280, 100))
    pygame.draw.rect(screen, WHITE, (20, 20, 100, 75))
    pygame.draw.rect(screen, (64, 128, 255), (150, 20, 100, 75), 8)
    pygame.display.update()

    clock.tick(60)

pygame.quit()
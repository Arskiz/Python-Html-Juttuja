import pygame
import random
import string
import sys
import oai

# Initialize pygame
pygame.init()


# Define window size
HEIGHT = 720
WIDTH = 720
res = (WIDTH, HEIGHT)

# Set up the display
screen = pygame.display.set_mode(res)
pygame.display.set_caption('Eka')

# Define colors
WHITE = (255,255,255)
BLACK = (0,0,0)

# FPS
fps = 60
clock = pygame.time.Clock()

# Define caption
all = string.ascii_lowercase + string.punctuation + string.digits
newList = []
for i in all:
    newList.append(i)

# Define line width
line_width = 5


# Define sprites:


def draw():
    #Fill screen with white color
    screen.fill(WHITE)
    
    ### Draw lines ###
    
    # Vertical
    pygame.draw.line(screen, BLACK, (WIDTH / 3, HEIGHT), (WIDTH / 3, 0), line_width)
    pygame.draw.line(screen, BLACK, (WIDTH / 1.5, HEIGHT), (WIDTH / 1.5, 0), line_width)
    
    # Horizontal
    pygame.draw.line(screen, BLACK, (WIDTH, HEIGHT / 3), (0, HEIGHT / 3), line_width)
    pygame.draw.line(screen, BLACK, (WIDTH, HEIGHT / 1.5), (0, HEIGHT / 1.5), line_width)
    
    ### Draw lines ###
    
    
    
    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(fps)
    
def chooseRandom(list):
    return random.choice(list)

def captionTicker():
    
    text = ""
    captionSize = random.randrange(5, 30)
    
    for i in range(captionSize):
        text = text.__add__(random.choice(newList))
    pygame.display.set_caption(text)


sprites = []
for i in pygame.sprite:
    sprites.append(i)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if  event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            
            # get a list of all sprites that are under the mouse cursor
            clicked_sprites = [s for s in sprites if s.rect.collidepoint(pos)]
    draw()
    
    captionTicker()
    
    mouse = pygame.mouse.get_pos()
    
    
    # Update game state here

    # Clear the screen
   
    

    # Draw your game elements here (if any)

    # Update the display
    pygame.display.flip()

import pygame
from constants import *

def main():
    #initialize the game and necessary objects/variables
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 #delta time
    fps = 60

    #game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        pygame.display.flip()
        dt = clock.tick(fps) / 1000

if __name__ == "__main__":
    main()

import pygame
from constants import *
from player import Player

def main():
    #initialize the game and necessary objects/variables
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2))
    dt = 0 #delta time

    #game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(FPS) / 1000

if __name__ == "__main__":
    main()

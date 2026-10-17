import pygame
from constants import *
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # game loop
    while True:
        log_state()     # create log
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
        
        screen.fill("black")

        pygame.display.flip()

if __name__ == "__main__":
    main()

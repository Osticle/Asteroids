import pygame
from constants import *
from logger import log_state
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from logger import log_event
import sys
from circleshape import CircleShape
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create time clock
    clock = pygame.time.Clock()
    dt = 0.0

    # create object group
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # add class to group
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # create player and asteroid field
    player_pos_x = SCREEN_WIDTH / 2
    player_pos_y = SCREEN_HEIGHT / 2
    player = Player(player_pos_x, player_pos_y)
    asteroid_field = AsteroidField()

    # game loop
    while True:
        log_state()     # create log
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
        
        screen.fill("black")
        updatable.update(dt)
        
        # Check player collision
        for _asteroid in asteroids:
            if _asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            else:
                continue
        
        # Check bullet collision
        for _asteroid in asteroids:
            for _shot in shots:
                if _asteroid.collides_with(_shot):
                    log_event("asteroid_shot")
                    pygame.sprite.Sprite.kill(_shot)
                    _asteroid.split()
                else:
                    continue


        
        for _object in drawable: 
            _object.draw(screen)
        

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

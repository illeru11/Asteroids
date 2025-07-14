import pygame, sys
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    
    #create groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()



    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

    # Create a player instance along with other game objects
    Player.containers = (updateable,drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids,updateable,drawable)
    Shot.containers = (shots, updateable,drawable)

    AsteroidField.containers = (updateable,)
    field =AsteroidField() 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))  # Fill the screen with black

        for objects in updateable:
            objects.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player)== True:
                print("Game over!")
                sys.exit()
        
        for drawing in drawable:
            drawing.draw(screen)
            #player.update(dt)
            #player.draw(screen)
        
        


        pygame.display.flip()
        
        dt_ms = clock.tick(60)
        dt = dt_ms/1000
        
        


if __name__ == "__main__":
    main()




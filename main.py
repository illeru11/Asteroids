import pygame
from constants import *
from player import Player
def main():
    
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

    # Create a player instance
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))  # Fill the screen with black
        player.draw(screen)
        pygame.display.flip()
        
        dt_ms = clock.tick(60)
        dt = dt_ms/1000
        
        


if __name__ == "__main__":
    main()




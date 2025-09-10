# this allows us to use code from the open-source pygame library throughout this file.
import pygame
from constants import *

def main():
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # init pygame
    pygame.init()
    
    # Set screen dimensions
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Fill the entire screen with black
        black = (0,0,0)
        screen.fill(black)
        
        # Refresh the screen
        pygame.display.flip()

if __name__ == "__main__":
    main()

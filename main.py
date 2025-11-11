import pygame, sys #type: ignore
from asteroid import *
from constants import *
from player import *
from asteroidfield import *
from shot import *

def main():
    # init pygame
    pygame.init()
    print(f"Starting Asteroids\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable) 
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    
    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT /2)    
    asteroid_field = AsteroidField()
    
    #Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                sys.exit()
        
            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.split()
                
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        
        # Limit the FPS to 60
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()

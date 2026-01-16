import pygame
from config import WIDTH, HEIGHT, FPS
from world import World

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    world = World()

    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        world.tick(dt)
        
        screen.fill((200, 200, 200))
        world.draw(screen)
        pygame.display.flip()
    
    pygame.quit()


if __name__ == "__main__":
    main()
import pygame
from config import WIDTH, HEIGHT, FPS
from world import World
from entity import Entity

def main():
    pygame.init()

    # Initialize entity debug font
    Entity.debug_font = pygame.font.SysFont('Arial', 10)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    world = World(WIDTH, HEIGHT)

    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0

        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Keyboard input
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    Entity.draw_food = not Entity.draw_food


        world.tick(dt)
        
        screen.fill((200, 200, 200))
        world.draw(screen)
        pygame.display.flip()
    
    pygame.quit()


if __name__ == "__main__":
    main()
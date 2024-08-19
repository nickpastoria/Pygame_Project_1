# main.py
import pygame


class World:
    def __init__(self) -> None:
        self.gravity = pygame.math.Vector2(0,-0.5)

class Player:
    def __init__(self) -> None:
        self.position = pygame.math.Vector2(0,0)
        self.size = [100, 100]
        self.color = "Red"
        self.velocity = pygame.math.Vector2(0, 0)
    def update(self, world, keys):
        self.position += self.velocity
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.position, self.size))

def game_draw(clock, screen, player):
    player.draw(screen)
    pygame.display.flip()
    clock.tick(60)

def game_update(screen, player, world):
    keys = pygame.key.get_pressed()
    player.update(world, keys)
    screen.fill("Purple")
    pass

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280,720))
    clock = pygame.time.Clock()
    running = True
    
    player = Player()
    world = World()
    while running:
        game_update(screen, player, world)
        game_draw(clock, screen, player)

if __name__ == "__main__":
    main()

"""Main game module."""
import sys
import pygame
from config import WINDOW_SIZE, MAX_FPS, COLORS, gamestate
from msg import fail, win
from gamecharacter import GameCharacter, Raft

def main():
    pygame.init()

    # Screen and FPS settings.
    screen = pygame.display.set_mode(WINDOW_SIZE)
    screen_surface = screen.get_rect()
    screen.fill((255,255,255))
    pygame.display.flip()
    fps = pygame.time.Clock()

    lose_text = fail(screen_surface)
    win_text = win(screen_surface)
    
    # Cannibal_1 = GameCharacter(screen_surface, (0, 0) , "example/wolf.png")
    # Cannibal_2 = GameCharacter(screen_surface, (0, 100) , "example/wolf.png")
    # Cannibal_3 = GameCharacter(screen_surface, (0, 200) , "example/wolf.png")
    # cannibals = [Cannibal_1, Cannibal_2, Cannibal_3]
    Cannibal_1 = Raft(screen_surface, [500, 250], "example/wolf.png")
    cannibals = [Cannibal_1]
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.K_a:
                print("siema")
            
        screen.fill((255,255,255))
        screen.blit(Cannibal_1.image, Cannibal_1.pos)
        fps.tick(MAX_FPS)
        pygame.display.flip()
    
if __name__ == "__main__":
    main()
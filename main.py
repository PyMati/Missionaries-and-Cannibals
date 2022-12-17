"""Main game module."""
import sys
import pygame
from config import WINDOW_SIZE, MAX_FPS, GAMEGRAPH
from msg import fail, win, welcome, instructions
from gamecharacter import GameCharacter, Raft

# States that helps keep state of the game.
is_start = False
is_game = True
is_win = False


def main():
    global is_game, is_win, is_start
    pygame.init()

    # Screen and FPS settings.
    screen = pygame.display.set_mode(WINDOW_SIZE)
    screen_surface = screen.get_rect()
    background = pygame.image.load("grass.jpg")
    scaled_background = pygame.transform.scale(background, (800, 600))
    screen.blit(scaled_background, (0, 0))
    pygame.display.flip()
    fps = pygame.time.Clock()

    # Text initialization.
    welcome_text = welcome(screen_surface)
    instr_text = instructions()
    lose_text = fail(screen_surface)
    win_text = win(screen_surface)

    def refreshscreen():
        """Draws all characters in game screen."""
        screen.blit(scaled_background, (0, 0))
        for character in all_characters:
            screen.blit(character.image, character.pos)
        screen.blit(raft.image, raft.pos)
        fps.tick(MAX_FPS)
        pygame.display.flip()

    def welcome_screen():
        """Welcome screen text."""
        screen.fill((255, 255, 255))
        screen.blit(welcome_text["msg"], welcome_text["pos"])
        screen.blit(instr_text["msg"], [160, 320])
        pygame.display.flip()

    def lose():
        """Function which creates lose message."""
        screen.fill((255, 255, 255))
        screen.blit(lose_text["msg"], lose_text["pos"])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()

    def winf():
        """Function which creates win message."""
        screen.fill((255, 255, 255))
        screen.blit(win_text["msg"], lose_text["pos"])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()

    # Game objects/ characters initialization.
    raft = Raft([150, 225], "2.png")
    goat_1 = GameCharacter([25, 100], [25, 100], [670, 100],
                           "example/goat.png", type="goat")
    goat_2 = GameCharacter([25, 300], [25, 300], [670, 300],
                           "example/goat.png", type="goat")
    goat_3 = GameCharacter([25, 500], [25, 500], [670, 500],
                           "example/goat.png", type="goat")
    cabb_1 = GameCharacter([25, 200], [25, 200], [670, 200],
                           "example/cabb.png", type="cabb")
    cabb_2 = GameCharacter([25, 400], [25, 400], [670, 400],
                           "example/cabb.png", type="cabb")
    cabb_3 = GameCharacter([25, 0], [25, 0], [670, 0],
                           "example/cabb.png", type="cabb")
    all_characters = [goat_1, goat_2, goat_3, cabb_1, cabb_2, cabb_3]

    # For my info only
    # real_pos = [[[25, 100], [670, 100]],
    #             [[25, 300], [670, 300]],
    #             [[25, 500], [670, 500]],
    #             [[25, 200], [670, 200]],
    #             [[25, 400], [670, 400]],
    #             [[25, 0], [670, 0]]]

    # Places that are available on raft(In this case truck).
    raft_places = [
        {"av": "yes",
         "x": -40},
        {"av": "yes",
         "x": 100}
    ]
    # Main game loop.
    while True:
        if is_start:
            # Game state checker
            gamestate = ["-"]
            for game_character in all_characters:
                if (game_character.type == "goat"
                        and game_character.side == "left"):
                    gamestate.insert(0, "g")
                if (game_character.type == "cabb"
                        and game_character.side == "left"):
                    gamestate.insert(0, "c")
                if (game_character.type == "goat"
                        and game_character.side == "right"):
                    gamestate.insert(len(gamestate), "g")
                if (game_character.type == "cabb"
                        and game_character.side == "right"):
                    gamestate.insert(len(gamestate), "c")

            if gamestate == GAMEGRAPH["win"]:
                is_game = False
                is_win = True

            for lose_check in GAMEGRAPH["lose"]:
                if gamestate == lose_check:
                    is_game = False

            if is_game:
                # Counter that checks if anything is on raft or raft if full.
                counter = 0
                for game_character in range(0, len(all_characters)):
                    if all_characters[game_character].is_on_raft:
                        counter += 1
                    if counter > 0:
                        raft.is_someone = True
                    else:
                        raft.is_someone = False
                    if counter >= 2:
                        raft.is_full = True
                    else:
                        raft.is_full = False

                for event in pygame.event.get():
                    # Exit game
                    if event.type == pygame.QUIT:
                        sys.exit()

                    # Main functionality when sprite is clicked.
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        print(gamestate)
                        pos = pygame.mouse.get_pos()
                        for game_character in range(0, len(all_characters)):
                            # Collide sprite detection
                            if (all_characters[game_character]
                                    .rect.collidepoint(pos)):
                                # Check if the sprite is on the same site
                                if (all_characters[game_character]
                                        .side == raft.state):
                                    # Functionality
                                    if (not all_characters[game_character]
                                            .is_on_raft):
                                        if not raft.is_full:
                                            (all_characters[game_character]
                                                .is_on_raft) = True
                                            for place in raft_places:
                                                if place["av"] == "yes":
                                                    (all_characters
                                                     [game_character]
                                                     .go_on_raft(raft.rect.x,
                                                                 raft.rect.y,
                                                                 place["x"]))
                                                    place["av"] = "no"
                                                    break
                                    else:
                                        (all_characters[game_character]
                                         .quit_raft())
                                        (all_characters[game_character]
                                         .flip_sprite())
                                        for place in raft_places:
                                            if (place["x"] == all_characters
                                                    [game_character].rx):
                                                place["av"] = "yes"
                                        (all_characters
                                         [game_character].is_on_raft) = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            # Raft moving
                            if raft.is_someone:
                                for _ in range(160):
                                    raft.move_raft()
                                    for game_character in range(0, len(all_characters)):
                                        if (all_characters
                                                [game_character].is_on_raft):

                                            (all_characters[game_character]
                                                .move_with_raft
                                                (raft.rect.x, raft.rect.y))
                                    refreshscreen()

                                # Changing the position of raft
                                if raft.state == "right":
                                    raft.state = "left"
                                elif raft.state == "left":
                                    raft.state = "right"

                                # Changing the position of game character.
                                for game_character in range(0, len(all_characters)):
                                    if (all_characters
                                            [game_character].is_on_raft):
                                        (all_characters
                                         [game_character].side) = raft.state

                                raft.flip_sprite()

                refreshscreen()
            else:
                if not is_win:
                    lose()
                else:
                    winf()

        else:
            welcome_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    is_start = True


if __name__ == "__main__":
    main()

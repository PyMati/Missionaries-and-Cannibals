"""This module contains all messages that are used in game."""
import pygame
from config import GAME_FONT, COLORS, INSTRUCTIONS_FONT


pygame.init()

FONT = pygame.font.Font(GAME_FONT[0], GAME_FONT[1])
INS_FONT = pygame.font.Font(INSTRUCTIONS_FONT[0], INSTRUCTIONS_FONT[1])


def fail(screen_surface):
    """Shows lose message in the center of screen."""
    msg = FONT.render("You lose!", True, COLORS["red"])
    msg_surface = msg.get_rect()
    msg_surface.center = screen_surface.center
    data = {
        "msg": msg,
        "pos": msg_surface
    }
    return data


def win(screen_surface):
    """Shows win message in the center of screen."""
    msg = FONT.render("You win!", True, COLORS["green"])
    msg_surface = msg.get_rect()
    msg_surface.center = screen_surface.center
    data = {
        "msg": msg,
        "pos": msg_surface
    }
    return data


def welcome(screen_surface):
    """Shows win message in the center of screen."""
    msg = FONT.render("GOATS AND CABBAGES", True, COLORS["green"])
    msg_surface = msg.get_rect()
    msg_surface.center = screen_surface.center
    data = {
        "msg": msg,
        "pos": msg_surface
    }
    return data


def instructions():
    """Shows instructions message in the center of screen."""
    msg = INS_FONT.render("""Space - Move raft/ Click on character - Move character/ Press anything to start.""",
                          True, COLORS["black"])
    data = {
        "msg": msg,
    }
    return data

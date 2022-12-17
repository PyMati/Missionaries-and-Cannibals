"""Game character/ object classes."""
import pygame


MOVE = [-2.5, 2.5]


class GameCharacter(pygame.sprite.Sprite):
    def __init__(self, pos, pos2, pos3, image_path, type):
        pygame.sprite.Sprite.__init__(self)

        # Type of character
        self.type = type

        # Sprite loading/scalling/surface
        self.image_path = image_path
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()

        # Sprite positioning
        self.pos = pos
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.realpos = pos2
        self.realpos2 = pos3

        # States variable
        self.side = "left"
        self.is_on_raft = False

        # Raft position
        self.rx = 0

    def flip_sprite(self):
        """Flips sprite horizontaly."""
        self.image = pygame.transform.flip(self.image, -1, 0)

    def scale_sprite_down(self):
        """Scales sprite"""
        self.image = pygame.transform.scale(self.image, (60, 46))

    def scale_sprite_up(self):
        """Scales sprite"""
        self.image = pygame.image.load(self.image_path)

    def go_on_raft(self, x, y, distance_x):
        """Sends sprite on raft image."""
        self.scale_sprite_down()
        self.rx = distance_x
        self.pos[0] = x + distance_x
        self.pos[1] = y
        # self.scale_sprite_down()
        self.update_rect()

    def update_rect(self):
        """Updates rectangle of sprite"""
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]

    def move_with_raft(self, x, y):
        """Moves sprite with raft."""
        self.pos[0] = x + self.rx
        self.pos[1] = y
        self.update_rect()

    def quit_raft(self):
        """Transport sprite outside raft."""
        if self.side == "left":
            # print(f"Prawdziwa 1 {self.realpos}")
            self.scale_sprite_up()
            self.pos[0] = self.realpos[0]
            self.pos[1] = self.realpos[1]
            self.update_rect()
        else:
            self.side == "right"
            # print(f"Prawdziwa 2 {self.realpos2}")
            self.scale_sprite_up()
            self.pos[0] = self.realpos2[0]
            self.pos[1] = self.realpos2[1]
            self.update_rect()


class Raft(pygame.sprite.Sprite):
    def __init__(self, pos, image_path):
        super(Raft, self).__init__()

        # Sprite loading/scalling/surface
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()

        # Sprite positioning
        self.pos = pos
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.state = "left"
        self.move = [-2.5, 2.5]
        self.is_full = False
        self.is_someone = False

    def move_raft(self):
        """Function that moves raft left and right."""
        if self.state == "right":
            if self.pos[0] > 150:
                self.pos[0] += self.move[0]
                self.rect.x = self.pos[0]
                self.rect.y = self.pos[1]

        if self.state == "left":
            if self.pos[0] < 550:
                self.pos[0] += self.move[1]
                self.rect.x = self.pos[0]
                self.rect.y = self.pos[1]

    def flip_sprite(self):
        """Flips sprite horizontaly."""
        self.image = pygame.transform.flip(self.image, -1, 0)

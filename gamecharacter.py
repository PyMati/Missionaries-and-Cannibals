import pygame

class GameCharacter(pygame.sprite.Sprite):
    def __init__(self, screen_surface, pos, image_path):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = screen_surface.center
        self.pos = pos
    
    def flip_sprite(self):
        self.image = pygame.transform.flip(self.image, -1, 0)
        

class Raft(pygame.sprite.Sprite):
    def __init__(self, screen_surface, pos, image_path):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = screen_surface.center
        self.pos = pos
        self.is_someone = False
    
    def move_right(self):
        if self.is_someone:
            self.is_target = False
            if not self.is_target:
                if self.pos[0] < 500:
                    print(self.pos)
                    self.pos[0] = self.pos[0] + 2.5
                else:
                    self.is_target = True
    
    def move_left(self):
        if self.is_someone:
            self.is_target = False
            if not self.is_target:
                if self.pos[0] > 200:
                    print(self.pos)
                    self.pos[0] = self.pos[0] - 2.5
                else:
                    self.is_target = True
                
    def get_on(self):
        self.is_someone = True
    
    def leave(self):
        self.is_someone = False
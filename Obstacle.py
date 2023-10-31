import pygame
from random import randint


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == 'storm':
            storm_1 = pygame.image.load(
                'graphics/storm/sprite_storm1.png').convert_alpha()
            storm_2 = pygame.image.load(
                'graphics/storm/sprite_storm2.png').convert_alpha()
            storm_3 = pygame.image.load(
                'graphics/storm/sprite_storm3.png').convert_alpha()
            storm_4 = pygame.image.load(
                'graphics/storm/sprite_storm4.png').convert_alpha()
            storm_5 = pygame.image.load(
                'graphics/storm/sprite_storm5.png').convert_alpha()
            storm_6 = pygame.image.load(
                'graphics/storm/sprite_storm6.png').convert_alpha()
            storm_7 = pygame.image.load(
                'graphics/storm/sprite_storm7.png').convert_alpha()
            storm_8 = pygame.image.load(
                'graphics/storm/sprite_storm8.png').convert_alpha()
            self.frames = [storm_1, storm_2, storm_3, storm_4, storm_5, storm_6,
                           storm_7, storm_8]
            y_pos = 190
        else:
            snail_1 = pygame.image.load(
                'graphics/snail/sprite_snail1.png').convert_alpha()
            snail_2 = pygame.image.load(
                'graphics/snail/sprite_snail2.png').convert_alpha()
            self.frames = [snail_1, snail_2, snail_2]
            y_pos = 300

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.05
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

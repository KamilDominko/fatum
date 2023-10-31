import os

import pygame
from random import randint

import useful


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, game, type):
        super().__init__()
        self.game = game
        self.frames = []

        if type == 'storm':
            self._load_imgs(type)
            y_pos = 190
        elif type == "snail":
            self._load_imgs(type)
            y_pos = game.ground_y

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(
            randint(int(game.screen_w * 1.2), int(game.screen_w * 1.6)),
            y_pos))

    def _load_imgs(self, type):
        """Funkcja ładująca obrazy do animacji dla sprite'a."""

        folder_path = f"graphics/{type}"
        file_count = len(os.listdir(folder_path))
        for i in range(file_count):
            img = pygame.image.load(f"{folder_path}/sprite_{type}"
                                    f"{i + 1}.png").convert_alpha()
            img = useful.scale_image(img, self.game.scale_x, self.game.scale_y)
            self.frames.append(img)

    def animation_state(self):
        self.animation_index += 0.05
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= self.game.settings.enemy_speed
        self.destroy()

    def destroy(self):
        if self.rect.right <= 0:
            print("ZGON")
            self.kill()

import pygame
import useful


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        player_walk_1 = pygame.image.load(
            'graphics/player/sprite_cuteknight1.png').convert_alpha()
        player_walk_1 = useful.scale_image(player_walk_1,
                                           game.scale_x, game.scale_y)
        player_walk_2 = pygame.image.load(
            'graphics/player/sprite_cuteknight2.png').convert_alpha()
        player_walk_2 = useful.scale_image(player_walk_2,
                                           game.scale_x, game.scale_y)
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load(
            'graphics/player/sprite_knight_jump.png').convert_alpha()
        self.player_jump = useful.scale_image(self.player_jump,
                                              game.scale_x, game.scale_y)

        self.image = self.player_walk[self.player_index]
        self.player_y = game.ground_y - self.image.get_height()
        self.rect = self.image.get_rect(
            midbottom=(80 * game.scale_x, self.player_y))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
        self.jump_sound.set_volume(0.5)
        self.max_health = self.game.settings.player_health
        self.current_health = self.game.settings.player_health

    def _display_player_hp(self):
        """Wyświetla na środku na dole ekranu pasek zdrowia gracza."""
        # RED BAR
        x = self.game.screen_w / 2 - self.game.settings.hp_bar_width / 2
        y = self.game.screen_h - self.game.settings.hp_bar_height
        hp_bar_red = pygame.Rect((x, y), (self.game.settings.hp_bar_width,
                                          self.game.settings.hp_bar_height))
        pygame.draw.rect(self.game.screen, self.game.settings.RED, hp_bar_red)
        # GREEN BAR
        proc_hp = self.game.settings.hp_bar_width * (self.current_health /
                                                     self.max_health)
        hp_bar_green = pygame.Rect((x, y),
                                   (proc_hp, self.game.settings.hp_bar_height))
        pygame.draw.rect(self.game.screen, self.game.settings.GREEN,
                         hp_bar_green)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= self.game.ground_y:
            self.gravity = self.game.settings.player_jump * self.game.scale_x
            print(self.game.scale_y, self.game.scale_x)
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= self.game.ground_y:
            self.rect.bottom = self.game.ground_y

    def animation_state(self):
        if self.rect.bottom < self.game.ground_y:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self._display_player_hp()
        self.player_input()
        self.apply_gravity()
        self.animation_state()

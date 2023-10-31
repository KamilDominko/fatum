import pygame
from Settings import Settings
from Player import Player
from Obstacle import Obstacle
import useful

from random import choice

pygame.font.init()
pygame.mixer.init()


class Game:
    def __init__(self):
        # pygame.init()
        self.isRunning = True
        self.settings = Settings()
        self.screen_w = self.settings.screen_width
        self.screen_h = self.settings.screen_height
        self.screen = pygame.display.set_mode((self.screen_w, self.screen_h))
        pygame.display.set_caption(self.settings.game_title)
        self.clock = pygame.time.Clock()
        self.game_active = False
        self.start_time = 0
        self.score = 0

        # Resources.
        self.font = pygame.font.Font('font/Pixeltype.ttf', 50)
        self.bg_music = pygame.mixer.Sound('audio/Hoppin.mp3')
        self.bg_music.play(loops=-1)
        self.bg_img = pygame.image.load('graphics/morninghill.png').convert()

        self.scale_x, self.scale_y = useful.get_scale(self.screen, self.bg_img)

        self.bg_img = useful.scale_image(self.bg_img, self.scale_x,
                                         self.scale_y)
        self.ground_img = pygame.image.load('graphics/ground.png').convert()
        self.ground_img = useful.scale_image(self.ground_img, self.scale_x,
                                             self.scale_y)

        self.ground_y = self.screen.get_height() - self.ground_img.get_height()


        self.player = Player(self)

        # Groups
        self.players = pygame.sprite.GroupSingle()
        self.players.add(self.player)

        self.obstacle_group = pygame.sprite.Group()

        # Intro screen
        self.player_stand = pygame.image.load(
            'graphics/player/sprite_knight_stand.png').convert_alpha()
        self.player_stand = pygame.transform.rotozoom(self.player_stand, 0, 2)
        self.player_stand_rect = self.player_stand.get_rect(center=(400, 200))

        self.title_msg = self.font.render(self.settings.game_title, False,
                                          self.settings.font_color)
        self.title_msg_rect = self.title_msg.get_rect(center=(400, 80))

        self.start_msg = self.font.render('Press space to jump', False,
                                          self.settings.font_color)
        self.start_msg_rect = self.start_msg.get_rect(center=(400, 330))

        # Timer
        self.obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_timer, 1500)

    def _display_start_screen(self):
        self.screen.fill(self.settings.theme_color)
        self.screen.blit(self.player_stand, self.player_stand_rect)
        self.screen.blit(self.title_msg, self.title_msg_rect)
        if self.score == 0:
            self.screen.blit(self.start_msg, self.start_msg_rect)
        else:
            score_msg = self.font.render(
                f'Your score: {self.score}', False, self.settings.font_color)
            score_msg_rect = score_msg.get_rect(center=(400, 330))
            self.screen.blit(score_msg, score_msg_rect)

    def display_score(self):
        current_time = int(pygame.time.get_ticks() / 1000) - self.start_time
        score_surf = self.font.render(f'Score: {current_time}', False,
                                      self.settings.BLACK)
        score_rect = score_surf.get_rect(center=(400, 50))
        self.screen.blit(score_surf, score_rect)
        return current_time

    def _check_collision(self):
        if pygame.sprite.spritecollide(self.players.sprite, self.obstacle_group,
                                       True):
            # self.obstacle_group.empty()
            # self.game_active = False
            self.player.current_health -= self.settings.damage
            if self.player.current_health <= 0:
                self.game_active = False

    def _update_screen(self):
        self.screen.blit(self.bg_img, (0, 0))
        # self.screen.blit(self.ground_img, (0, 300 * self.scale_x))

        self.screen.blit(self.ground_img, (0, self.ground_y))
        self.score = self.display_score()

        self.players.draw(self.screen)
        self.players.update()

        self.obstacle_group.draw(self.screen)
        self.obstacle_group.update()

    def _reset_game(self):
        self.player.current_health = self.settings.player_health

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.isRunning = False

            if self.game_active:
                if event.type == self.obstacle_timer:
                    self.obstacle_group.add(Obstacle(self,
                        choice(['storm', 'snail', 'snail', 'snail'])))

            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self._reset_game()
                    self.game_active = True
                    self.start_time = int(pygame.time.get_ticks() / 1000)

    def run(self):
        while self.isRunning:
            self._check_events()
            if self.game_active:
                self._update_screen()
                self._check_collision()
            else:
                self._display_start_screen()
            pygame.display.update()
            self.clock.tick(self.settings.fps)
        pygame.quit()

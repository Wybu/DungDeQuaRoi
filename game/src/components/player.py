import pygame
import pygame.transform
from pygame.locals import *

from src.config import Config
from src.services.visualization_service import VisualizationService

vec = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = VisualizationService.get_player_image()
        self.image_st = VisualizationService.get_santa_hand()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.pos = vec((180, 550))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.player_position = vec(0, 0)
        self.control_mode = 'keyboard'
    def back_hand(self):
        self.image = VisualizationService.get_back_hand()
    def jump(self):
        
        self.vel.y = -Config.JUMP

    def change_gameplay(self):
        if self.control_mode == 'keyboard':
            self.control_mode = 'mouse'
        else:
            self.control_mode = 'keyboard'
    def update(self):
        self.acc = vec(0, 0)

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT] or pressed_keys[K_a]:
            self.acc.x = -Config.ACC
        if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
            self.acc.x = +Config.ACC
        if pressed_keys[K_UP] or pressed_keys[K_w]:
            self.acc.y = -Config.ACC
        if pressed_keys[K_DOWN] or pressed_keys[K_s]:
            self.acc.y = +Config.ACC

        self.acc.x += self.vel.x * Config.FRIC
        self.acc.y += self.vel.y * Config.FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.player_position = self.pos.copy()


        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.pos = vec(mouse_x, mouse_y)

        self.player_position = self.pos.copy()

        if self.pos.x > Config.WIDTH:
            self.pos.x = Config.WIDTH
        if self.pos.x < 0:
            self.pos.x = 0
        if self.pos.y > Config.HEIGHT:
            self.pos.y = Config.HEIGHT
        if self.pos.y < 200:
            self.pos.y = 200

        self.rect.center = self.pos

    def draw(self, screen):
        original_width, original_height = self.image.get_size()
        original_width, original_height = self.image.get_size()
        scaled_width = int(original_width * 1) #cai nay de chia ti le khung hinh
        scaled_height = int(original_height * 1)
        scaled_image = pygame.transform.scale(self.image, (scaled_width, scaled_height))
        screen.blit(VisualizationService.get_santa_hand(), (self.rect.x + 10, self.rect.y - 0))
        screen.blit(scaled_image, self.rect)

    def reset(self):
        self.pos = vec((180, 550))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def hole(self):
        self.image = VisualizationService.get_hole_image()  # Assuming you have a method to get the hole image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.pos = vec(mouse_x, mouse_y)
        self.rect.center = self.pos

"""
    def update(self):
        self.acc = vec(0, 0)

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT] or pressed_keys[K_a]:
            self.acc.x = -Config.ACC
        if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
            self.acc.x = +Config.ACC
        if pressed_keys[K_UP] or pressed_keys[K_w]:
            self.acc.y = -Config.ACC
        if pressed_keys[K_DOWN] or pressed_keys[K_s]:
            self.acc.y = +Config.ACC

        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.pos = vec(mouse_x, mouse_y)

        self.acc.x += self.vel.x * Config.FRIC
        self.acc.y += self.vel.y * Config.FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.player_position = self.pos.copy()

        if self.pos.x > Config.WIDTH:
            self.pos.x = Config.WIDTH
        if self.pos.x < 0:
            self.pos.x = 0
        if self.pos.y > Config.HEIGHT:
            self.pos.y = Config.HEIGHT
        if self.pos.y < 200:
            self.pos.y = 200

        self.rect.center = self.pos
"""






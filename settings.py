import pygame as pg
import math
import random
import time

heal_allowed = True
spawn_toggle = True
shoot_enemy = False
shoot_player = True
screen = pg.display.set_mode((900, 900))
max_health = 5
heal = 0.5
healing_timer = 1
player_speed = 30

# Создание группы пуль
bullets = pg.sprite.Group()
# Создание вржеской группы
enemies = pg.sprite.Group()
# Создание персонажа
player_group = pg.sprite.Group()
all_sprites = pg.sprite.Group()
tiles = pg.sprite.Group()

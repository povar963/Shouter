import pygame as pg
import math
import random
import time

# Правила
heal_allowed = True  # вкл/выкл хил
spawn_toggle = True  # вкл/выкл спавн
shoot_enemy = True   # вкл/выкл огонь врага
shoot_player = True  # вкл/выкл огонь игрока
# Экран
screen = pg.display.set_mode((900, 900))
# Статы игрока
max_health = 5
heal = 0.5
healing_timer = 1
player_speed = 30
# Переменная для отрисовки тайлов
start_tile_pos = [0, 0]

# Создание групп
all_sprites = pg.sprite.Group()  # Создание общей группы
bullets = pg.sprite.Group()  # Создание группы пуль
enemies = pg.sprite.Group()  # Создание вржеской группы
player_group = pg.sprite.Group()  # Создание персонажа
tiles = pg.sprite.Group()  # Создание группы тайлов

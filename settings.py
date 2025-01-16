import pygame as pg
import math
import random
import time

spawn_toggle = True
shoot_enemy = False
shoot_player = True
screen = pg.display.set_mode((900, 900))

# Создание группы пуль
bullets = pg.sprite.Group()
# Создание вржеской группы
enemies = pg.sprite.Group()
# Создание персонажа
player_group = pg.sprite.Group()

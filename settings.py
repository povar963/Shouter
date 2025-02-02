import pygame as pg
import math
import random
import time

pg.init()


class Button:
    f1 = pg.font.Font(None, 36)

    def __init__(self, text: str, color: str, x: int, y: int, lx: int, ly: int):
        self.text = text
        self.color = color
        self.x = x
        self.lx = lx
        self.y = y
        self.ly = ly

    def draw(self):
        btn = pg.draw.rect(screen, self.color, ((self.x, self.y), (self.lx, self.ly)), 2)
        text1 = self.f1.render(self.text, 1, (0, 180, 0))
        x = btn.width / 2 + self.x - text1.get_width() / 2
        y = btn.height / 2 + self.y - text1.get_height() / 2

        screen.blit(text1, (x, y))

    def update(self):
        self.draw()


# Правила
heal_allowed = True  # вкл/выкл хил
spawn_toggle = True  # вкл/выкл спавн
shoot_enemy = True  # вкл/выкл огонь врага
shoot_player = True  # вкл/выкл огонь игрока
# Экран
with open("settings/screen.txt", "r") as f:
    w, h, mode, difficult = f.readline().split("-")
    difficult = int(difficult)
with open("settings/screen.txt", "w") as f:
    f.write(f"{w}-{h}-0-{difficult}")
resolution = (w, h)
screen = pg.display.set_mode((int(w), int(h)))
# Статы игрока
max_health = 5
heal = 0.5
healing_timer = 2
player_speed = 30
# Переменная для отрисовки тайлов
start_tile_pos = [0, 0]

# Создание групп
all_sprites = pg.sprite.Group()  # Создание общей группы
bullets = pg.sprite.Group()  # Создание группы пуль
enemies = pg.sprite.Group()  # Создание вржеской группы
player_group = pg.sprite.Group()  # Создание персонажа
tiles = pg.sprite.Group()  # Создание группы тайловdddddd
